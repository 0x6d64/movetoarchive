#!/opt/local/bin/python
# movetoarchive - quickly archive files in a year and month folder structure.
# The folder structure has year folders and year/year-month subfolders. Folders
# are created as needed, files are moved based on their date of last change.
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
#---------------------------------
FolderMode = 0755
CurrentDir = os.getcwd() #get the directory where the script is run from
FileCount = 0 #only for fancy stats
CreateCount = 0

for FilePath in os.listdir(CurrentDir):
    if os.path.isfile(FilePath):
        TimeOfLastChange = time.localtime(os.path.getctime(FilePath))
        YearString = str(TimeOfLastChange.tm_year)
        MonthString = str(TimeOfLastChange.tm_mon)
        if len(MonthString) == 1:
            MonthString = "0" + MonthString  # pad one digit numbers with zero
        YearDirAbspath = CurrentDir + "/" + YearString
        MonthDirAbspath = YearDirAbspath + "/" + YearString + "-" + MonthString  # dir in format "2013-9"
        if not os.path.isdir(YearDirAbspath):
            os.mkdir(YearDirAbspath, FolderMode)
            CreateCount += 1
        if not os.path.isdir(MonthDirAbspath):
            os.mkdir(MonthDirAbspath, FolderMode)
            CreateCount += 1
            
        stat = os.stat(FilePath)
        shutil.move(FilePath, MonthDirAbspath)
        #todo: preserve file stats
        #os.utime(my_new_file, (stat.st_atime, stat.st_mtime))
        FileCount += 1

print "%d files moved and %d directories created" % (FileCount, CreateCount)