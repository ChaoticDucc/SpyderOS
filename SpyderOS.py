#backend
##about
version = "1.1"
credits = '''Made with Python 3.7 in Spyder
Created by ChaoticDucc
Components by ArousedbyTurds'''
copyright = "Copyright (c) 2020 ChaoticDucc"
license = "This project uses the MIT License. Find out more on our GitHub at https://go.chaoticducc.com/oslicence."
##import
import random
import time
##variables#
pn=">>"
sn="> "
##lists
y = {'y','yes','yea','yep','g','go','affirmative'}
n = {'n','no','nope','nah'}
q = {'q','quit'}
#system
def sys():
    while True:
        x = input(">> ")
        if x in q:
            power(0)
            break
        elif x == "help":
            help()
        elif x == "about":
            about()
        elif x == "num":
            num()
        elif x == "time":
            times()
        else:
            error(2)
def power(t):
    if t == 0:
        while True:
            x = input("Quit OS? (y/n) ")
            if x in y or x in q:
                print("Stopping Processes")
                time.sleep(1)
                print("Clearing System Junk")
                time.sleep(1.5)
                print("Shutting Down")
                time.sleep(.5)
                print("Done")
                time.sleep(.5)
                break
            elif x in n:
                sys()
                break
            else:
                error(1)
    elif t == 1:
        print("Starting Up")
        time.sleep(.5)
        print("Loading System Files")
        time.sleep(1.5)
        print("Starting Core Processes")
        time.sleep(1)
        print("Done")
        time.sleep(0.25)
        print(" ")
        print("Welcome to SpyderOS")
        print("Version " + version)
        print(" ")
        print("For help type: help")
        time.sleep(0.5)
def about():
    n="about"
    while True:
        x = input(pn+n+sn)
        if x == "help":
            print("Coming Soon")
        elif x == "version":
            print(version)
        elif x == "credits":
            print(credits)
        elif x == "copyright":
            print(copyright)
        elif x == "license":
            print(license)
        elif x in q:
            break
            sys()
        else:
            error(2)
def help():
    print("Under Construction")
    n="help"
    while True:
        x = input(pn+n+sn)
        if x == "commands":
            c = input("Search Commands: ")
            print(c)
        elif x in q:
            break
            sys()
        else:
            error(2)
def error(t):
    e="Error "
    c=str(t)
    s=" > "
    if t==0:
        print(e+c+s+"Unkown")
    elif t==1:
        print(e+c+s+"Invalid Syntax")
    elif t==2:
        print(e+c+s+"Not Found")
#programs
def num():
    n="num"
    while True:
        x = input(pn+n+sn)
        if x == "help":
            print("Coming Soon")
        elif x == "math":
            print('''
Use + to add
Use - to subtract
Use * to multiply
Use / to divide
Use // to divide without decimals
Use % to find the remainder of a divsion (so 3%2=1)
Use ** to raise to a power(so 3**2=9)
Use s to reuse previous result
Use q to quit
        ''')
            while True:
                r = input()
                if r in q:
                    break
                else:
                    try:
                        s = eval(r)
                        print(s)
                    except:
                        error(1)
        elif x == "rand": 
            n1 = input("Minimum Number: ")
            r1 = int(n1)
            n2 = input("Maximum Number: ")
            r2 = int(n2)
            r = random.randint(r1,r2)
            print(r)
        elif x in q:
            break
            sys()
        else:
            error(2)
def times():
    n="time"
    while True:
        x = input(pn+n+sn)
        if x == "help":
            print("Time Help")
            print("Coming Soon")
        elif x == "timer":
            print('''
m = minutes
s = seconds
q = quit
            ''')
            t=input()
            if t in q:
                times()
            elif t == "s":
                sec = int(input("Seconds: "))
                while True:
                    if sec <= 0:
                        print(sec)
                        print("Done")
                        break
                    else:
                        print(sec)
                        sec -= 1
                        time.sleep(1)
            elif t == "m":
                min = int(input("Minutes: "))
                min *= 60
                while True:
                    if min <= 1:
                        print(min)
                        print("Done")
                        break
                    else:
                        print(min)
                        min -= 1
                        time.sleep(1)
            else:
                error(1)
        elif x in q:
            break
            sys()
        else:
            error(2)
power(1)
sys()