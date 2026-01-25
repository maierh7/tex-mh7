#! /usr/bin/env python3

import os
import re

ti = os.environ ["TEXINPUTS"]

arr = re.split (":", ti)
for i in arr:
    #print (i)
    if os.path.isdir (i) is False:
        print ("Error: ", i, " does not exist!")
        
