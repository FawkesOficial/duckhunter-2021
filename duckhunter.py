import argparse
import re
import os

parser = argparse.ArgumentParser(description='Converts USB rubber ducky scripts to a Nethunter format', epilog="Made by @FawkesOficial and original code by @byt3bl33d3r\nGithub repo: https://github.com/FawkesOficial/duckhunter-2021", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-l', type=str, dest='layout', choices=['us', 'uk', 'pt'], help='Keyboard layout')
parser.add_argument('duckyscript', help='Ducky script to convert')
parser.add_argument('hunterscript', help='Output script')


args = parser.parse_args()

infile = open(args.duckyscript)
dest = open(args.hunterscript, 'w')
tmpfile = open("tmp.txt", "w")

def crash(**extra_chars):
    print('[-] Error at line {}: "{}"; "{}" is not a valid character'.format(index, str(argument).replace("\n", ""), char))
    if extra_chars:
        print("[?] STRING's characters can only be [a-z], [A-Z], [0-9] or {}".format(extra_chars))
    else:
        print("[?] STRING's characters can only be [a-z], [A-Z] or [0-9] for layouts other than 'pt', 'us', 'uk'")
        print("[?] For support for additional characters, please visit the Github repo: https://github.com/FawkesOficial/duckhunter-2021")
    print("[X] Quitting...")
    src.close()
    dest.close()
    #os.remove(args.hunterscript)
    os.remove("tmp.txt")
    exit()

def duckyRules(source):

	tmpfile = source

	for (k,v) in rules.items():
		regex = re.compile(k)
		tmpfile  = regex.sub(v, tmpfile)

	return tmpfile

rules = {
    r'GUI' : 'left-meta',
    r'WINDOWS' : 'left-meta',
    r'COMMAND' : 'left-meta',
    r'ALT' : 'left-alt',
    r'CONTROL' : 'left-ctrl',
    r'CTRL' : 'left-ctrl',
    r'SHIFT' : 'left-shift',
    r'MENU' : 'left-shift f10',
    r'APP' : 'escape',
    r'ESCAPE' : 'escape',
    r'ESC' : 'esc',
    r'END' : 'end',
    r'SPACE' : 'space',
    r'TAB' : 'tab',
    r'ENTER' : 'enter',
    r'UPARROW' : 'up',
    r'UP' : 'up',
    r'DOWNARROW' : 'down',
    r'DOWN' : 'down',
    r'LEFTARROW' : 'left',
    r'LEFT' : 'left',
    r'RIGHTARROW' : 'right',
    r'RIGHT' : 'right',
    r'CAPSLOCK' : 'capslock',
    r'F1' : 'f1',
    r'F2' : 'f2',
    r'F3' : 'f3',
    r'F4' : 'f4',
    r'F5' : 'f5',
    r'F6' : 'f6',
    r'F7' : 'f7',
    r'F8' : 'f8',
    r'F9' : 'f9',
    r'F10' : 'f10',
    r'DELETE' : 'delete',
    r'INSERT' : 'insert',
    r'NUMLOCK' : 'numlock',
    r'PAGEUP' : 'pgup',
    r'PAGEDOWN' : 'pgdown',
    r'PRINTSCREEN' : 'print',
    r'BREAK' : 'pause',
    r'PAUSE' : 'pause',
    r'SCROLLLOCK' : 'scrolllock',
    r'MOUSE RIGHTCLICK' : '--b2',
    r'MOUSE LEFTCLICK' : '--b1',
    r'MOUSE leftCLICK' : '--b1', # Regex is lowering LEFT to left so we need to catch it.
    r'DELAY' : 'sleep',
    r'DEFAULT_DELAY' : '"sleep', # We need to add this in between each line if it's set. For debugging
    r'REPEAT' : '"'}

prefix = "echo '"
suffix = "' | /system/xbin/hid-keyboard /dev/hidg0 keyboard"

dest.write("#!/system/bin/sh\n\n")

with infile as text:
		new_text = duckyRules(text.read())
		infile.close()

# Write regex to tmp file
with tmpfile as result:
    result.write(new_text)
    tmpfile.close()

src = open("tmp.txt", "r")
index = 0
for line in src:
    index += 1
    command = line.upper().split(" ")[0]
    argument = " ".join(line.split(" ")[1:])

    if command == "DELAY" or command == "SLEEP":
        sleep_amount = int(argument) / 1000
        dest.write(f"sleep {sleep_amount}\n")
    
    elif command == "REM" or command == "PRINT":
        dest.write(f'echo "{argument}"\n')

    elif command == "STRING":
        for char in str(argument).replace("\n", ""):
            if char.isupper():
                dest.write(prefix+char.lower()+" --left-shift"+suffix+"\n")
            elif char.islower() or char.isnumeric():
                dest.write(prefix+char+suffix+"\n")
            elif char == " ":
                dest.write(prefix+"space"+suffix+"\n")
            
            elif args.layout == "pt":
                if char == r'!': dest.write(prefix+'1 --left-shift'+suffix+"\n")
                elif char == r'"': dest.write(prefix+'2 --left-shift'+suffix+"\n")
                elif char == r'#': dest.write(prefix+'3 --left-shift'+suffix+"\n")
                elif char == r'$': dest.write(prefix+'4 --left-shift'+suffix+"\n")
                elif char == r'%': dest.write(prefix+'5 --left-shift'+suffix+"\n")
                elif char == r'&': dest.write(prefix+'6 --left-shift'+suffix+"\n")
                elif char == r'/': dest.write(prefix+'7 --left-shift'+suffix+"\n")
                elif char == r'(': dest.write(prefix+'8 --left-shift'+suffix+"\n")
                elif char == r')': dest.write(prefix+'9 --left-shift'+suffix+"\n")
                elif char == r'=': dest.write(prefix+'0 --left-shift'+suffix+"\n")

                elif char == r'@': dest.write(prefix+'2 --right-alt'+suffix+"\n")
                elif char == r'£': dest.write(prefix+'3 --right-alt'+suffix+"\n")
                elif char == r'§': dest.write(prefix+'4 --right-alt'+suffix+"\n")
                elif char == r'{': dest.write(prefix+'7 --right-alt'+suffix+"\n")
                elif char == r'[': dest.write(prefix+'8 --right-alt'+suffix+"\n")
                elif char == r']': dest.write(prefix+'9 --right-alt'+suffix+"\n")
                elif char == r'}': dest.write(prefix+'0 --right-alt'+suffix+"\n")
                
                elif char == r'€': dest.write(prefix+'e --right-alt'+suffix+"\n")

                else:
                    crash(extra_chars=["!", '"', "#", "$", "%", "&", "/", "(", ")", "=", "@", "£", "§", "{", "}", "[", "]", "€"])

            elif args.layout == "us":
                if char == r'!': dest.write(prefix+'1 --left-shift'+suffix+"\n")
                elif char == r'@': dest.write(prefix+'2 --left-shift'+suffix+"\n")
                elif char == r'#': dest.write(prefix+'3 --left-shift'+suffix+"\n")
                elif char == r'$': dest.write(prefix+'4 --left-shift'+suffix+"\n")
                elif char == r'%': dest.write(prefix+'5 --left-shift'+suffix+"\n")
                elif char == r'^': dest.write(prefix+'6 --left-shift'+suffix+"\n")
                elif char == r'&': dest.write(prefix+'7 --left-shift'+suffix+"\n")
                elif char == r'*': dest.write(prefix+'8 --left-shift'+suffix+"\n")
                elif char == r'(': dest.write(prefix+'9 --left-shift'+suffix+"\n")
                elif char == r')': dest.write(prefix+'0 --left-shift'+suffix+"\n")

                else:
                    crash(extra_chars=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"])

            elif args.layout == "uk":
                if char == r'!': dest.write(prefix+'1 --left-shift'+suffix+"\n")
                elif char == r'"': dest.write(prefix+'2 --left-shift'+suffix+"\n")
                elif char == r'£': dest.write(prefix+'3 --left-shift'+suffix+"\n")
                elif char == r'$': dest.write(prefix+'4 --left-shift'+suffix+"\n")
                elif char == r'%': dest.write(prefix+'5 --left-shift'+suffix+"\n")
                elif char == r'^': dest.write(prefix+'6 --left-shift'+suffix+"\n")
                elif char == r'&': dest.write(prefix+'7 --left-shift'+suffix+"\n")
                elif char == r'*': dest.write(prefix+'8 --left-shift'+suffix+"\n")
                elif char == r'(': dest.write(prefix+'9 --left-shift'+suffix+"\n")
                elif char == r')': dest.write(prefix+'0 --left-shift'+suffix+"\n")

                elif char == r'€': dest.write(prefix+'4 --right-alt'+suffix+"\n")

                else:
                    crash(extra_chars=["!", '"', "£", "$", "%", "^", "&", "*", "(", ")", "€"])

            else:
                crash()
    
    else:
        dest.write('%s%s%s\n' % (prefix, line.rstrip('\n').strip(), suffix))

src.close()
dest.close()
os.remove("tmp.txt")
print("[+] File saved to location: " + (args.hunterscript))