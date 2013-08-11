#!/opt/local/bin/python
# movetoarchive - quickly archive files in a year/month folder structure
# (c) 2013 by Martin Demling
# License: GPL3
# https://github.com/0x6d64/ fixme: add github URL

import os 
import shutil
import sys
import time
#---------------------------------    
def PrintSeparator():
    if sys.stdout.isatty():
        rows, columns = os.popen('stty size', 'r').read().split()
        TerminalRows = int(rows)
        TerminalColumns = int(columns)
    else:
        TerminalRows = 0
        TerminalColumns = 30
    print(TerminalColumns * "-")
#---------------------------------
# PrintSeparator()
# print "debug-info:"
# print "in dir: " + os.getcwd()
# 
# for index, arg in enumerate(sys.argv):
#     print str(index) + ". arg: " + str(arg)
# PrintSeparator()

CurrentDir = os.getcwd()
FileCount = 0
CreateCount = 0

for file in os.listdir(CurrentDir):
    if os.path.isfile(file):
        TimeOfLastChange = time.localtime(os.path.getmtime(file))
        YearString = str(TimeOfLastChange.tm_year)
        MonthString = str(TimeOfLastChange.tm_mon)
        if len(MonthString) == 1:
            MonthString = "0" + MonthString  # pad one digit numbers with zero
        YearDirAbspath = CurrentDir + "/" + YearString
        MonthDirAbspath = YearDirAbspath + "/" + YearString + "-" + MonthString  # dir in format "2013-9"
        if not os.path.isdir(YearDirAbspath):
            os.mkdir(YearDirAbspath, 0755)
            CreateCount += 1
        if not os.path.isdir(MonthDirAbspath):
            os.mkdir(MonthDirAbspath, 0755)
            CreateCount += 1
        shutil.move(file, MonthDirAbspath)
        FileCount += 1

print "%d files moved and %d directories created" % (FileCount, CreateCount)