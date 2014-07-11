RaspberryCloud
==============

Dropbox for Raspberry Pi! A fully functioning command-line Dropbox client built using the Dropbox Python API for Raspberry Pi. Features include downloading entire directories as zip files, editing files in a local editor, uploading/downloading, and many many more!

Dependencies
============

This was written in Python 2.7 and requires the Dropbox module to work.
You can get it by issuing this command:
```pip install dropbox```
wget is also required. If you don't have it already, you can install it in Raspbian by entering this into the Terminal.
```apt-get install wget```

Supported Systems
=================

Although it's only been tested on Ubuntu 12.04 and Raspbian, it should work on most operating systems, so long as they've installed the dependencies. However, it probably won't work on Windows since there is no support for Python curses.

Commands
========
```
mkdir ~ create a new folder
usage: mkdir absolue_path_to_folder
example: mkdir /Pictures/Family
optional arguments:
  -h, --help  show this help message and exit

rm ~ delete a file/folder
usage: rm absolute_path_to_file_1 absolute_path_to_file_2 absolute_path_to_file_3 etc.
example: rm /Random/Other /tps_report.txt
optional arguments:
  -h, --help  show this help message and exit
  
ls ~ print a list of files in the current directory
usage: ls
example: ls
optional arguments:
  -h, --help  show this help message and exit
  
cd ~ change to another directory
usage: cd directory_path_to_change_to
example: cd /Pictures
note: using cd by itslef will bring you back to the root directory
optional arguments:
  -h, --help  show this help message and exit
  
cp ~ copy a file/folder from one location to another
usage: cp absolute_path_to_file_with_filename new_path_to_file_with_filename
example: cp /School/Essay.pdf /School/History/Essay.pdf
note: if a different filename is given for the second arguement, the file will be copied and renamed 
optional arguments:
  -h, --help  show this help message and exit
  
mv ~ move a file/folder from one location to another
usage: mv absolute_path_to_file_with_filename new_path_to_file_with_filename
example: mv /Music/Playlist /Shared
note: if a different filename is given for the second arguement, the file will be moved and renamed 
special usage: just like in linux, you may use this command to rename a file also.
optional arguments:
  -h, --help  show this help message and exit
  
mlink ~ create a media link to an image/video/sound file from your Dropbox
usage: mlink absolute_path_to_file
example: mlink /Videos/important_video.mov
optional arguments:
  -h, --help  show this help message and exit
  
share ~ create a link to share a file/folder
usage: share absolute_path_to_file
example: share /Art/ConceptArt
optional arguments:
  -h, --help  show this help message and exit
  
upload ~ upload a file to the current directory
usage: upload path_to_local_file filename
example: /home/user/Documents/BeejCGuide.pdf BeejCguide.pdf
note: file can be drag and dropped from the local machine into the terminal window
optional arguments:
  -h, --help  show this help message and exit
  
dl ~ download files from current directory
usage: dl filename1 filename2 filename3 filename4 etc.
example: dl tps_reports.txt intro_to_c.pdf
optional arguments:
  -c, --compress  convert file/folder to .zip and download (this is the only way to download entire folders)
  -h, --help  show this help message and exit

fs ~ check size of file
usage: fs filename
example: fs tps_reports.txt
note: does not work on folders
optional arguments:
  -h, --help  show this help message and exit

use ~ use text editor of your choice to edit and save files inside your dropbox. text editor supplied must already be installed
usage: use text_editor filename1
example: use nano tps_reports.txt
example 2: use emacs tps_reports.txt
example 3: use vim tps_reports.txt
optional arguments:
  -h, --help  show this help message and exit

time ~ print the current time and date
usage: time
example: time
optional arguments:
  -h, --help  show this help message and exit
  
! ~ open raspberry cloud shell
usage: !
example: !
optional arguments:
  -h, --help  show this help message and exit
note: This will open the shell only, to exit the shell type '!q'
      This shell is identical to the bash shell except you cannot
      change directories.
special functionality: while inside the shell you can enter 'bash' for a full blown bash shell which can be exited by pressing CTRL+D

view ~ view img as thumbnail
usage: view imagename preview_size
example: view glamour_shot_by_deb.jpg 
optional arguments:
  -h, --help  show this help message and exit
note: If no image size is entered, the preview will default 
      to medium size (128x128). Also, image sizes are displayed 
      approximately as follows:
          "xs" (32x32) 
          "s" (64x64) 
          "m" (128x128)
          "l" (640x480) 
          "xl" (1024x768)

clear ~ clear the screen
usage: clear
example: clear
optional arguments:
  -h, --help  show this help message and exit
  
home ~ return to the home screen of Raspberry Cloud
usage: home
example: home
optional arguments:
  -h, --help  show this help message and exit  
  
? ~ view the entire list of commands
useage: ?
example: ?
optional arguments:
  -h, --help  show this help message and exit
note: Can't be used from within the Raspberry Cloud shell or bash shell.

l ~ logout and quit raspberry cloud
usage: l
example: l
optional arguments:
  -h, --help  show this help message and exit
note: Can't be used from within the Raspberry Cloud shell or bash shell.    
```

Donate
======

Donate Bitcoin:
19Ve bRAu 8ZdT zf7A JnJv dCyh qSBZ qMon T

Donate Dogecoin:
DBGX4dwhD7SHhfcgzKjSZ2yJDhruAPgPUP

Donate via Paypal:
http://bit.ly/1klxN1M
