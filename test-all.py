#! /usr/bin/env python3

import os
import re
from glob import glob
import subprocess as sub


cdir = os.getcwd ()
m = re.search ("test$", cdir)
# On top level change to test directory
if m is None:
    os.chdir ("test")

for i in glob ("*.ltx"):
    cmd = "pdflatex -halt-on-error " + i + " > /dev/null"
    #print (cmd)
    try:
        out = sub.check_output (cmd, shell = True).decode ("utf8")
    except sub.CalledProcessError as e:
        print ("Error on", i)
        
    
    
