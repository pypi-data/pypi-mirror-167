# Copyright DatabaseCI Pty Ltd 2022

import sys
from uuid import uuid4

import databaseci
from migra import Migration
from requests.exceptions import HTTPError
from schemainspect import get_inspector
from sqlbag import S

from .call import get_response
from .conn import trans
from .copy import handle_copy_instruction, print_status
from .schema import create_fk_constraints, drop_fk_constraints, temporarily_dropped_fks
from .summary import Summary


def validate_config(config, summary):
    from databaseci import quoted_identifier

    cannot_find_tables = []
    keyless_tables = []

    inspected_tables = set([_[0] for _ in summary["tables"]])

    for schema, tables in (config.get("schemas") or {}).items():
        if tables:
            for table, tconf in tables.items():
                tname = ".".join(
                    [
                        quoted_identifier(schema, always_quote=True),
                        quoted_identifier(table, always_quote=True),
                    ]
                )

                if tname not in inspected_tables:
                    cannot_find_tables.append(tname)

    for table in summary["tables"]:
        name, cols, c = table

        if not c:
            keyless_tables.append(name)

    if keyless_tables:
        print(
            "\nSubsetting requires each table to have a primary key or other unique constraint."
        )
        print("\nThe following tables do not have such a constraint:")

        for t in keyless_tables:
            print(t)
        print()
        return False

    if cannot_find_tables:
        print(f"The following tables in the config are not found in the database:")

        for t in cannot_find_tables:
            print(t)
        print()
        return False

    return True


def do_subset(config: dict):
    safe_config = dict(config)

    do_clear_check = safe_config.pop("do_clear_check", True)
    do_schema_sync = safe_config.pop("do_schema_sync", True)
    drop_and_recreate_copy_db = safe_config.pop("drop_and_recreate_copy_db", False)
    wipe_tables_copy_db = safe_config.pop("wipe_tables_copy_db", False)
    ignore_extension_versions = safe_config.pop("ignore_extension_versions", False)
    yes_really_drop = safe_config.pop("yes_really_drop", False)

    try:
        real_db_url = safe_config.pop("real_db_url")
        copy_db_url = safe_config.pop("copy_db_url")
    except KeyError:
        print("ERROR: Both real_db_url and copy_db_url need to be set in config.")

    print("Inspecting database...")

    with S(real_db_url) as s:
        ii = get_inspector(s)
        summary = Summary.get_schema_summary(ii)

    if not summary["linkages"]:
        print("Aborting. It looks like your database has no linkages.")

        sys.exit(1)

    if not summary["tables"]:
        print("Aborting. It looks like your database has no tables.")
        sys.exit(1)

    print("Inspection complete.\n")

    print("Checking config...")
    if not validate_config(config, summary):
        print("Errors in config, stopping.")
        sys.exit(1)
    print("Config OK.\n")

    if do_clear_check:
        print("Confirming copy destination database is empty...")
        with S(copy_db_url) as s:
            csummary = Summary.get_schema_summary(get_inspector(s))

        if csummary["tables"]:
            print(csummary)
            print("Aborting: Copy destination already contains tables!")

            sys.exit(1)
        else:
            print("Confirmed.\n")

    state = {}

    state["w"] = {_[0]: set() for _ in summary["tables"]}
    state["a"] = {_[0]: set() for _ in summary["tables"]}

    with S(real_db_url) as ss:
        with trans(ss.connection().connection) as t:

            if drop_and_recreate_copy_db:
                print("Dropping/recreating copy...")
                copy_db = databaseci.db(copy_db_url)
                name = copy_db.name

                template1 = copy_db.sibling("template1")
                template1.create_db(
                    name, drop_if_exists=True, yes_really_drop=yes_really_drop
                )
                print("Done.")
                print()

            if do_schema_sync or drop_and_recreate_copy_db:
                i = get_inspector(ss)

                print("Replicating schema on copy destination.")
                with S(copy_db_url) as ssc:
                    with trans(ssc.connection().connection) as tc:

                        m = Migration(
                            ssc, i, ignore_extension_versions=ignore_extension_versions
                        )
                        m.set_safety(False)

                        m.add_all_changes()

                        m.apply()

            with S(copy_db_url) as ssc:
                with trans(ssc.connection().connection) as tc:
                    ic = get_inspector(ssc)

                    print("Dropping constraints...")
                    for c in drop_fk_constraints(ic):
                        tc.ex(c)

                    if wipe_tables_copy_db:
                        print("Wiping tables on copy...")
                        for fqtn in ic.tables:
                            tc.ex(f"delete from {fqtn}")

            print("Copy setup complete.\n")

            base = dict(inspected=summary, **safe_config)

            base["step"] = 0
            base["run_id"] = str(uuid4())

            result = {}

            print("Copying subsetted rows...\n")

            with S(copy_db_url) as ssc:
                with trans(ssc.connection().connection) as tc:
                    while True:
                        req = {**base, **result}

                        try:
                            response = get_response(req)
                        except HTTPError as e:
                            if e.response.status_code == 403:
                                print(
                                    "Access forbidden. Bad API key? If in doubt contact support@databaseci.com."
                                )

                            else:
                                print(
                                    "Unknown error - Likely this is a server error, and we're investigating. For more details please contact support@databaseci.com."
                                )

                            sys.exit(1)

                        if not response.get("carry_on"):
                            print()
                            break

                        handle_copy_instruction(response, state, t, tc)

                        result = dict(
                            done=True,
                            s=dict(
                                w={k: len(v) for k, v in state["w"].items()},
                                a={k: len(v) for k, v in state["a"].items()},
                            ),
                        )

            print("\nRows copied.\n")

    print("Applying constraints on subsetted copy...")
    if do_schema_sync:
        with S(copy_db_url) as ssc:
            with trans(ssc.connection().connection) as tc:
                for c in create_fk_constraints(ic):
                    tc.ex(c)

    print("Complete.")


def do_inspect(config: dict):
    raise NotImplementedError


def do_check(config: dict):
    safe_config = dict(config)

    print("Checking api_key:")

    try:
        req = dict(api_key=safe_config["api_key"], check="true")

    except LookupError:
        print("api_key not found in config file")
        sys.exit(1)

    try:
        resp = get_response(req)

        print("Connection successful - valid API key.")
        print()

    except HTTPError as e:
        if e.response.status_code == 403:
            print(
                "Access forbidden. Bad API key? If in doubt contact support@databaseci.com."
            )

        else:
            print(
                "Unknown error - Likely this is a server error, and we're investigating. For more details please contact support@databaseci.com."
            )

        sys.exit(1)

    real_db_url = safe_config.pop("real_db_url")
    copy_db_url = safe_config.pop("copy_db_url")

    print("Checking production database connectivity...")

    with S(real_db_url) as s:
        s.execute("select 1")

    print("Prod connection successful.")
    print()

    print("Checking copy/destination database connectivity...")

    with S(real_db_url) as s:
        s.execute("select 1")

    print("Copy/destination connection successful.")
    print()
