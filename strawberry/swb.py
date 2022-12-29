from importlib.metadata import version
import os
import sys
from os import listdir
from os.path import isfile, join
import shutil
from GUI import textColors
from reorderutility import eR, aR, kwR, bdR, LbdR
from identifier import SearchDuplicate
from GUI import homeScreen, helpPage
from GUI import infoStrawberry
version = infoStrawberry.version

def switchApp(i):
    if i==1:
        eR("", False)
    elif i==2:
        aR("", "","")
    elif i==3:
        kwR("","","")
    elif i==4:
        if sys.platform != "linux":
            bdR("","","","")
        else:
            LbdR("","","","")
    elif i==5:
        SearchDuplicate("")
    else:
        print("Command not recongnized")



def begin():

    homeScreen()

    #       args handler       #

    if sys.argv[1:]:                                                               
        try:
            if sys.argv[1] == "--help" or sys.argv[1] == "-h":
                helpPage()
                exit()
            if sys.argv[1] == "--version":
                print(version)
                exit()
        except Exception as e:
            print("An error occurred.")

            if sys.argv[1] == "-help":
                print("Type --help to get helped")
                exit()
    ###Add two to args   #swb -fR sa --imageInput sa -d sa
    if sys.argv[8:]:
        if sys.argv[1] == "-bdR" or sys.argv[1] == "--bydateReorder":
            if os.sys.platform == "linux":
                LbdR(sys.argv[2], sys.argv[4], sys.argv[6], sys.argv[8])
            else:
                bdR(sys.argv[2], sys.argv[4], sys.argv[6], sys.argv[8])        
    if sys.argv[6:]:
        if sys.argv[1] == "-kwR" or sys.argv[1] == "--keywordReorder":
            kwR(sys.argv[2], sys.argv[4].replace("_"," "), sys.argv[6].replace("_"," "))
    if sys.argv[6:]:
        if sys.argv[1] == "-aR" or sys.argv[1] == "--advancedReorder":
            aR(sys.argv[2],sys.argv[4], sys.argv[6].replace("_"," "))
    if sys.argv[3:]:                                                                                   
        if sys.argv[1] == "-eR" or sys.argv[1] == " --elementaryReorder" and sys.argv[3] == "-R":
            eR(sys.argv[2],True)
    if sys.argv[2:]:
            if sys.argv[1] == "-eR" or sys.argv[1] == " --elementaryReorder" :
                eR(sys.argv[2], False)
            elif sys.argv[1] == "-fD" or sys.argv[1] == " --findDuplicated":
                SearchDuplicate(sys.argv[2])
 
    #When there's no args given.

    print("Enter a reordering mode: ")                                                  
    print("[1]Reorder by extension")
    print("[2]Advanced reorder")
    print("[3]Reorder by keyword")                                                         
    print("[4]Reorder by date")
    print("[5]Search duplicate files")
    try:
        iP=input("Enter a mode: ")
        switchApp(int(iP))
    except KeyboardInterrupt as ki:
        os.system("clear")
        exit()
