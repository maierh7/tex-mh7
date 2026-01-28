#! /usr/bin/env python3

import os
import re
from glob import glob
import subprocess as sub

dirs = ("test", "ct_test")

rdir = os.getcwd()
print (rdir)
def comp (dir):
    wdir = rdir + "/" + dir
    os.chdir (wdir)

    for i in glob ("*.[lt][et]x"):
        cmd = "pdflatex -halt-on-error " + i + " > /dev/null"
        # print (cmd)
        # continue
        
        try:
            out = sub.check_output (cmd, shell = True).decode ("utf8")
        except sub.CalledProcessError as e:
            print ("Error on", i)

for i in dirs:
    comp (i)
    
