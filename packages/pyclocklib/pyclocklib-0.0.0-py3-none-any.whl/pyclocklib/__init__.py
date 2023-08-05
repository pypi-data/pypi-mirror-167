from time import *  # imports all from time
from pyautogui import * # alerts
import os # os = operating system
import sys # to exit script if error or sum
import datetime # to get datetime
#================================

print("Hello, From pyclocklib")

#===================================================

def get_currect_time(): # get's current time
    try: # try's..
        dt = datetime.datetime.now() #difining dt as time
        return print(dt) # returning it
    except Exception as en: # if error..
        print(str(en)) # print error

#====================================================


#=======================================
def set_timeout(sec: int): #set_timeout
    try: # try's
        return time.sleep(sec) # returns
    except Exception as en: # if error..
        print(str(en)) # prints
#=======================================

#=================================================
def clock_create():
    try:
            clock = 0 # Setting Clock To 0
            minu = 0 # Setting Minutes To 0
            hour = 0 # Setting Hours To 0

            while True: # Using A Loop.
                try:
                    for i in range(10000 * 10000): # Loop
                        clock = clock + 1 # For The Loop
                        time.sleep(1) # Waiting 1 Second To Add Another Seconds
                        os.system("cls") # Clearing Terminal To Look Nicer
                        if clock == 60: # If Clock Get's To 60s Add One Min
                            minu = minu + 1 # Adding One Minute
                            clock = 0 # Reseting The Clock To 0
                        if minu == 60: # If Minutes == 60
                            hour = hour + 1 # Add 1 Hour
                            minu = 0 # Reset Minutes
                        print(f"Seconds: {clock}, Minutes: {minu}, Hours: {hour}") # Print Statement
                except Exception as en: # If Error..
                    print(str(en)) # Print Error
    except Exception as en:
        print(str(en))
    
#===================================================================

#===================================================================
def set_timer(sec: int, minutes: int, hours: int):
    print("Most Features Of: set_timer Is Broken!, Will Probably Be Fixed Later On.")
    try:
        if minutes == None: # If Minutes == None
            if hours == None: # If Hours = None
                while True: # Loop
                    for i in range(sec): # A For Loop
                        try:
                            sec = sec -1 # seconds are = seconds -1
                            time.sleep(1) # waiting 1 second
                            os.system('cls') # clearing terminal
                            print(sec) # printing seconds
                            if sec == 1: # if seconds = 1
                                try: # Trying this..
                                    sys.exit(f'Timer Has Ended') # Exit The Script
                                except Exception as en: # If Error..
                                    print(str(en)) # Prints it on screen
                        except Exception as en: # If Error..
                            print(str(en)) # Prints On Screen
        if hours == None: # If Hours Are = None/0
            if sec == any: # If Sec == Any
                while True: # Loop
                    for i in range(sec): # For Loop
                        try: # Try's
                            sec = 60 #broken
                            sec = sec -1 #broken
                            time.sleep(1)#broken2
                            os.system('cls')#broken3
                            if sec == 60:#broken4
                                sec = 0#broken5
                                minutes + 1#broken6
                            print(f'Minutes: {minutes} Seconds: {sec}')#broken7
                        except Exception as en:#broken8
                            print(str(en))#broken9
    except Exception as en:#broken10
        print(str(en))#broken11
#========================================================================

def display_live_clock(): # the name
    try: # try's
        dt = datetime.datetime.now() #time
        while True: # loop
            print(dt) # prints
            os.system('cls') # clears terminal
    except Exception as en: # if error..
        print(str(en)) # ...

#=========================================================================

def currect_time(): # name of function
    try: # trying..
        t=time.ctime() # defining t as ctime
        print(f"Time: {t}") # printing on terminal
    except Exception as en: # if error...  
        print(str(en)) #prints error