import os
import sys
from os import listdir
from os.path import isfile, join
import shutil
from GUI import textColors
from reorderutility import eR, aR, kwR, bdR
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
            print("E: this command can't be execute on Linux systems.") #For now.
            exit()
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

    if sys.argv[8:]:
        if sys.argv[1] == "-bdR":
            bdR(sys.argv[2], sys.argv[4], sys.argv[6], sys.argv[8])        
    if sys.argv[6:]:
        if sys.argv[1] == "-kwR":
            kwR(sys.argv[2], sys.argv[4].replace("_"," "), sys.argv[6].replace("_"," "))
    if sys.argv[5:]:
        if sys.argv[1] == "-aR":
            aR(sys.argv[2],sys.argv[4], sys.argv[5].replace("_"," "))
    if sys.argv[2:]:
        if sys.argv[1] == "-eR":
            eR(sys.argv[2])
    #When there's no args given.
    print("Enter a reordering mode: ")                                                  
    print("[1]Reorder by extension")
    print("[2]Advanced reorder")
    print("[3]Reorder by keyword")
    if sys.platform != "linux":                                                            
        print("[4]Reorder by date (Available only on macOS)")
    try:
        iP=input("Enter a mode: ")
        switchApp(int(iP))
    except KeyboardInterrupt as ki:
        os.system("clear")
        exit()
