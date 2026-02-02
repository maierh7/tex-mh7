#! /usr/bin/env python3

import os
import re

import argparse as arg
import subprocess as sub

par = arg.ArgumentParser ()
par.add_argument ("file")
args = par.parse_args ()

biber_fn, _ = os.path.splitext (args.file)
print (biber_fn)

def pdf_latex ():
    sub.run ("pdflatex" + " " + args.file, shell=True)

pdf_latex ()
sub.run ("biber" + " " + biber_fn, shell=True)
pdf_latex ()
pdf_latex ()
