import argparse
import re
import os

parser = argparse.ArgumentParser(description='Converts USB rubber ducky scripts to a Nethunter format', epilog="Quack Quack")
#parser.add_argument('-l', type=str, dest='layout', choices=['us', 'fr', 'de', 'es','sv', 'it', 'uk', 'ru','dk','no','pt','be'], help='Keyboard layout')
parser.add_argument('duckyscript', help='Ducky script to convert')
parser.add_argument('hunterscript', help='Output script')


args = parser.parse_args()

infile = open(args.duckyscript)
dest = open(args.hunterscript, 'w')
tmpfile = open("tmp.txt", "w")

def duckyRules(source):

	tmpfile = source

	for (k,v) in rules.items():
		regex = re.compile(k)
		tmpfile  = regex.sub(v, tmpfile)

	return tmpfile

rules = { 
    r'ALT' : u'left-alt',
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
    r'PRINTSCREEN' : 'print',
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

prefix = "echo -ne '"
suffix = "' | /system/xbin/hid-keyboard /dev/hidg0 keyboard"

with infile as text:
		new_text = duckyRules(text.read())
		infile.close()

# Write regex to tmp file
with tmpfile as result:
    result.write(new_text)
    tmpfile.close()

src = open("tmp.txt", "r")
for line in src.read().split("\n"):
    command = line.upper().split(" ")[0]
    argument = " ".join(line.split(" ")[1:])

    if command == "DELAY" or command == "SLEEP":
        sleep_amount = int(argument) / 1000
        dest.write(f"sleep {sleep_amount}")
    
    elif command == "REM" or command == "PRINT":
        dest.write(f'echo "{argument}"')

    elif command == "STRING":
        dest.write(prefix+str(argument)+suffix)
    
    else:
        dest.write('%s%s%s\n' % (prefix, line.rstrip('\n').strip(), suffix))

    dest.write("\n")

src.close()
dest.close()
os.remove("tmp.txt")
print("File saved to location: " + (args.hunterscript))