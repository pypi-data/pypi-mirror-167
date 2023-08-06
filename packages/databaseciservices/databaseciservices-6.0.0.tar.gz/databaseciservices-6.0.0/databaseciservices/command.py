# Copyright DatabaseCI Pty Ltd 2022

from pathlib import Path

import click
import yaml

from .do import do_check, do_inspect, do_subset


def init_commands(cli):
    @cli.command(help="Subset a database.")
    @click.argument("file", type=click.Path(exists=True), nargs=1)
    def subset(file):
        with Path(file).open() as f:

            j = yaml.safe_load(f)

        do_subset(j)

    @cli.command(help="Inspect a database.")
    @click.argument("file", type=click.Path(exists=True), nargs=1)
    def inspect(file):
        with Path(file).open() as f:

            j = yaml.safe_load(f)
        do_inspect(j)

    @cli.command(help="Check subsetting config.")
    @click.argument("file", type=click.Path(exists=True), nargs=1)
    def checksubsetconfig(file):
        with Path(file).open() as f:

            j = yaml.safe_load(f)
        do_check(j)
