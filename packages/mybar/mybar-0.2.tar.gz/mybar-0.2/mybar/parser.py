from string import Formatter


switch = [
    ('mins', 'secs', 60),
    ('hours', 'mins', 60),
    ('days', 'hours', 24),
    ('weeks', 'days', 7),
]

keys = [
    'secs',
    'mins',
    'hours',
    'days',
    'weeks',
]

def make_dct(n, fields):
    d = {'secs': n}
    indexes = tuple(keys.index(f) for f in fields)
    granularity = keys[min(indexes)]

    reps = max(indexes)
    for i in range(reps):
        fname, prev, mod = switch[i]
        d[fname], d[prev] = divmod(d[prev], mod)
    return d


def nested_join(sep, it):
    return sep.join(''.join(t) for t in it)


def format_elapsed(
    fmt: str,
    sep: str,
    n,
    dynamic: bool = True
):
    stuff = tuple(
        tuple(Formatter().parse(sub))
        for sub in fmt.split(sep)
    )

    fnames = tuple(
        name
        for thing in stuff
        for tup in thing
        if (
        name := tup[1])
    )
    #print(fnames)

    d = make_dct(n, fnames)

    #print(j)

    last_was_nonzero = True

    j = []
    for i, splitted in enumerate(stuff):
        section = []
        
        for tup in splitted:
            buf = ""

            #print(f"{last_was_nonzero = }")
            #print(i, tup)

            match tup:
                case [lit, None, None, None,]:
                    if last_was_nonzero:
                        #print("valid", lit)
                        buf += lit

                case [lit, field, spec, conv]:
                    val = d.get(field)
                    #print(f"{val = }!")
                    if dynamic:
                        if not val:
                            last_was_nonzero = False
                            continue

                    if lit is not None:
                        buf += lit
                    buf += str(val)
                    last_was_nonzero = True

                case blarg:
                    print(f"{i}: {blarg = !r}!")

            #print(f"{buf = }")
            if buf:
                section.append(buf)

        if section:
            j.append(section)

    return nested_join(sep, j)
    return j


