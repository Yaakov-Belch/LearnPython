    groups = []
    uniquekeys = []
    data = sorted(data, key=keyfunc)
    for k, g in groupby(data, keyfunc):
        groups.append(list(g))      # Store group iterator as a list
        uniquekeys.append(k)

Note: g becomes invalid in the next loop: need to convert it to a list
for later use.  But can loop over it.

Note: need to sort data before itertools.groupby

itertools.groupby
pandas.DataFrame.groupby
