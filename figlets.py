import sys
import random

from pyfiglet import Figlet
figlet = Figlet()
figlet.getFonts()
if len(sys.argv) == 1 or len(sys.argv) == 3:
    #randombfont
    if len(sys.argv) == 1:
        string = input('Input: ')
        figlet.setFont(font=random.choice(figlet.getFonts()))
        print(figlet.renderText(string))

    #specified font
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-f' or sys.argv[1] == '--font':
            try:
                figlet.setFont(font = sys.argv[2])
                string = input('Input: ')
                print(figlet.renderText(string))
            except:
                sys.exit('Invalid usage')
        else:
            sys.exit('Invalid usage')
else:
    sys.exit('Invalid usage')
