#!/opt/local/bin/python
# movetoarchive - quickly archive files in a year and month folder structure.
# The folder structure has year folders and year/year-month subfolders. Folders
# are created as needed, files are moved based on their date of last change.
# (c) 2013 by Martin Demling
# License: GPL3
# https://github.com/0x6d64/ fixme: add github URL

import sys
import os 
import time
import shutil
import argparse

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
parser = argparse.ArgumentParser()
group1 = parser.add_mutually_exclusive_group()
group1.add_argument("-m", "--month", help="create subfolders for years and months (default)", action="store_true")
group1.add_argument("-y", "--year", help="create subfolders for years", action="store_true")
group2 = parser.add_mutually_exclusive_group()
group2.add_argument("-v", "--verbose", help="verbose output (default)", action="store_true")
group2.add_argument("-q", "--quiet", help="quiet output", action="store_true")
args= parser.parse_args()
    
FolderMode = 0755
CurrentDir = os.getcwd() #get the directory where the script is run from
FileCount = 0 #only for stats
CreateCount = 0


for FilePath in os.listdir(CurrentDir): #handle all files in current dir
    if os.path.isfile(FilePath): #deal only with files, not folders
        if args.verbose:
            print("handling file %s") % FilePath
        TimeOfLastChange = time.localtime(os.path.getmtime(FilePath))
        YearString = str(TimeOfLastChange.tm_year)
        MonthString = str(TimeOfLastChange.tm_mon)
        
        if len(MonthString) == 1:
            MonthString = "0" + MonthString  # pad one digit numbers with zero
            
        YearDirAbspath = CurrentDir + "/" + YearString
        MonthDirAbspath = YearDirAbspath + "/" + YearString + "-" + MonthString  # dir in format "2013-9"
        
        if not os.path.isdir(YearDirAbspath):
            if args.verbose:
                print("creating folder ./%s") % YearString
            os.mkdir(YearDirAbspath, FolderMode)
            CreateCount += 1
        if not args.year:
            if not os.path.isdir(MonthDirAbspath):
                if args.verbose:
                    print("creating folder ./%s/%s") % (YearString, MonthString)
                os.mkdir(MonthDirAbspath, FolderMode)
                CreateCount += 1
        
        TempAttributes = os.stat(FilePath) #save file attributes in temp var
        if args.month:
            NewDirAbsPath = MonthDirAbspath
        else:
            NewDirAbsPath = YearDirAbspath
        shutil.move(FilePath, NewDirAbsPath)
        NewFileAbspath = NewDirAbsPath + "/" + os.path.basename(FilePath)
        os.utime(NewFileAbspath, (TempAttributes.st_atime, TempAttributes.st_mtime)) #restore file attributes
        FileCount += 1
        
if not args.quiet:
    print "%d files moved and %d directories created" % (FileCount, CreateCount)
