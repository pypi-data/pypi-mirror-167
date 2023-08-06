# Copyright DatabaseCI Pty Ltd 2022

BATCH_SIZE = 1000

# from console.utils import clear_lines

import sys

from .paging import get_page
from .util import batched, chunk

pl = 0


def q(x):
    x = x.replace("'", "''")
    return f"'{x}'"


def ft(t):
    if not t:
        return "Empty."

    k = list(t[0])

    ttt = [str(type(_).__name__) for _ in t[0].values()]

    st = [{k: str(v) for k, v in r.items()} for r in t]

    st.insert(0, {k: k.upper() for k in k})

    w = {_: 0 for _ in k}

    for r in st:
        for kk in k:
            l = len(r[kk])
            if w[kk] < l:
                w[kk] = l

    for r in st:
        for tt, kk in zip(ttt, k):
            ww = w[kk]

            s = r[kk]

            if tt == "str":
                r[kk] = s.ljust(ww)

            else:
                r[kk] = s.rjust(ww)

    return "\n".join(" ".join(x.values()) for x in st)


def print_status(s, backtrack=False):
    global pl

    if pl and backtrack:
        for i in range(pl):
            sys.stdout.write("\033[K")
            sys.stdout.write("\033[F")

    a = s["a"]

    w = s["w"]

    t = list(set(w) | set(a))

    t.sort()

    rows = [dict(table=tt, loaded=len(a[tt]), remaining=len(w[tt])) for tt in t]

    rows.sort(key=lambda x: (x["loaded"] + x["remaining"], x["table"]))

    t = ft(rows)

    lines = t.splitlines()
    pl = len(lines)

    print(lines[-1])


def kfr(rows, pksi, exclude=None):
    exclude = exclude or set()

    if len(pksi) == 1:
        k = pksi[0]
        return set(x for row in rows if (x := row[k]) not in exclude and x is not None)

    return set(
        x
        for row in rows
        if (x := tuple(row[k] for k in pksi)) not in exclude and None not in x
    )


def print_table_status(s, t):
    print(
        f"{t.ljust(40)} {str(len(s['a'][t])).rjust(6)} {str(len(s['w'][t])).rjust(6)}"
    )


def do_select_instruction(i, t, tc, s):
    q = i["q"]

    bookmark = None

    while True:
        rows = get_page(
            t,
            q,
            ordering=",".join(i["pks"]),
            per_page=BATCH_SIZE,
            backwards=False,
            bookmark=bookmark,
        )

        if rows:
            a = kfr(rows, i["pksi"])

            tc.insert(i["table"], rows)

            s["a"][i["table"]] |= a
            s["w"][i["table"]] -= a

            for l, _, ii in i["lo"]:

                kk = kfr(rows, ii, exclude=s["a"][l])
                s["w"][l] |= kk

            for aa, bb in zip(i["li"], i["qq"]):
                l, iii, p, ii = aa
                do_inwards(t, l, iii, a, s, p, bb, ii)

            print_table_status(s, t=i["table"])

        if rows.paging.has_next:
            bookmark = rows.paging.next
        else:
            break
    # print_table_status(s, t=i['table'])


def paramspec(batch, x):
    def ff(n):
        return f"%({n})s"

    def r(batch):
        its = []

        if x > 1:
            for i, _ in enumerate(batch):
                v = ",".join(ff(f"ppp{i}_{j}") for j in range(x))
                v = f"({v})"
                its.append(v)
        else:
            for i, _ in enumerate(batch):
                v = ff(f"ppp{i}")
                v = f"({v})"
                its.append(v)

        return ", ".join(its)

    return f"""
    
select * from (values {r(batch)})
    """


def paramd(batch, x):
    d = {}

    for i, b in enumerate(batch):
        if x > 1:
            for j in range(x):
                k = f"ppp{i}_{j}"
                d[k] = b[j]
        else:
            k = f"ppp{i}"
            d[k] = b

    return d


from itertools import islice


def do_select_instruction2(i, t, tc, s):
    itt = i["table"]
    w = s["w"][itt]

    while True:
        batch = set(islice(w, BATCH_SIZE))

        if not batch:
            break

        x = len(i["pks"])
        q = i["q"]

        q = q.format(paramspec(batch, x))
        bookmark = None

        while True:
            rows = get_page(
                t,
                q,
                paramd(batch, x),
                ordering=",".join(i["pks"]),
                per_page=BATCH_SIZE,
                backwards=False,
                bookmark=bookmark,
            )

            tc.insert(itt, rows)

            s["a"][itt] |= batch
            s["w"][itt] -= batch

            for l, o, ii in i["lo"]:

                kk = kfr(rows, ii, exclude=s["a"][l])

                s["w"][l] |= kk

            for aa, bb in zip(i["li"], i["qq"]):
                l, iii, p, ii = aa
                do_inwards(t, l, iii, batch, s, p, bb, ii)

            print_table_status(s, t=i["table"])

            if rows.paging.has_next:
                bookmark = rows.paging.next
            else:
                break


def do_inwards(t, l, i, a, s, p, b, ii):
    if not a:
        return

    batch = a

    bookmark = None

    qq = b

    x = len(i)

    qq = qq.format(paramspec(batch, x))

    while True:

        rows = get_page(
            t,
            qq,
            paramd(batch, x),
            ordering=",".join(p),
            per_page=BATCH_SIZE,
            backwards=False,
            bookmark=bookmark,
        )

        if rows:
            a = kfr(rows, ii, exclude=s["a"][l])

            s["w"][l] |= a

        if rows.paging.has_next:
            bookmark = rows.paging.next
        else:
            break


def handle_copy_instruction(instruction, state, t, tc):
    if instruction["stage"] == 0:
        for i in instruction["inst"]:
            do_select_instruction(i, t, tc, state)

    elif instruction["stage"] == 1:
        for i in instruction["inst"]:
            do_select_instruction2(i, t, tc, state)

    else:
        raise ValueError("Server error - invalid instructions.")
