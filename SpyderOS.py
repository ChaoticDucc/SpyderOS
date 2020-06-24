#backend
##import
import random
import time
##about
version = "1.1.1"
credits = '''Made with Python 3.7 in Spyder
Created by ChaoticDucc
Components by ArousedbyTurds'''
copyright = "Copyright (c) 2020 ChaoticDucc"
license = "This project uses the MIT License. Find out more on our GitHub at https://go.chaoticducc.com/oslicence."
##variables
z="Coming Soon"
pn=">>"
sn="> "
q="q"
##data
items = []
##execution
def pow(t):
    if t == 0:
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
        sys()
    elif t == 1:
        print("Stopping Processes")
        time.sleep(1)
        print("Clearing System Junk")
        time.sleep(1.5)
        print("Shutting Down")
        time.sleep(.5)
        print("Done")
        time.sleep(.5)
    elif t == 2:
        time.sleep(1)
        s=input("Currently Sleeping. Press enter to resume")
        print("Resumming...")
        time.sleep(0.5)
        sys()
        print(s)
def err(t):
    e="Error "
    c=str(t)
    s=" > "
    if t==0:
        print(e+c+s+"Unkown")
    elif t==1:
        print(e+c+s+"Invalid Syntax")
    elif t==2:
        print(e+c+s+"Not Found")
    elif t==3:
        print(z)
    elif t==4:
        print(e+c+s+"User Input does not exist")
def help(t):
    if t=="sys":
        print("gethelp, about, power, num, time, list")
    elif t=="about":
        print("version, credits, copyright, licence")
    print("Works everywhere: help, q")
#system
def sys():
    n="sys"
    while True:
        x = input(">> ")
        try:
            if x == "help":
                help(n)
            elif x == "gethelp":
                gethelp()
                break
            elif x == "about":
                about()
                break
            elif x == "power" or x == q:
                power()
                break
            elif x == "num":
                num()
                break
            elif x == "time":
                times()
                break
            elif x == "list":
                list()
                break
            elif x == q:
                print(z)
            else:
                err(2)
        except:
            err(0)
def gethelp():
    print(z)
    sys()
def about():
    n="about"
    while True:
        x = input(pn+n+sn)
        if x == "help":
            help(n)
        elif x == "version":
            print(version)
        elif x == "credits":
            print(credits)
        elif x == "copyright":
            print(copyright)
        elif x == "license":
            print(license)
        elif x == q:
            sys()
            break
        else:
            err(2)
def power():
    n="power"
    while True:
        x = input(pn+n+sn)
        if x == "shutdown" or x == q:
            print("")
            pow(1)
            break
        elif x == "restart":
            print("")
            pow(1)
            time.sleep(2)
            print("")
            pow(0)
            break
        elif x == "sleep":
            pow(2)
            break
        elif x == q:
            sys()
            break
        else:
            err(2)
#programs
def num():
    n="num"
    while True:
        x = input(pn+n+sn)
        if x == "help":
            print(z)
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
Use q to quit''')
            while True:
                r = input()
                if r == q:
                    sys()
                    break
                else:
                    try:
                        s = eval(r)
                        print(s)
                    except:
                        err(1)
        elif x == "rand": 
            n1 = input("Minimum Number: ")
            r1 = int(n1)
            n2 = input("Maximum Number: ")
            r2 = int(n2)
            r = random.randint(r1,r2)
            print(r)
        elif x == q:
            break
            sys()
        else:
            err(2)
def times():
    n="time"
    while True:
        x = input(pn+n+sn)
        if x == "help":
            print(z)
        elif x == "timer":
            print('''
m = minutes
s = seconds
q = quit''')
            t=input()
            if t == q:
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
                err(1)
        elif x == q:
            sys()
            break
        else:
            err(2)
def list():
    n="list"
    while True:
        x = input(pn+n+sn)
        if x == "help":
            print(z)
        elif x == "view":
            print(items)
        elif x == "add":
            while True:
                i = input()
                if i == q:
                    break
                else:
                    items.append(i)
        elif x == "remove":
            while True:
                i = input()
                if i == q:
                    break
                elif i in items:
                    items.remove(i)
                else:
                    err(4)
        elif x == q:
            sys()
            break
        else:
            err(2)
pow(0)