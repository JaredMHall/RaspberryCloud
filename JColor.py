
# colors
HEADER = '\033[95m'
FAIL = '\033[91m'
FGBLUE2 = '\033[94m'
FGGREEN2 = '\033[92m'
FGORANGE = '\033[93m'
FGGRAY = '\033[30m'
FGRED = '\033[31m'
FGGREEN = '\033[32m'
FGYELLOW = '\033[33m'
FGBLUE = '\033[34m'
FGMAG = '\033[35m'
FGCYAN = '\033[36m'
FGWHITE = '\033[37m'
#   FGGRAY = '\033[61m'
BGBLACK = '\033[40m'
BGRED = '\033[41m'
BGGREEN = '\033[42m'
BGYELLOW = '\033[43m'
BGBLUE = '\033[44m'
BGMAG = '\033[45m'
BGCYAN = '\033[46m'
BGWHITE = '\033[47m'
    
# end color(s)
ENDC = '\033[0m'
    
# format settings
BOLDON = '\033[1m'
BOLDOFF = '\033[22m'
ITALON = '\033[3m'
ITALOFF = '\033[23m'
UNDLNON = '\033[4m'
UNDLNOFF = '\033[24m'
INVON = '\033[7m'
INVOFF = '\033[27m'
STRKTHRUON = '\033[9m'
STRKTHRUOFF = '\033[29m'

def success():
    pass
def failure():
    pass
   
def blue(input_string, bg_color='', option1='', option2='', option3=''):
    print option1 + option2 + option3 + bg_color + '\033[94m' + input_string + '\033[0m' + '\033[0m' + '\033[22m' + '\033[23m' + '\033[24m' + '\033[27m' + '\033[29m'
def green(input_string, bg_color='', option1='', option2='', option3=''):
    print option1 + option2 + option3 + bg_color + '\033[92m' + input_string + '\033[0m' + '\033[0m' + '\033[22m' + '\033[23m' + '\033[24m' + '\033[27m' + '\033[29m'               
def red(input_string, bg_color='', option1='', option2='', option3=''):
    print option1 + option2 + option3 + bg_color + '\033[41m' + input_string + '\033[0m' + '\033[0m' + '\033[22m' + '\033[23m' + '\033[24m' + '\033[27m' + '\033[29m'
def orange(input_string, bg_color='', option1='', option2='', option3=''):
    print option1 + option2 + option3 + bg_color + '\033[93m' + input_string + '\033[0m' + '\033[0m' + '\033[22m' + '\033[23m' + '\033[24m' + '\033[27m' + '\033[29m'        
def yellow(input_string, bg_color='', option1='', option2='', option3=''):
    print option1 + option2 + option3 + bg_color + '\033[43m' + input_string + '\033[0m' + '\033[0m' + '\033[22m' + '\033[23m' + '\033[24m' + '\033[27m' + '\033[29m'
def gray(input_string, bg_color='', option1='', option2='', option3=''):
    print option1 + option2 + option3 + bg_color + '\033[94m' + input_string + '\033[0m' + '\033[0m' + '\033[22m' + '\033[23m' + '\033[24m' + '\033[27m' + '\033[29m'
def white(input_string, bg_color='', option1='', option2='', option3=''):
    print option1 + option2 + option3 + bg_color + '\033[37m' + input_string + '\033[0m' + '\033[0m' + '\033[22m' + '\033[23m' + '\033[24m' + '\033[27m' + '\033[29m'                        
