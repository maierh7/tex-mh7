#! /usr/bin/env python3

import os
import re

exts = (
    ".pdf",
    ".log",
    ".aux",
    )

for r, d, f in os.walk ("."):
    m = re.match (r"^\./\.git", r)
    if m:
        continue
    for i in f:
        _, e = os.path.splitext (i)

        if e in exts:
            fn = r + "/" + i
            print ("Delete:", fn)
            os.remove (fn)
            continue
