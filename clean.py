#! /usr/bin/env python3

import os
import re

fns  = (
    "t9-bib-ref.tex",
    )
exts = (
    ".aux",
    ".bbl",
    ".bcf",
    ".blg",
    ".lbl",
    ".lof",
    ".log",
    ".lot",
    ".out",
    ".pdf",
    ".xml",
    ".toc",
    )

for r, d, f in os.walk ("."):
    m = re.match (r"^\./\.git", r)
    if m:
        continue
    
    for i in f:
        _, e = os.path.splitext (i)

        if e in exts or i in fns:
            fn = r + "/" + i
            print ("Delete:", fn)
            os.remove (fn)
            continue
