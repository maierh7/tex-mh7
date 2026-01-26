#! /usr/bin/env python3

import re
import subprocess as sub

with open ("FEDORA") as fp:

    cmd = "sudo dnf install "
    get_pack = False
    for i in fp:
        i = i.strip ("\n")
        #print (i)
        m1 = re.match (r"^\*\* Install", i)
        if m1:
            get_pack = True
            continue
        m2 = re.match (r"^\*\* org-mode", i)
        if m2:
            break

        m3 = re.match (r"^dnf install (.*)$" ,i)
        if m3:
            pck = m3.group (1)
            cmd += pck + " "

    print (cmd)
    sub.run (cmd, shell=True)
