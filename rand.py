#!/usr/bin/env python
import sys,random
lines = open(sys.argv[1]).readlines()
olines=[]
while lines:
    olines.append(lines.pop(random.randrange(len(lines))))

sys.stdout.write("".join(olines))
