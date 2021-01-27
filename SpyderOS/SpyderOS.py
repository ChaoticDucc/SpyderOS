#backend
##import
import random
import time
##about
version = "1.3"
credits = '''Made with Python 3.7 in Spyder
Created by ChaoticDucc
Components by ArousedbyTurds'''
copyright = "Copyright (c) 2020 ChaoticDucc"
license = "This project uses the MIT License. Find out more on our GitHub at https://go.chaoticducc.com/oslicence."
##sys-variables
z="Coming Soon"
uq="Use q to quit"
ue="Use ENTER to "
pn=">>"
sn="> "
##control-variables
q=["q", "quit"]
yes=["y", "yes"]
no=["n", "no"]
##data
items = []
##execute
def expow(t):
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
def exerr(t):
    e="Error "
    c=str(t)
    s=" > "
    if t==0:
        print(e,c,s,"Unkown")
    elif t==1:
        print(e,c,s,"Invalid Syntax")
    elif t==2:
        print(e,c,s,"Not Found")
    elif t==3:
        print(e,c,s,"Incorrect Response")
    elif t==4:
        print(e,c,s,"User Input does not exist")
def exhelp(t):
    if t=="sys":
        print('''
about: about SpyderOS
power: display power options
num: complete operatons with numbers
time: complete operations with time
list: view and edit a list of items''')
    elif t=="viewex":
        print('''
commands: search for commands associated with an app''')
    elif t=="about":
        print('''
version: show SpyderOS version
credits: show credits for SpyderOS
copyright: show SpyderOS's copyright
license: show SpyderOS's license''')
    elif t=="power":
        print('''
shutdown: stops all processes
restart: stops all processes and then starts them again
sleep: all processes continue to run and the systems sleeps''')
    elif t=="num":
        print('''
math: complete math calculations
rand: generate a random number between two numbers''')
    elif t=="time":
        print('''
timer: set times for a set amount of minutes or seconds
current: show current date and time''')
    elif t=="list":
        print('''
view: look at the list
add: add an item to the list
remove: remove an item from the list''')
    else:
        exerr(2)
    print('''
Works everywhere: 
help: show list of commands
quit: quit current app (use in sys to quit os)
q: alternative to quit

For more information, visit www.github.com/chaoticducc/spyderos/wiki''')
#programs
##core
def sys():
    n="sys"
    while True:
        x = input(">> ")
        if x == "help":
            exhelp(n)
        elif x == "about":
            about()
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
        elif x == "power" or x in q:
            power()
            break
        else:
            exerr(2)
def about():
    n="about"
    while True:
        x = input(pn+n+sn)
        if x == "help":
            exhelp(n)
        elif x == "version":
            print(version)
        elif x == "credits":
            print(credits)
        elif x == "copyright":
            print(copyright)
        elif x == "license":
            print(license)
        elif x == "spiderman":
            print("With great power, comes great responsibility")
        elif x in q:
            sys()
            break
        else:
            exerr(2)
def power():
    n="power"
    while True:
        x = input(pn+n+sn)
        if x == "help":
            exhelp(n)
        elif x == "shutdown":
            expow(1)
            break
        elif x == "restart":
            print("")
            expow(1)
            time.sleep(2)
            print("")
            expow(0)
            break
        elif x == "sleep":
            expow(2)
            break
        elif x in q:
            sys()
            break
        else:
            exerr(2)
##tools
def num():
    n="num"
    while True:
        x = input(pn+n+sn)
        if x == "help":
            exhelp(n)
        elif x == "math":
            print('''
Use + to add
Use - to subtract
Use * to multiply
Use / to divide
Use // to divide without decimals
Use % to find the remainder of a divsion (so 3%2=1)
Use ** to raise to a power(so 3**2=9)
Use s to reuse previous result''')
            print(uq)
            while True:
                r = input()
                if r in q:
                    break
                else:
                    try:
                        s = eval(r)
                        print(s)
                    except:
                        exerr(1)
        elif x == "rand": 
            n1 = input("Minimum Number: ")
            r1 = int(n1)
            n2 = input("Maximum Number: ")
            r2 = int(n2)
            r = random.randint(r1,r2)
            print(r)
        elif x == "round":
            n1 = input("Number to Round: ")
            r1 = float(n1)
            n2 = input("To the nearest _: ")
            r2 = int(n2)
            r = round(r1,r2)
            print(r)
        elif x in q:
            sys()
            break
        else:
            exerr(2)
def times():
    n="time"
    while True:
        x = input(pn+n+sn)
        if x == "help":
            exhelp(n)
        elif x == "timer":
            print('''
Use m for minutes
Use s for seconds''')
            print(uq)
            t=input()
            if t in q:
                times()
            elif t == "s":
                print(ue+"start")
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
                exerr(3)
        elif x == "current":
            t = time.localtime()
            cd = time.strftime("%B %d, %Y", t)
            ch = time.strftime("%H:%M:%S", t)
            print(cd)
            print(ch)
        elif x in q:
            sys()
            break
        else:
            exerr(2)
def list():
    n="list"
    while True:
        x = input(pn+n+sn)
        if x == "help":
            exhelp(n)
        elif x == "view":
            if len(items) == 0:
                print("List Empty")
            else:
                for i in range(0,len(items)):
                    print(i,items[i])
        elif x == "add":
            print(uq)
            while True:
                i = input()
                if i in q:
                    break
                elif i == int():
                    items.pop(i)
                else:
                    items.append(i)
        elif x == "remove":
            print(uq)
            while True:
                i = input()
                if i in q:
                    break
                elif i in items:
                    items.remove(i)
                else:
                    exerr(4)
        elif x in q:
            sys()
            break
        else:
            exerr(2)
expow(0)