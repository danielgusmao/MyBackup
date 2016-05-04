#!/usr/bin/env python
# MyBackup - A backup script to exercise my python practice!
# Copyright (C) <2016>  <Jean Landim - jewanbb@gmail.com> 
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

# a silly script in python to backup my files.

import sys, os, tarfile, time

class MyBackup():

    FileConfig=os.environ.get('HOME')+'/.mybackup.conf' # get path and setted filename of fileconfig (fileconfig is used to store full path to backup it items)
    EmptyFile=0 # 
    if os.path.exists(FileConfig) == True:
        FileTo=open(FileConfig,'at') # append 
    else:
        FileTo=open(FileConfig,'wt') # write, (create)
    def __init__(self):
        # if file is empty, so advice to add files to backup.
        if os.path.getsize(MyBackup.FileConfig) == 0:  
           print("Empty file! Is needed to calling this script again to insert files to backup (with full path, please), with -a option")
           MyBackup.EmptyFile=1 # if file is empty so, isnt be possible to backup it
    def usage(self): # an usage message :)
        print('''MyBackup - Jean Landim (GPL) 2016:
                          -a add files to backup when script runs e.g.: $ MyBackup -a /home/foo/foofile
                          -l list files saved to backup, setted by the user
                          -d remove files from backup to do e.g.: $ MyBackup -d /home/foo/foofile
                          -h this usage/help.''')
        exit()
    def append_files(self,addfile): # add files to fileconfig. these files (with fullpath, please) will be backup ed
            if os.path.exists(addfile) == True:
                print("adding: ",addfile) 
                MyBackup.FileTo.write(addfile+'\n')
            else:
                print(addfile,"file doesnt exist")
    def list_files(self): # list files added to fileconfig. 
        MyBackup.FileTo=open(MyBackup.FileConfig,'rt')
        for listfile in MyBackup.FileTo:
            print(listfile.strip('\n'))
    def del_files(self,filestodel):
        allfiles=[]
        MyBackup.FileTo=open(MyBackup.FileConfig,'rt') # open file to read 
        
        for singlefile in MyBackup.FileTo:
            allfiles.append(singlefile.strip('\r\n'))
        
        numbersoffiles=len(allfiles)
        MyBackup.FileTo.close()
        
        MyBackup.FileTo=open(MyBackup.FileConfig,'w')
        for n in range(numbersoffiles):
              print(allfiles[n])
              if allfiles[n]==filestodel:
                 print("deleting: ",filestodel)
              else:
                 MyBackup.FileTo.write(allfiles[n]+'\n')
                  
    def backup(self): # so, "let him run wild and dont care"
        if MyBackup.EmptyFile ==1:
           exit()

        filename=os.environ.get('USER')+time.strftime('%y%d%m%H%M')+".tar"
        backupfile=tarfile.open(filename,'w')
       
        files=open(MyBackup.FileConfig,'r') 
        for i in files:
            i=i.strip('\n') 
            print("saving: ",i)
            backupfile.add(i)
        
        backupfile.close()
        files.close()
if __name__ == '__main__': # execute the script
    run=MyBackup() # create instance
    if len(sys.argv) > 1:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            run.usage()
        elif sys.argv[1] == "-l":
            run.list_files()
        elif sys.argv[1] == "-d": 
            for i in sys.argv[2:]:
                run.del_files(i)
        elif sys.argv[1] == "-a":
            for i in sys.argv[2:]:
                run.append_files(i)
        else:
            print("Call the script again with -h option")
    else:
        run.backup()

# Seg Abr 25 22:58:30 BRT 2016
