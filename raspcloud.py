from __future__ import division
import curses
import uth
# Include the Dropbox SDK
import dropbox
import webbrowser
import os
import ConfigParser
# import JaredColors
import JColor
from subprocess import call
import sys
import time
from os.path import expanduser

# the raspberry cloud graphic was created by me, and I reserve all rights 
# if you would like to use it, please contact me first and give me credit as well.
#
# Author: Jared Marshall Hall
# Website: http://www.jaredmhall.com
# Contact: hall.jared.m@gmail.com
# Created: May 23, 2014
# Updated: July 10, 2014
# Why: I saw the need for Dropbox after getting my first Raspberry Pi
#      and couldn't find an app for it. So I decided after taking a look
#      at the Dropbox API to make one myself. I'm sorry for the horrible,
#      unoptimized spaghetti code. It's quite possible that by reviewing this 
#      source code, you may in fact learn a great deal about how NOT to program.
#      I strung it together over the period of a about a week, with the commuinity at 
#      heart. I really hope that this is useful for some of you. That will 
#      make it worth it. If this app was helpful please consider donating to help 
#      me pay my bills, I'm a poor college student. You can find the donation info
#      on the homescreen of the app but here it is again. 
#     
#     Donate Bitcoin:
#     1AYk yF8P 1k19 NpAA xxEm WBa6 rp7g wgHz dr
#
#     Donate Dogecoin:
#     DBGX4dwhD7SHhfcgzKjSZ2yJDhruAPgPUP
#
#     Donate via Paypal:
#     http://bit.ly/1klxN1M
#
#     However, what I'd really love more than a donation is a job! I'm fresh out of college 
#     and haven't had much luck finding one. I know it's a long shot, but if you are interested 
#     in hiring me, full-time part-time or on a freelance basis, please email me 
#     at hall.jared.m@gmail.com and let me know! My resume is available on my website at
#     http://www.jaredmhall.com. I'm also the proud creator of http://www.doge4.us as well 
#     as the android app over at http://goo.gl/JpeJFV. So if you're into that sort of thing, 
#     give 'em a look sometime! Stay stoked my friends!
#   
#

# to keep things looking fresh
def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# initiate the curses library for the homescreen
def init_curses():
    s = curses.initscr()
    curses.start_color()
    curses.use_default_colors()
    curses.noecho()
    s.scrollok(1)
    curses.curs_set(0)
    s.keypad(1)
    s.refresh()
    return s

def donate(s):
    curses.endwin()
    clearscreen()
    print JColor.FGYELLOW + JColor.BOLDON + "Donate Bitcoin" + JColor.ENDC + JColor.BOLDOFF
    print "19Ve bRAu 8ZdT zf7A JnJv dCyh qSBZ qMon T\n"
    print JColor.FGYELLOW + JColor.BOLDON + "Donate Dogecoin" + JColor.ENDC + JColor.BOLDOFF
    print "DBGX4dwhD7SHhfcgzKjSZ2yJDhruAPgPUP\n"
    print JColor.FGYELLOW + JColor.BOLDON + "Donate via Paypal" + JColor.ENDC + JColor.BOLDOFF
    print "http://bit.ly/1klxN1M\n"
    print JColor.FGGREEN + JColor.BOLDON + """  
However, what I'd really love more than a donation is a job! I'm fresh out 
of college and haven't had much luck finding one. I know it's a long shot, 
but if you are interested in hiring me, full-time, part-time or on 
a freelance basis, please email me at hall.jared.m@gmail.com and let 
me know! My resume is available on my website at 
http://www.jaredmhall.com. I'm also the proud creator of 
http://www.doge4.us as well as the android app over at 
http://goo.gl/JpeJFV. So if you're into that sort of thing, 
give 'em a look sometime! Thank you for your time and stay stoked!\n""" + JColor.ENDC + JColor.BOLDOFF 
    print raw_input("Press [ENTER] to continue..")
    start_raspberry_cloud(s)
    
def contact(s):
    curses.endwin()
    clearscreen()
    print JColor.FGYELLOW + JColor.BOLDON + "Email" + JColor.ENDC + JColor.BOLDOFF
    print "hall.jared.m@gmail.com\n"
    print raw_input("Press [ENTER] to continue..")
    start_raspberry_cloud(s)
    
def help(s):
    curses.endwin()
    clearscreen()
    print JColor.FGWHITE + JColor.BOLDON + """    
 ____  ____  ____  ____ 
||h ||||e ||||l ||||p ||
||__||||__||||__||||__||
|/__\||/__\||/__\||/__\|
     
""" + JColor.ENDC + JColor.BOLDOFF + """                                       
There are several dependencies for this program, they are: wget & dropbox
To install, enter these into the command line:
    sudo apt-get install wget
    sudo pip install dropbox
"""
    print JColor.FGWHITE + JColor.BOLDON + """
 ____  ____  ____  ____  ____ 
||o ||||t ||||h ||||e ||||r ||
||__||||__||||__||||__||||__||
|/__\||/__\||/__\||/__\||/__\|

"""  + JColor.ENDC + JColor.BOLDOFF + """
Other stuff:
- Raspberry Cloud does not like spaces!

command short list    
"""     
    print JColor.FGWHITE + JColor.BOLDON + """
 ____  ____  ____  ____  ____  ____  ____ 
||c ||||o ||||m ||||a ||||n ||||d ||||s ||
||__||||__||||__||||__||||__||||__||||__||
|/__\||/__\||/__\||/__\||/__\||/__\||/__\|

""" + JColor.ENDC + """mkdir ~ create a new folder
usage: mkdir absolue_path_to_folder
example: mkdir /Pictures/Family
optional arguments:
  -h, --help  show this help message and exit

rm ~ delete a file/folder
usage: rm absolute_path_to_file_1 absolute_path_to_file_2 absolute_path_to_file_2 etc.
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
"""  
    print raw_input("Press [ENTER] to continue..") 
    start_raspberry_cloud(s)
    
# this awesome explosion graphic was pulled from the 'boxes' terminal app created Thomas Jensen 
# the graphic itself was created by Joan G. Stark <spunk1111@juno.com>
# -- I only modified it a bit and added color.
def error_img(error_string):
    print JColor.FGORANGE + JColor.BOLDON + """
       _ ._  _ , _ ._
     (_ ' ( `  )_  .__)
   ( (  (    )   `)  ) _)
  (__ (_   (_ . _) _) ,__) """ + JColor.ENDC + JColor.BOLDOFF + JColor.FGORANGE + """
      `~~`\ ' . /`~~` """ + JColor.ENDC + JColor.FGWHITE + JColor.BOLDON + """
      ,::: ;   ; :::,
     ':::::::::::::::' """ + JColor.ENDC + JColor.BOLDOFF + JColor.FGORANGE + """
          /_ __ \    """ + JColor.ENDC + JColor.FGRED + """ 
Error: """ + error_string + JColor.ENDC

# didn't use this because i wanted to separate the colors
#     the those are clouds in the background btw ;)
def splash_screen(s, y, x):
 #   splash_logo = """
  #              ----.   .----
   #             '. \ '_' / .'
    #             .- (   ) -.
     #           ( .-.'-'.-. )
      #         - (   ) (   ) -  ,,,
#    ,,,,,,,,  (  )'-'.-.'-'(  )    ),,
#  ,(        ), - .- (   ) -. -      ,,)
# (,,            (  ) '-' (  ) ,,,, ),,
#     (,,,,       '- (   ) -'          ),
 #        (,,,,,,,)   '-'            ,,,,)        RASPBERRY CLOUD
  #        ,,(    ______________ ,,,,),,                    V 1.0
 #  ,,,,,,(,,____/_____________/____   ,)  BY JARED MARSHALL HALL
 # (        /   /|            |/   /,,),,,,,
 #(,,,     /___/_|____________/___/      ,,,)
 #    (,, ,,, /______________/|        ,,)
  #      (,, ,,|             ||,,,,, ,,)
   #   ,,,,,(  |             ||     )
   #  (,,,     |_____________|/    ,,)
    #     (,,            ,,,,,,,,,)
     #       (,,,,,,,,,,)
#"""
     
    # use curses library to print out the logo with colors
    s.addstr(1, 26, "----.   .----", curses.color_pair(1))
    s.addstr(2, 26, "'. \ '_' / .'", curses.color_pair(1))
    s.addstr(3, 27, ".- (   ) -.", curses.color_pair(2))
    s.addstr(4, 26, "( .-.'-'.-. )", curses.color_pair(2))
    s.addstr(4, 25, "- (   ) (   ) -", curses.color_pair(2))
    s.addstr(4, 42, ",,,", curses.color_pair(3))
    s.addstr(5, 14, ",,,,,,,,", curses.color_pair(3))
    s.addstr(5, 24, "(  )'-'.-.'-'(  )", curses.color_pair(2))
    s.addstr(5, 45, "),,", curses.color_pair(3))
    s.addstr(6, 12, ",(        ),", curses.color_pair(3))
    s.addstr(6, 25, "- .- (   ) -. -", curses.color_pair(2))
    s.addstr(6, 46, ",,)", curses.color_pair(3))
    s.addstr(7, 11, "(,,", curses.color_pair(3))
    s.addstr(7, 26, "(  ) '-' (  )", curses.color_pair(2))
    s.addstr(7, 41, ",,,, ),,", curses.color_pair(3))
    s.addstr(8, 15, "(,,,,", curses.color_pair(3))
    s.addstr(8, 27, "'- (   ) -'", curses.color_pair(2))
    s.addstr(8, 49, "),", curses.color_pair(3))
    s.addstr(9, 19, "(,,,,,,,)", curses.color_pair(3))
    s.addstr(9, 31, "'-'", curses.color_pair(2))
    s.addstr(9, 47, ",,,,)", curses.color_pair(3))
    s.addstr(4, 60, "RASPBERRY CLOUD", curses.color_pair(4))
    s.addstr(10, 20, ",,(", curses.color_pair(3))
    s.addstr(10, 27, "______________", curses.color_pair(5))
    s.addstr(10, 42, ",,,,),,", curses.color_pair(3))
    s.addstr(5, 70, "V 1.0", curses.color_pair(4))
    s.addstr(11, 13, ",,,,,,(,,", curses.color_pair(3))
    s.addstr(11, 22, "____/_____________/____", curses.color_pair(5))
    s.addstr(11, 48, ",)", curses.color_pair(3))
    s.addstr(6, 53, "BY JARED MARSHALL HALL", curses.color_pair(4))
    s.addstr(12, 12, "(", curses.color_pair(3))
    s.addstr(12, 21, "/   /|            |/   /", curses.color_pair(5))
    s.addstr(12, 45, ",,),,,,,", curses.color_pair(3))
    s.addstr(7, 67, "(c) 2014", curses.color_pair(4))
    s.addstr(13, 11, "(,,,", curses.color_pair(3))
    s.addstr(13, 20, "/___/_|____________/___/", curses.color_pair(5))
    s.addstr(13, 50, ",,,)", curses.color_pair(3))
    s.addstr(14, 15, "(,, ,,,", curses.color_pair(3))
    s.addstr(14, 23, "/______________/|", curses.color_pair(5))
    s.addstr(14, 50, ",,)", curses.color_pair(3))
    s.addstr(15, 15, "(,, ,,", curses.color_pair(3))
    s.addstr(15, 24, "|             ||", curses.color_pair(5))
    s.addstr(15, 40, " ,,,,, ,,)", curses.color_pair(3))
    s.addstr(16, 16, ",,,,,(", curses.color_pair(3))
    s.addstr(16, 24, "|             ||", curses.color_pair(5))
    s.addstr(16, 45, ")", curses.color_pair(3))
    s.addstr(17, 15, "(,,,", curses.color_pair(3))
    s.addstr(17, 24, "|_____________|/", curses.color_pair(5))
    s.addstr(17, 44, ",,)", curses.color_pair(3))
    s.addstr(18, 19, "(,,", curses.color_pair(3))
    s.addstr(18, 34, ",,,,,,,,,)", curses.color_pair(3))
    s.addstr(19, 22, "(,,,,,,,,,,)", curses.color_pair(3))

    s.addstr(17, 51, "> ", curses.color_pair(3))
    s.addstr(17, 53, "Start Raspberry Cloud", curses.color_pair(6))
    s.addstr(18, 53, "Donate", curses.color_pair(3))
    s.addstr(19, 53, "Contact", curses.color_pair(3))
    s.addstr(20, 53, "Help", curses.color_pair(3))
    s.addstr(21, 53, "Quit", curses.color_pair(3))

    # this is to keep track of where we are in the menu
    menu_pointer = 17

    # create the loop for the menu
    while(1): # AKA while True
        
        # store selection in a variable
        c = s.getch()

        
        if c == curses.KEY_DOWN:
            if menu_pointer >=21:
                s.addstr(menu_pointer, 51, " ", curses.color_pair(3))
                menu_pointer = 16
            #   for item in menu_list:
            menu_pointer += 1
            s.addstr(menu_pointer - 1, 51, " ", curses.color_pair(3))
            s.addstr(menu_pointer, 51, ">", curses.color_pair(3))
            #s.addstr(18, 51, "Donate", curses.color_pair(3))
            #s.addstr(19, 53, "Contact", curses.color_pair(3))
            #s.addstr(20, 53, "Help", curses.color_pair(3))
            s.refresh()
        elif c == curses.KEY_UP:
            if menu_pointer <=17:
                s.addstr(menu_pointer, 51, " ", curses.color_pair(3))
                menu_pointer = 22
            #   for item in menu_list:
            menu_pointer -= 1
            s.addstr(menu_pointer + 1, 51, " ", curses.color_pair(3))
            s.addstr(menu_pointer, 51, ">", curses.color_pair(3))
            #s.addstr(18, 51, "Donate", curses.color_pair(3))
            #s.addstr(19, 53, "Contact", curses.color_pair(3))
            #s.addstr(20, 53, "Help", curses.color_pair(3))
            s.refresh()
        elif c == ord('q'):
            break  # Exit the while()
        if menu_pointer == 17:
            s.addstr(17, 53, "Start Raspberry Cloud", curses.color_pair(6))
            s.addstr(18, 53, "Donate", curses.color_pair(3))
            s.addstr(19, 53, "Contact", curses.color_pair(3))
            s.addstr(20, 53, "Help", curses.color_pair(3))
            s.addstr(21, 53, "Quit", curses.color_pair(3))
            s.refresh()
            # I chose the right arrow key because the enter key is unreliable
            if c == curses.KEY_RIGHT:
                start_raspberry_cloud(s)
        elif menu_pointer == 18:
            s.addstr(17, 53, "Start Raspberry Cloud", curses.color_pair(3))
            s.addstr(18, 53, "Donate", curses.color_pair(6))
            s.addstr(19, 53, "Contact", curses.color_pair(3))
            s.addstr(20, 53, "Help", curses.color_pair(3))
            s.addstr(21, 53, "Quit", curses.color_pair(3))
            s.refresh()
            if c == curses.KEY_RIGHT:
                donate(s)
        elif menu_pointer == 19:
            s.addstr(17, 53, "Start Raspberry Cloud", curses.color_pair(3))
            s.addstr(18, 53, "Donate", curses.color_pair(3))
            s.addstr(19, 53, "Contact", curses.color_pair(6))
            s.addstr(20, 53, "Help", curses.color_pair(3))
            s.addstr(21, 53, "Quit", curses.color_pair(3))
            s.refresh()
            if c == curses.KEY_RIGHT:
                contact(s)
        elif menu_pointer == 20:
            s.addstr(17, 53, "Start Raspberry Cloud", curses.color_pair(3))
            s.addstr(18, 53, "Donate", curses.color_pair(3))
            s.addstr(19, 53, "Contact", curses.color_pair(3))
            s.addstr(20, 53, "Help", curses.color_pair(6))
            s.addstr(21, 53, "Quit", curses.color_pair(3))
            s.refresh()
            if c == curses.KEY_RIGHT:
                help(s)
        elif menu_pointer == 21:
            s.addstr(17, 53, "Start Raspberry Cloud", curses.color_pair(3))
            s.addstr(18, 53, "Donate", curses.color_pair(3))
            s.addstr(19, 53, "Contact", curses.color_pair(3))
            s.addstr(20, 53, "Help", curses.color_pair(3))
            s.addstr(21, 53, "Quit", curses.color_pair(6))
            s.refresh()
            if c == curses.KEY_RIGHT:
                curses.endwin()
                clearscreen()
                sys.exit()

def format_date(and_time=None):
    months = ('Null','January','February','March','April','May','June','July','August','September','October','November','December')
    curr_day = time.strftime("%d")
    curr_month = time.strftime("%m").strip('0')
    curr_year = time.strftime("%G")
    counter = 0
    for month in months:
        # print month
        # print counter + 1
        # print (str(curr_month) + ' and ' + str(counter + 1))
        if str(curr_month) == str(counter - 1):
            # print "[+]\t match found ------------> " + months[counter + 1]
            curr_month = months[counter - 1]
        counter += 1
    formatted_date = curr_month + ' ' + curr_day + ', ' + curr_year
    formatted_time = time.strftime("%I:%M:%S %p") # Hour Minute Second and the %p is for AM PM ;)
    if and_time == True:
        formatted_datetime = str(formatted_time) + ' ~ ' + str(formatted_date)
        return formatted_datetime 
    else:
        return formatted_date
    
def format_time():
    formatted_time = time.strftime("%I:%M:%S %p") # Hour Minute Second and the %p is for AM PM ;)
    return formatted_time

# this text was created using the ascii text generator over at http://patorjk.com/software/taag/
def home_screen(nickname, logged_in=True):
    formatted_date = format_date()
    formatted_time = format_time()
    if logged_in == True:
        print JColor.FGRED + JColor.BOLDON + """________                          ______                                 
___  __ \______ _________________ ___  /_ _____ _____________________  __
__  /_/ /_  __ `/__  ___/___  __ \__  __ \_  _ \__  ___/__  ___/__  / / /
_  _, _/ / /_/ / _(__  ) __  /_/ /_  /_/ //  __/_  /    _  /    _  /_/ / 
/_/ |_|  \__,_/  /____/  _  .___/ /_.___/ \___/ /_/     /_/     _\__, /  
                         /_/                                    /____/   """ + JColor.ENDC + JColor.BOLDOFF + JColor.FGWHITE + JColor.BOLDON +"""
_______________               _________                                  
__  ____/___  /______ ____  ________  /                                  
_  /     __  / _  __ \_  / / /_  __  /                                   
/ /___   _  /  / /_/ // /_/ / / /_/ /                                    
\____/   /_/   \____/ \__,_/  \__,_/
""" + JColor.ENDC + JColor.BOLDOFF + """
Hello """ + JColor.FGCYAN + JColor.BOLDON + nickname + JColor.ENDC + JColor.BOLDOFF + """! Welcome to Raspberry Cloud.
You are logged in.
The date is """+ JColor.FGWHITE + formatted_date + JColor.ENDC +""" and the current time is """+ JColor.FGWHITE+formatted_time+JColor.ENDC+"""     
You can enter """+ JColor.FGORANGE + JColor.BOLDON +"""ls"""+ JColor.ENDC + JColor.BOLDOFF +""" to print your home directory or """+ JColor.FGORANGE + JColor.BOLDON +"""?"""+ JColor.ENDC + JColor.BOLDOFF +""" for more help."""        
    else:
                print JColor.FGRED + JColor.BOLDON + """________                          ______                                 
___  __ \______ _________________ ___  /_ _____ _____________________  __
__  /_/ /_  __ `/__  ___/___  __ \__  __ \_  _ \__  ___/__  ___/__  / / /
_  _, _/ / /_/ / _(__  ) __  /_/ /_  /_/ //  __/_  /    _  /    _  /_/ / 
/_/ |_|  \__,_/  /____/  _  .___/ /_.___/ \___/ /_/     /_/     _\__, /  
                         /_/                                    /____/   """ + JColor.ENDC + JColor.BOLDOFF + JColor.FGWHITE + JColor.BOLDON +"""
_______________               _________                                  
__  ____/___  /______ ____  ________  /                                  
_  /     __  / _  __ \_  / / /_  __  /                                   
/ /___   _  /  / /_/ // /_/ / / /_/ /                                    
\____/   /_/   \____/ \__,_/  \__,_/
""" + JColor.ENDC + JColor.BOLDOFF + """
Hello """ + JColor.FGCYAN + JColor.BOLDON + nickname + JColor.ENDC + JColor.BOLDOFF + """! Welcome to Raspberry Cloud.
You are not logged in.
The date is """+ JColor.FGWHITE + formatted_date + JColor.ENDC +""" and the current time is """+ JColor.FGWHITE+formatted_time+JColor.ENDC #+"""     
# You can enter """+ JColor.FGORANGE + JColor.BOLDON +"""ls"""+ JColor.ENDC + JColor.BOLDOFF +""" to print your home directory or """+ JColor.FGORANGE + JColor.BOLDON +"""?"""+ JColor.ENDC + JColor.BOLDOFF +""" for more help."""                    
            

# put our app to work!
def start_raspberry_cloud(s):
    # i decided to end the curses window here
    #     i realize how nice it would be to be able
    #     to navigate with the arrow keys like the main menu
    #     but things get a little crazy when the size of your
    #     directory goes beyond the height of the terminal
    #     so i decided to keep things simple
    curses.endwin()

    # create a function to access our dropbox accound
    def access_dropbox(access_token, user_id):

        clearscreen()

        # get info about our dropbox
        client = dropbox.client.DropboxClient(access_token)


        # the first thing we need to do is print the directory so 
        #     we can get our bearings
        def print_dir(access_token, user_id, foldername):

 
            # stick folder info in a variable
            folder_metadata = client.metadata(foldername)

            # store folders in a dict
            folder_metadata_dict = folder_metadata

            formatted_date = format_date()
            formatted_time = format_time()

            # i hate these kinds of things, i really do
            #     this was such a pain for me to figure out
            # in case you are wondering, i'm looping through the folder dict
            #     and pulling out the names so they can be displayed
            for key, value in folder_metadata_dict.iteritems():                
                if type(value) is list:
                    for listitem in value:
                        if type(listitem) is dict:
                            #print listitem
                            for nested_key, nested_value in listitem.iteritems():
                                if nested_key == 'path':
                                    print JColor.FGORANGE + nested_value + JColor.ENDC
            print JColor.FGWHITE + "--------------------------------------------------" + formatted_time + ' ~ ' + formatted_date + JColor.ENDC

        settings = ConfigParser.ConfigParser()
        f = open("config.ini","r")
        settings.readfp(f)
        nickname = settings.get('NickName', 'nick_name')
        f.close()
        
        home_screen(nickname)
        # finally we print our root directory
        #print_dir(access_token, user_id, '/')

        # this is how we will get our info from the user
        def get_command():
            handle_input = raw_input(JColor.BOLDON + JColor.FGCYAN + "\n>> " + JColor.ENDC + JColor.BOLDOFF)
            return handle_input

        # a nifty function to check file size. doesn't work on folders
        def check_filesize(current_dir, name_of_file, client):

            # list client folders
            folder_metadata = client.metadata(current_dir)

            # store folders in a dict
            folder_metadata_dict = folder_metadata
            for key, value in folder_metadata_dict.iteritems():
                #print value
                if type(value) is list:
                    for listitem in value:
                        if type(listitem) is dict:
                        #print listitem
                            for nested_key, nested_value in listitem.iteritems():
                               # print "looping through data"
                                if (nested_key == 'path'):
                                   # print "found path" + nested_value
                                    if (nested_value == (current_dir + "/" + name_of_file)) or (nested_value.lower() == current_dir + "/" + name_of_file.lower()):
                                        current_dir = nested_value
                                        if name_of_file in current_dir:
                                            current_dir = current_dir.replace(name_of_file, "")
                                        print current_dir + name_of_file + ": " + str(listitem['bytes']) + " bytes"
                                        file_size = listitem['bytes']
                                        return str(file_size) + " bytes"
                                    elif (nested_value == "/" + name_of_file) or (nested_value.lower() == "/" + name_of_file):
                                        current_dir = nested_value
                                        if name_of_file in current_dir:
                                            current_dir = current_dir.replace(name_of_file, "")
                                        current_dir = "/"
                                        print current_dir + name_of_file + ": " + str(listitem['bytes']) + " bytes"
                                        file_size = listitem['bytes']
                                        return str(file_size) + " bytes"
                                    
        # this didn't work :/ may fix it later                                    
        def convert_bytes(bytes):  
            bytes_d = bytes
            bytes = bytes_d             
            kilobytes_d = bytes / 1024
            kilobytes = kilobytes_d
            megabytes_d = bytes / 1048576
            megabytes = megabytes_d
            gigabytes_d = bytes / 1073741824
            gigabytes = gigabytes_d
            if gigabytes_d is not None:
                return gigabytes
            elif megabytes_d is not None:
                return megabytes
            elif kilobytes_d is not None:
                return kilobytes
            elif bytes_d is not None:
                return bytes
            
        # for uploading files
        def new_upload(current_dir, path_to_file, upload_file_name, client):
            new_file_name = current_dir + "/" + upload_file_name
            local_file_size = os.stat(path_to_file).st_size            

            # if file is bigger than or equal to 4MB 
            #     use the chunked uploader (apparently 
            #     better for bigger files)
            # else 
            #     use the regular put_file() function
            if (local_file_size >= 4194304):
                print "uploading " + path_to_file + " to " + current_dir
                big_file = open(path_to_file, 'rb')
                uploader = client.get_chunked_uploader(big_file, local_file_size)
                while uploader.offset < local_file_size:
                    try:
                        upload = uploader.upload_chunked()
                    except rest.ErrorResponse, e:
                        # perform error handling and retry logic
                        print e
                        raise
                uploader.finish(current_dir + "/" + upload_file_name, True)
                clearscreen()
                print_dir(access_token, user_id, current_dir)
                print "[+]\tsuccessfully uploaded " + upload_file_name 
                #upload_file_size = check_filesize(current_dir, upload_file_name, client)
              #  print "uploaded " + convert_bytes(upload_file_size) + " of " + convert_bytes(local_file_size)
               # print "[+]\tsuccessfully uploaded " + upload_file_name + " to " + current_dir
            else:
                try:
                    f = open(path_to_file, 'rb')
                    target = client.put_file(current_dir + "/" + upload_file_name, f, True) 
                    upload_file_size = check_filesize(current_dir, upload_file_name, client)  
                except res.ErrorResponse, e:
                    print e
                    raise                
                # print "uploaded " + convert_bytes(upload_file_size) + " of " + convert_bytes(local_file_size) 
                clearscreen()
                print_dir(access_token, user_id, current_dir)  
                print "[+]\tsuccessfully uploaded " + upload_file_name                     

        # function to copy files
        def copy_file(client, old_file, new_file, current_dir):
            client.file_copy(current_dir + "/" + old_file, new_file)

        # function to backup files when they are being edited
        def backup_file(client, current_dir, file_to_edit):
            client.file_copy(current_dir + "/" + file_to_edit, current_dir + "/" + file_to_edit + ".backup")
           
        # download files to the ~/Downloads/RaspberryCloud folder by default (it will be created if it does not exist!)
        #     can be changed if you supply a different destination as an argument
        def download_file(current_dir, file_to_download, client, download_loc=(expanduser("~") + "/Downloads/RasberryCloud")):
            # check and see if the path exists
            if not os.path.exists(download_loc):
                # tell the system to create it
                os.makedirs(download_loc)             
            # create and open the file on the user's system that we will write to  
            out = open(download_loc + "/" + file_to_download, 'w+')
            # actually download the file
            with client.get_file(current_dir + "/" + file_to_download) as f:
                out.write(f.read())
            out.close()
            print JColor.BOLDON + JColor.FGYELLOW + "[+]\tsuccessfully downloaded " +  + JColor.ENDC + JColor.BOLDOFF + JColor.FGGREEN + file_to_download + JColor.ENDC

        # i think you can guess what this does ;)
        curr_time = time.strftime('%H:%M:%S')

        # create a current directory variable to store which directory we are currently in
        #     this will turn out to be very important for nearly all the other commands
        current_dir = "/"
        
        # start our main input loop
        while (1):
            # get the very first input, the program will loop back to this each
            #     time the a conditional finishes executing
            handle_input = get_command()
            if handle_input == '! -h' or handle_input == '! --help':
                print """
! ~ open raspberry cloud shell                
usage: !
example: !
optional arguments:
  -h, --help  show this help message and exit
note: this will open the shell only, to exit the shell type '!q'
          This shell is identical to the bash shell except you cannot
          change directories.
special functionality: while inside the shell you can enter 'bash' for a full blown bash shell which can be exited by pressing CTRL+D                
"""
            elif '!' in handle_input:
                                
                handle_input = handle_input.replace('!','')
                handle_input = handle_input.strip()
                os.system(handle_input)
                shell_mode = None
                print "\nWelcome to the bow shell! "
                print "Enter 'bash' to call a full-on system shell."
                print "From the bow shell enter '!q' to return to your Dropbox directory."
                print "From the bash shell press CTRL-D to return to the bow shell."
                while (1):
                # can enter shell instance with bash and exit back to the raspberry cloud with ctrl+d
                    shell_mode = raw_input(JColor.STRKTHRUON + JColor.BOLDON + JColor.FGYELLOW + "|" + JColor.ENDC + JColor.BOLDOFF + JColor.STRKTHRUOFF + JColor.STRKTHRUON + JColor.BOLDON + JColor.FGYELLOW + "} " + JColor.ENDC + JColor.BOLDOFF + JColor.STRKTHRUOFF) + " "
                    if shell_mode == "!q":   
                        break
                    elif "bash" in shell_mode:
                        print "\nenter CTRL + d to return to the Raspberry Cloud arrow shell"
                        os.system(shell_mode)
                    else:
                        os.system(shell_mode)
                #handle_input = handle_input.split()
                # list_to_string =  ' '.join(map(str, handle_input))
                #list_pointer = 0
                #string_builder = '"'
                #while list_pointer <= len(handle_input) - 1:                    
                #    string_builder = string_builder + handle_input[list_pointer] + '", "' 
                #    list_pointer += 1 
                #    print "looping"
                #    string_builder2 = string_builder + ' "'
                    
                #print 'new list'
                #print string_builder2
               # try:
                #    call([string_builder2])
                #except Exception as ex:
                 #   print ex
                  #  raise   
            # in case someone enters the command with no parameters, give them some help
            elif handle_input == 'mkdir' or handle_input == 'mkdir -h' or handle_input == 'mkdir --help':
                print """
mkdir ~ create a new folder
usage: mkdir absolue_path_to_folder
example: mkdir /Pictures/Family
optional arguments:
  -h, --help  show this help message and exit
"""                                
            elif ('mkdir' in handle_input) and ('-h' not in handle_input) and ('--help' not in handle_input):
                try:
                    handle_input = handle_input.replace("mkdir","")
                    handle_input = handle_input.strip('"')
                    handle_input = handle_input.strip("'")
                    handle_input = handle_input.strip(" ")
                    client.file_create_folder(handle_input.strip())                    
                    clearscreen()
                    print_dir(access_token, user_id, current_dir)
                    print "Folder " + handle_input + " created successfully."
                except Exception as ex:
                    error_img(str(ex))
                    # raise           
            # list or refresh the files in current directory
            elif handle_input == 'ls -h' or handle_input == 'ls --help':
                print """
ls ~ print a list of files in the current directory
usage: ls
example: ls
optional arguments:
  -h, --help  show this help message and exit                
"""                
            elif 'ls' in handle_input:
                clearscreen()
                try:
                    print_dir(access_token, user_id, current_dir)
                except Exception as ex:
                    error_img(str(ex))
                    # raise
            # go back to the root directory
            elif handle_input == 'cd':
                print_dir(access_token, user_id, "/")
                current_dir = "/"
            # change to another directory
            elif handle_input == 'cd -h' or handle_input == 'cd --help':
                print """
cd ~ change to another directory
usage: cd directory_path_to_change_to
example: cd /Pictures
note: using cd by itslef will bring you back to the root directory
optional arguments:
  -h, --help  show this help message and exit                
"""                                
            elif 'cd' in handle_input:
                try:
                    # scrub out what was entered in so we are left with only the argument to process
                    handle_input = handle_input.replace("cd","")
                    # strip away any whitespaces
                    handle_input = handle_input.strip()
                    clearscreen()
                    # if we are in the root directory set the new directory to the root "/" + what was just entered
                    # for example: cd work will change from the root or / to /work
                    if current_dir == "/":
                        current_dir = current_dir + handle_input                            
                    # otherwise tack the newly entered directory onto the previous one so that we can get into nested folders
                    else:                        
                        current_dir = current_dir + "/" + handle_input     

                    print_dir(access_token, user_id, current_dir)                      
                    #current_dir = handle_input
                    #current_dir = current_dir + "/" + handle_input
                    #get_command()
                except Exception as ex:
                    current_dir = "/"
                    # print_dir(access_token, user_id, "/")
                    error_img(str(ex))                    
                    # raise
            # this is probably my favorite part of the whole program! 
            # this function downloads the file to a temp folder, opens it in nano/emacs/vim
            #     and when your finished editing it will automatically upload it back into 
            #     the same folder and deletes the old file fromthe temp folder
            elif handle_input == 'use' or handle_input == 'use -h' or handle_input == 'use --help':
                print """
use ~ use text editor of your choice to edit and save files inside your dropbox. text editor supplied must already be installed
usage: use text_editor filename1
example: use nano tps_reports.txt
example 2: use emacs tps_reports.txt
example 3: use vim tps_reports.txt
optional arguments:
  -h, --help  show this help message and exit                
"""                
            elif 'use' in handle_input:
                temp_folder = "temp/"
                try:
                    handle_input = handle_input.replace("use","")
                    handle_input = handle_input.strip().split()
                    
                    file_path = temp_folder + handle_input[1]
                    out = open(file_path, 'wb')
                    file_open = True
                    with client.get_file(current_dir + "/" + handle_input[1]) as f:
                        out.write(f.read())
                    out.close()

                    # backup the file
                    backup_file(client, current_dir, handle_input[1])
                    # use a system call to access nano
                    call([handle_input[0], file_path])
                    clearscreen()
                    print "editing file..."
                    print JColor.FGGREEN + "[+]\tsuccessfully edited " + JColor.ENDC + JColor.FGBLUE + handle_input[1] + JColor.ENDC
                    sys.stdout.flush()
                    # reupload the file
                    print "uploading.." + current_dir
                    sys.stdout.flush()
                    f = open(file_path, 'rb')
                    response = client.put_file(current_dir + "/" + handle_input[1], f, True)
                    # delete the temp file
                    print "cleaning up..."
                    sys.stdout.flush()
                    os.remove(file_path)
                    client.file_delete(current_dir + "/" + handle_input[1] + ".backup")
                    clearscreen()
                    # other time formats
                    # curr_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
                    # curr_time = time.strftime("%H:%M:%S", time.gmtime())

                    print JColor.FGGREEN + "[+]\tsuccessfully uploaded " + JColor.ENDC + JColor.FGBLUE + handle_input[1] + JColor.ENDC + " to " + JColor.FGBLUE + current_dir + JColor.ENDC + " at " + JColor.FGWHITE + curr_time + JColor.ENDC
                    print_dir(access_token, user_id, current_dir)


                except Exception as ex:
                    error_img(str(ex))
                    # raise
            elif handle_input == 'cp' or handle_input == 'cp -h' or handle_input == 'cp --help':
                print """
cp ~ copy a file/folder from one location to another
usage: cp absolute_path_to_file_with_filename new_path_to_file_with_filename
example: cp /School/Essay.pdf /School/History/Essay.pdf
note: if a different filename is given for the second arguement, the file will be copied and renamed 
optional arguments:
  -h, --help  show this help message and exit                
"""                
            elif 'cp' in handle_input:
                handle_input = handle_input.replace("cp","")
                handle_input = handle_input.split()
                try:           
                    # print handle_input[0]
                    # print handle_input[1]
                    client.file_copy(handle_input[0], handle_input[1])
                    print JColor.FGBLUE + handle_input[0] + JColor.ENDC + " was successfully copied to " + JColor.FGBLUE + handle_input[1] + JColor.ENDC + " at " + JColor.FGWHITE + curr_time + JColor.ENDC
                except Exception as ex:
                    error_img(str(ex))
                    # print ex
            elif handle_input == 'mv' or handle_input == 'mv -h' or handle_input == 'mv --help':
                print """
mv ~ move a file/folder from one location to another
usage: mv absolute_path_to_file_with_filename new_path_to_file_with_filename
example: mv /Music/Playlist /Shared
note: if a different filename is given for the second arguement, the file will be moved and renamed 
special usage: just like in linux, you may use this command to rename a file also.
optional arguments:
  -h, --help  show this help message and exit                
"""                
            elif 'mv' in handle_input:
                handle_input = handle_input.replace("mv","").strip()
                handle_input = handle_input.split()
                formatted_time = format_time()
                try:
                    client.file_move(handle_input[0], handle_input[1])
                    print JColor.FGBLUE + handle_input[0] + JColor.ENDC + " was successfully moved to " + JColor.FGBLUE + handle_input[1] + JColor.ENDC + " at " + JColor.FGWHITE + formatted_time + JColor.ENDC
                except Exception as ex:
                    error_img(str(ex))
            elif handle_input == 'rm' or handle_input == 'rm -h' or handle_input == 'rm --help':
                print """
rm ~ delete a file/folder
usage: rm absolute_path_to_file_1 absolute_path_to_file_2 absolute_path_to_file_2 etc.
example: rm /Random/Other /tps_report.txt
optional arguments:
  -h, --help  show this help message and exit                
"""                
            elif 'rm' in handle_input:
                handle_input = handle_input.replace("rm","")
                handle_input = handle_input.split()
                list_pointer1 = 0          
                list_pointer2 = 0     
                list_to_string =  ' '.join(map(str, handle_input))
                delete_prompt = raw_input(JColor.FGRED + "WARNING: You are about to delete " + JColor.ENDC + JColor.FGBLUE + list_to_string + JColor.ENDC + JColor.FGRED + " forever! Proceed (Y/N)? " + JColor.ENDC)               
                if (delete_prompt == 'Y') or (delete_prompt == 'y'):
                    try:
                        while list_pointer2 <= len(handle_input) - 1:
                            client.file_delete(handle_input[list_pointer2]) 
                            list_pointer2 += 1                                       
                        clearscreen()
                        print_dir(access_token, user_id, current_dir)
                        if list_pointer2 > 1:
                            print JColor.FGBLUE + list_to_string + JColor.ENDC + " were successfully deleted at " + JColor.FGWHITE + curr_time + JColor.ENDC
                        else:
                            print JColor.FGBLUE + list_to_string + JColor.ENDC + " was successfully deleted at " + JColor.FGWHITE + curr_time + JColor.ENDC                    
                    except Exception as ex:
                        error_img(str(ex) + '\nPlease make sure you entered the complete path.\nFor help enter' + JColor.FGORANGE + JColor.BOLDON + ' rm -h ' + JColor.ENDC + JColor.BOLDOFF)
                        # raise                    
                elif (delete_prompt == 'N') or (delete_prompt == 'n'):
                    clearscreen()
                    print_dir(access_token, user_id, current_dir)
                else:
                    clearscreen()
                    print_dir(access_token, user_id, current_dir)
            elif handle_input == 'share' or handle_input == 'share -h' or handle_input == 'share --help':          
                print """
share ~ create a link to share a file/folder
usage: share absolute_path_to_file
example: share /Art/ConceptArt
optional arguments:
  -h, --help  show this help message and exit                
"""                
            elif 'share' in handle_input:
                handle_input = handle_input.replace("share","").strip()
                share_link = client.share(current_dir + "/" + handle_input, False)
                for a, b in share_link.iteritems():
                    if a == 'url':
                        print "share link: " + b
                    if a == 'expires':
                        print "expires " + b
            elif handle_input == 'upload' or handle_input == 'upload -h' or handle_input == 'upload --help':
                print """
upload ~ upload a file to the current directory
usage: upload path_to_local_file filename
example: /home/user/Documents/BeejCGuide.pdf BeejCguide.pdf
note: file can be drag and dropped from the local machine into the terminal window
optional arguments:
  -h, --help  show this help message and exit                
"""              
            elif 'upload' in handle_input:
                handle_input = handle_input.replace("upload","")
                handle_input = handle_input.replace("'","").strip()
                handle_input = handle_input.split()
                new_upload(current_dir, handle_input[0], handle_input[1], client)
                #upload_file(current_dir, handle_input[0], handle_input[1], client)
            elif handle_input == 'dl' or handle_input == 'dl -h' or handle_input == 'dl --help' or handle_input == 'dl -c':
                print """
dl ~ download files from current directory
usage: dl filename1 filename2 filename3 filename4 etc.
example: dl tps_reports.txt intro_to_c.pdf
optional arguments:
  -c, --compress  convert file/folder to .zip and download (this is the only way to download entire folders)
  -h, --help  show this help message and exit                
"""                
            elif ('dl' in handle_input) and ('-c' not in handle_input):
                handle_input = handle_input.replace("dl","")
                handle_input = handle_input.replace("'","")
                handle_input = handle_input.replace('"',"").strip()  
                handle_input = handle_input.split()
                list_pointer = 0
                while list_pointer <= len(handle_input) - 1:
                    try:
                        download_file(current_dir, handle_input[list_pointer], client) 
                    except Exception as ex:
                        error_img(str(ex))
                        # print "If it's a folder use the -f flag dl -f <folder1> <folder2> etc.!"
                        # raise
                    list_pointer += 1       
                    
            # TODO this still doesn't work
            # wget -r -l1 --directory-prefix=~/Downloads/RaspberryCloud --no-parent -A zip "https://www.dropbox.com/sh/pz5zqn72a5ct6om/AACLQJRZiNYMHGYpL6YDJKGqa?dl=1"                    
            # http://stackoverflow.com/questions/6533187/wget-removing-filename-since-it-should-be-rejected
                    
            # make an option for downloading folders 
            elif 'dl -c' in handle_input:
                # dl entire folder
                handle_input = handle_input.replace("dl -c","")
                handle_input = handle_input.replace("'","")
                handle_input = handle_input.replace('"',"")
                handle_input = handle_input.strip()  
                handle_input = handle_input.split(" ")
               # handle_input = map(str.strip, handle_input)
                list_to_string =  ' '.join(map(str, handle_input))
                list_pointer_dlf = 0
                while list_pointer_dlf <= len(handle_input) - 1:
                    try:
                        if current_dir == "/":
                            share_link = client.share(current_dir + handle_input[list_pointer_dlf], False)
                        else:
                            share_link = client.share(current_dir + "/" + handle_input[list_pointer_dlf], False)
                        for a, b in share_link.iteritems():
                            if a == 'url':
                                link_address = b 
                                            # check and see if the path exists
                                home = expanduser("~")
                                download_loc = home + '/Downloads/RaspberryCloud' + '/' 
                                if not os.path.exists(download_loc):
                                    # tell the system to create it
                                    os.makedirs(download_loc)  
                                # os.system('curl ' + link_address + '?dl=1 --create-dirs -o ' + home + '/Downloads/RaspberryCloud' + '/' + handle_input[0].strip("/") + ".zip")
                                os.system('wget -E -H -K --force-directories -O ' + home + '/Downloads/RaspberryCloud' + '/' + handle_input[list_pointer_dlf].strip("/") + ".zip " + link_address + "?dl=1")
                                sys.stdout.flush()
                                list_pointer_dlf += 1
                        # download_file(current_dir, handle_input[list_pointer], client) 
                        print JColor.FGGREEN2 + 'Successfully downloaded ' + JColor.ENDC + JColor.FGBLUE + list_to_string + JColor.ENDC + ' to ' + home + '/Downloads/RaspberryCloud'
#                        JaredColors.Successfully downloaded ' + JColor.ENDC + JColor.FGBLUE + list_to_string + JColor.ENDC + ' to ' + home + '/Downloads/RaspberryCloud'
                    except Exception as ex:
                        error_img(str(ex))
                        # raise
                        # raise
                    clearscreen()
                    print_dir(access_token, user_id, current_dir)
                    print '[+]\t' + JColor.FGGREEN2 + 'Successfully downloaded ' + JColor.ENDC + JColor.FGBLUE + list_to_string + JColor.ENDC + ' to ' + home + '/Downloads/RaspberryCloud'
                   # list_pointer_dlf += 1                 
                #share_link = client.share(current_dir + "/" + handle_input) 
            elif handle_input == 'view' or handle_input == 'view -h' or handle_input == 'view --help':
                print """
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
"""          
            elif 'view' in handle_input:
                handle_input = handle_input.replace('view','')
                handle_input = handle_input.replace('/', '')
                handle_input = handle_input.split()
                home = expanduser("~")
                download_loc = home + '/Downloads/RaspberryCloud' 
                if current_dir == '/':
                    use_dir = current_dir + handle_input[0]
                else:
                    use_dir = current_dir + '/' + handle_input[0]
                if len(handle_input) > 1:
                    try:
                        picture_type = 'JPEG'
                        file_to_download = client.thumbnail(use_dir, handle_input[1])    
                    except Exception as ex:
                        error_img(str(ex))                  
                else:
                    try:
                        picture_type = 'JPEG'
                        file_to_download = client.thumbnail(use_dir, 'm')    
                    except Exception as ex:
                        error_img(str(ex))     
                try:  
                    temp_path = "temp/" + 'thumbnail'
                    out = open(temp_path, 'w+')
                    f = file_to_download
                    out.write(f.read())
                    # TODO add colors
                    out.close()
                    # test to make sure the file isn't empty
                    if os.stat(temp_path).st_size == 0:
                    #    error_img('Cannot preview thumbnail.\nMake sure it is a picture file and not over 20MB.')
                        os.remove(temp_path)
                    else:
                        os.system('gpicview ' + temp_path)
                        os.remove(temp_path)
                except Exception as ex:
                    pass
                #    error_img(str(ex))
                    # raise
                #print "[+]\tsuccessfully downloaded " + file_to_download 
            elif handle_input == 'clear -h' or handle_input == 'clear --help':
                print """
clear ~ clear the screen
usage: clear
example: clear
optional arguments:
  -h, --help  show this help message and exit               
"""                
            elif 'clear' in handle_input:
                os.system('clear')    
            elif handle_input == 'fs' or handle_input == 'fs -h' or handle_input == 'fs --help':
                print """
fs ~ check size of file
usage: fs filename
example: fs tps_reports.txt
note: does not work on folders
optional arguments:
  -h, --help  show this help message and exit                
"""                     
            elif 'fs' in handle_input:
                handle_input = handle_input.replace("fs","")
                handle_input = handle_input.replace("'","")
                handle_input = handle_input.replace('"',"").strip()
                try:
                    check_filesize(current_dir, handle_input, client)
                except Exception as ex:
                    error_img(str(ex))
            elif handle_input == 'mlink' or handle_input == 'mlink -h' or handle_input == 'mlink --help':
                print """
mlink ~ create a media link to an image/video/sound file from your Dropbox
usage: mlink absolute_path_to_file
example: mlink /Videos/important_video.mov
optional arguments:
  -h, --help  show this help message and exit                
"""                
            elif 'mlink' in handle_input:
                handle_input = handle_input.replace("mlink", "").strip()  
                try:
                    media_link = client.media(current_dir + "/" + handle_input)
                    for a, b in media_link.iteritems():
                        if a == 'url':
                            print "share link: " + b
                        if a == 'expires':
                            print "expires " + b
                except Exception as ex:
                    error_img(str(ex))
            elif handle_input == 'home -h' or handle_input == 'home --help':
                print """
home ~ return to the home screen of Raspberry Cloud
usage: home
example: home
optional arguments:
  -h, --help  show this help message and exit                    
"""                                    
            elif handle_input == 'home':
                clearscreen()
                home_screen(nickname)
            elif handle_input == '?':
                # print the entire help screen
                print JColor.FGWHITE + JColor.BOLDON + """
 ____  ____  ____  ____  ____  ____  ____ 
||c ||||o ||||m ||||a ||||n ||||d ||||s ||
||__||||__||||__||||__||||__||||__||||__||
|/__\||/__\||/__\||/__\||/__\||/__\||/__\|

""" + JColor.ENDC + """mkdir ~ create a new folder
usage: mkdir absolue_path_to_folder
example: mkdir /Pictures/Family
optional arguments:
  -h, --help  show this help message and exit

rm ~ delete a file/folder
usage: rm absolute_path_to_file_1 absolute_path_to_file_2 absolute_path_to_file_2 etc.
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
"""
            elif handle_input == 'time -h' or handle_input == 'time --help':
                print """
time ~ print the current time and date
usage: time
example: time
optional arguments:
  -h, --help  show this help message and exit                
"""        
            elif handle_input == 'time':
                formatted_date = format_date(True)
                print formatted_date
                # print time.strftime("%d-%m-%Y, %H:%M:%S")
            elif handle_input == 'l -h' or handle_input == 'l --help':
                print """
l ~ logout and quit raspberry cloud
usage: l
example: l
optional arguments:
  -h, --help  show this help message and exit
note: Can't be used from within the Raspberry Cloud shell or bash shell.                                
"""                
            elif handle_input == 'l':
                # clearscreen()
                logout_prompt = raw_input("Are you sure you want to logout (Y/N)? ")
                if (logout_prompt == 'Y') or (logout_prompt == 'y'):
                    clearscreen()
                    sys.exit()
                elif (logout_prompt == 'N') or (logout_prompt == 'n'):
                    clearscreen()
                    print_dir(access_token, user_id, current_dir)
                else:
                    clearscreen()
                    print_dir(access_token, user_id, current_dir)
            else:
                print "Please enter a valid command.\nEnter " + JColor.FGORANGE + JColor.BOLDON + "?" + JColor.ENDC + JColor.BOLDOFF + " to view a list of commands."               

    # load in config file and check to see if this is the
    # first run of the program
    settings = ConfigParser.ConfigParser()
    f = open("config.ini","r")
    settings.readfp(f)
    first_run = settings.get('FirstRun', 'first_run')

    if (first_run == 'True'):

        clearscreen()

        # a = settings.get('AppKey', 'app_key').strip()
        # b = settings.get('AppSecret', 'app_secret').strip()

        appkey = raw_input(JColor.BOLDON + JColor.FGCYAN + "Please head over to https://www.dropbox.com/developers/apps \n and create a new App. \nMake it a Core app, give it any name that you like. \n Make sure it has full access to Dropbox. \n Once it has been created enter the App Key and App Secret below." + JColor.ENDC + JColor.BOLDOFF + JColor.BOLDON + JColor.FGYELLOW +" \n\nApp Key: " + JColor.ENDC + JColor.BOLDOFF).strip()
        appsecret = raw_input(JColor.BOLDON + JColor.FGYELLOW + "App Secret: " + JColor.ENDC + JColor.BOLDOFF).strip()
        #try:
        flow = dropbox.client.DropboxOAuth2FlowNoRedirect(appkey, appsecret)
        authorize_url = flow.start()
        #except Exception as ex:
      #      error_img(str(ex))
            
        # get user's nickname
        nickname = raw_input(JColor.BOLDON + JColor.FGCYAN + "What should I call you? " + JColor.ENDC + JColor.BOLDOFF).strip()
        
        clearscreen()
        # make sure its converted to a string
        nickname = str(nickname)
        # settings.set('AccessCode', 'access_code', access_token)

        home_screen(nickname, False)
        auto_or_manual = raw_input(JColor.FGYELLOW + JColor.BOLDON + "\n*Please head over to " + authorize_url + " \n(1) Entering \'g\' to open your web browser \n(2) Entering \'m\' to open it manually \nNOTE: Once there click 'Allow' and copy the code back into this window (you may be required to login first).\n" + JColor.ENDC + JColor.BOLDOFF + JColor.BOLDON + JColor.FGCYAN + "\n>> " + JColor.ENDC + JColor.BOLDOFF)
        # auto_or_manual = raw_input('Welcome to Raspberry Cloud!\nHead over to ' + authorize_url + ' to confirm your account either by:\n(1) Entering \'g\' to open your web browser \n(2) Entering \'m\' to open it manually \nNOTE: Once there click "Allow" and copy the code back into this window(you may be required to login first).\n>> ')

        if auto_or_manual == 'g':
            webbrowser.open(authorize_url)
        elif auto_or_manual == 'm':
            pass
        #print '1. Go to: ' + authorize_url
        #print '2. Click "Allow" (you might have to log in first)'
        #print '3. Copy the authorization code.'
        code = raw_input(JColor.BOLDON + JColor.FGCYAN + "Enter the authorization code here: " + JColor.ENDC + JColor.BOLDOFF).strip()

        try:
            # This will fail if the user enters an invalid authorization code
            access_token, user_id = flow.finish(code)
            # add access code to file and change first_run variable to false
            # so we won't have to repeat this process next time!
            settings.set('FirstRun', 'first_run', 'False')
            settings.set('AccessCode', 'access_code', access_token)
            settings.set('NickName', 'nick_name', nickname)
            f = open("config.ini","w")
            settings.write(f)
            f.close()

            access_dropbox(access_token, user_id)
        except Exception as ex:
            error_img(str(ex))
            # raise  

        clearscreen()
    elif first_run == 'False':
        #access_token = raw_input("enter token: ").strip()
        access_token = settings.get('AccessCode', 'access_code').strip()
        user_id = access_token.strip()

        #print access_token
        #user_id = settings.get('AccessCode', 'access_code').strip()
        access_dropbox(access_token, user_id)

# more curses stuff
# set colors 
# get width, heigth of the screen, etc.
def main():
    screen = init_curses()
    y, x = screen.getmaxyx()
    # create green
    curses.init_pair(1, curses.COLOR_GREEN, -1)
    # create red
    curses.init_pair(2, curses.COLOR_RED, -1) # -1 is default bcgd color
    # create white
    curses.init_pair(3, curses.COLOR_WHITE, -1)
    # create cyan
    curses.init_pair(4, curses.COLOR_CYAN, -1)
    # create yellow
    curses.init_pair(5, curses.COLOR_YELLOW, -1)
    # create black on white
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)    
    # print the splash screen out!
    splash_screen(screen, y, x)
    

# check and see if this program is being run by itself
# if so call the main function
if __name__ == '__main__':
    main()
