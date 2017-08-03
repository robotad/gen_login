#!/usr/bin/env python
import sys
SEEN = set()


def combine(str1, str2):
    for s1 in range(0, len(str1) + 1):
        for s2 in range(0, len(str2) + 1):
            for sp in ["", ".", "-", "_"]:
                combo = str1[:s1] + sp + str2[:s2]
                if combo not in SEEN and len(combo) > 1:
                    print combo
                    SEEN.add(combo)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage: %s names.txt" % (sys.argv[0])
        sys.exit(0)

    for line in open(sys.argv[1]):
        name = ''.join([c for c in line if  c == " " or  c.isalpha()])

        tokens = name.lower().split()
        fname = tokens[0]
        lname = tokens[-1]

        combine(fname, lname)
        combine(lname, fname)