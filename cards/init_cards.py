#! /usr/bin/env python
# vim: set fileencoding=utf-8 :#
# pylint: disable=W0312
import sys
if __name__ == "__main__":
    if sys.argv[1] == "brick":
        cost='b'
    if sys.argv[1] == "gem":
        cost='g'
    if sys.argv[1] == "creature":
        cost='c'
    with open(sys.argv[1], 'r') as f:
        for line in f:
            name=line.split(':')[0].strip()
            rname = name.lower().replace(' ', '_')
            c=int(line.split(':')[1].strip())
            print("cp card.sample {}.card".format(rname))
            print("sed -i 's/Sample name/{}/' {}.card".format(name, rname))
            print("sed -i 's/ost\]/&\\n{}={}/' {}.card".format(cost, c, rname))
