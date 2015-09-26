#!/usr/bin/python

import os, sys
from pyPdf import PdfFileWriter, PdfFileReader

print "Name ="+os.name

print "Current Dir ="+os.curdir


TargetDir = input("Get input target directory: ")

print "Target directory: "+TargetDir

ListDir = os.listdir(TargetDir)

included_extenstions = ['pdf'] ;
file_names = [fn for fn in os.listdir(TargetDir) if any([fn.endswith(ext) for ext in included_extenstions])];

print file_names


output = PdfFileWriter()

for fn in file_names:
    fh = file(TargetDir+fn, "rb")
    inputNames = PdfFileReader(fh)
    print "title = %s" % (inputNames.getDocumentInfo().title)
    NewDocTitle = inputNames.getDocumentInfo().title
    fh.close()
    os.rename(TargetDir+fn,TargetDir+NewDocTitle+".pdf")
    
