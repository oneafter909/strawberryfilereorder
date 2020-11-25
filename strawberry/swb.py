import os
import sys
from os import listdir
from os.path import isfile, join
import shutil
from GUI import textColors
from reorderutility import eR, aR, kwR, bdR, LbdR
from GUI import homeScreen, helpPage

def switchApp(i):
    if i==1:
        eR("")
    elif i==2:
        aR("", "","")
    elif i==3:
        kwR("","","")
    elif i==4:
        if sys.platform != "linux":
            bdR("","","","")
        else:
            LbdR("","","","")
    else:
        print("Command not recongnized")

def begin():
    homeScreen()
    if sys.argv[1:]:                                                               
        try:
            if sys.argv[1] == "--help" or sys.argv[1] == "-h":
                helpPage()
                exit()
        except Exception as e:
            print("An error occurred.")

            if sys.argv[1] == "-help":
                print("Type --help to get helped")
                exit()
    ###Add two to args
    if sys.argv[8:]:
        if sys.argv[1] == "-bdR":
            if os.sys.platform == "linux":
                LbdR(sys.argv[2], sys.argv[4], sys.argv[6], sys.argv[8])
            else:
                bdR(sys.argv[2], sys.argv[4], sys.argv[6], sys.argv[8])        
    if sys.argv[6:]:
        if sys.argv[1] == "-kwR":
            kwR(sys.argv[2], sys.argv[4].replace("_"," "), sys.argv[6].replace("_"," "))
    if sys.argv[6:]:
        if sys.argv[1] == "-aR":
            aR(sys.argv[2],sys.argv[4], sys.argv[6].replace("_"," "))
    if sys.argv[3:]:                                                                                   
        if sys.argv[1] == "-eR" and sys.argv[3] == "-R":
            eR(sys.argv[2],True)
    if sys.argv[2:]:
            eR(sys.argv[2], False)
    #When there's no args given.
    print("Enter a reordering mode: ")                                                  
    print("[1]Reorder by extension")
    print("[2]Advanced reorder")
    print("[3]Reorder by keyword")                                                         
    print("[4]Reorder by date")
    try:
        iP=input("Enter a mode: ")
        switchApp(int(iP))
    except KeyboardInterrupt as ki:
        os.system("clear")
        exit()
