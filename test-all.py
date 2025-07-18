#! /usr/bin/env python3

import os
from glob import glob
import subprocess as sub

for i in glob ("*.ltx"):
    cmd = "pdflatex -halt-on-error " + i + " > /dev/null"
    #print (cmd)
    try:
        out = sub.check_output (cmd, shell = True).decode ("utf8")
    except sub.CalledProcessError as e:
        print ("Error on", i)
        
    
    
