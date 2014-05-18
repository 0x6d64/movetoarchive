# movetoarchive


Script to move files into a year/month structure, according to the time of its last change.
## basic usage
Copy movetoarchive.py into a folder that is included in your system path (see this [wikipedia article](http://en.wikipedia.org/wiki/PATH_(variable)) on how to do this). Make the script executable by excuting `chmod +x ./movetoarchive.py` in that folder.

Then call `movetoarchive.py` in a folder of your choice to create a year/month structure and move your files in that structure.

## arguments
movetoarchive accepts the following arguments:

**-m, --month:** create subfolders for years and months (default)  
**-y --year:** only create folders for years (obviously cannot be used with --month)  
**-v, --verbose:** extra verbose output  
**-q, --quiet:** no output at all (can't use with -v, use this e.g. in your cron jobs)

## limitations
- movetoarchive was not tested on any platform different from OS X (10.7.5). I don't know how all the python *shutil* library stuff will work e.g. on Windows.
- maybe others

## bugs
Feel free to comment on that.