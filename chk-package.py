#! /usr/bin/env python3

import os
import re

tp=os.environ["TEXINPUTS"]

ign = (r"\.", r"tex-mh7")

lst = re.split (os.pathsep, tp)
for i in lst:
    pr = True
    for j in ign:
        m = re.search (j, i)
        #print (m)
        if m:
            pr = False
            break
    if pr is True:
        if os.path.isdir (i) is False:
            print (i)
