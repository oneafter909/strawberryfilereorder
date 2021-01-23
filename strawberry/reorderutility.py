import os
import sys
from os import listdir
from os.path import isfile, join
import shutil
import datetime
import time
from GUI import textColors
from creationdateutils import Date
import faceRecognizer as FR
def eR(p, recursive):     

    print(textColors.BOLD+"Reorder by extension"+textColors.RESET)                                                                                                          
    totFile = 0

    if p == "":
        p = input("Enter a directory: ")
        
    print("SELECTED DIRECTORY: ")
    print("["+p+"]")

    #---[Arrays of extensions]---
    filesDocs = []
    filesAudio = []
    filesVideo = []
    filesPhoto = []
    filesSource = []
    filesCompressed = []
    filesFont = []
    filesPACK = []
    filesJAR = []
    filesIcon = []
    filesImage= []
    files3DM = []
    #----------------------------
    #---[Check the extensions]---
    for r, d, f in os.walk(p):    
        for file in f:
            if '.txt' in file or '.docx' in file or '.pdf' in file or '.xlsx' in file or '.pptx' in file or '.odt' in file or '.ods' in file or '.odp' in file or '.odm' in file or '.rtf' in file or '.odd' in file or '.sxw' in file or '.readme' in file or '.sxi' in file or '.ppt' in file or '.doc' in file or '.xls' in file or '.odb' in file:
                filesDocs.append(os.path.join(r, file)) 
            if '.png' in file or '.jpeg' in file or '.jpg' in file or '.JPG' in file or '.JPEG' in file or '.PNG' in file or '.jfif' in file or '.tiff' in file or '.cr2' in file or '.CR2' in file or '.gif' in file or '.GIF' in file or '.JFIF' in file or '.bmp' in file or '.BMP' in file or '.webp' in file or '.WEBP' in file or '.heic' in file or '.heif' in file or '.HEIC' in file or '.HEIF' in file or '.SVG' in file or '.svg' in file or '.raw' in file or '.RAW' in file or '.pict' in file or '.EPS' in file or '.eps' in file or '.dng' in file or '.DNG' in file:
                filesPhoto.append(os.path.join(r, file))
            if '.mp3' in file or '.m4a' in file or '.ogg' in file or '.m4b' in file or '.wav' in file or '.flac' in file or '.m4r' in file or '.midi' in file or '.mid' in file:
                filesAudio.append(os.path.join(r, file)) 
            if '.mp4' in file or '.m4v' in file or '.mov' in file or '.MOV' in file or '.MP4' in file or '.flac' in file or '.avi' in file or '.mkv' in file or '.MKV' in file:
                filesVideo.append(os.path.join(r, file)) 
            if '.ttf' in file or '.otf' in file or '.woff' in file or '.eot' in file:
                filesFont.append(os.path.join(r, file))
            if '.c' in file or '.h' in file or '.cs' in file or '.py' in file or '.cpp' in file or '.vb' in file or '.csproj' in file or '.sln' in file or '.htm' in file or '.html' in file or '.css' in file or '.js' in file or '.xml' in file or '.xaml' in file or '.sh' in file:
                filesSource.append(os.path.join(r, file)) 
            if '.zip' in file or '.rar' in file or '.7z' in file or '.tar' in file or '.xz' in file or '.gz' in file or '.tgz' in file or '.tbz' in file or '.tbz2' in file or '.bz' in file:
                filesCompressed.append(os.path.join(r, file))
            if '.deb' in file or '.pkg' in file or '.snap' in file or '.rpm' in file or '.dnf' in file or '.AppImage' in file:
                filesPACK.append(os.path.join(r, file))  
            if '.ico' in file:
                filesIcon.append(os.path.join(r, file))
            if '.jar' in file:
                filesJAR.append(os.path.join(r, file))
            if '.iso' in file or '.img' in file or '.bin' in file or '.cue' in file:
                filesImage.append(os.path.join(r, file))
            if '.blend'in file:
                files3DM.append(os.path.join(r, file))
        if recursive == False:    
            break
    #----------------------------------------------------

    newDir = p + "/Document Files/"
    DirB = p + "/Document\ Files/"
    try:
        if filesDocs:
            print("DOCS FILES")
            if os.path.exists(newDir) is False:
                os.mkdir(newDir)
                print("Creating the directory: " + newDir)

            for f in filesDocs:
                source = f
                destination = newDir+os.path.basename(f)
                now = datetime.datetime.now()
                a = now.strftime("%Y%m%d%H%M%S")+"[dx]"
                destinationDX = newDir+a+os.path.basename(f)
                if os.path.exists(destination):
                    print("Transfer: " + os.path.basename(source)+" (This is a duplicated, this file will have a [dx] sign to be easily recognized.") 
                    shutil.move(source, destinationDX) #duplicated
                else:
                    print("Transfer: " + os.path.basename(source)) 
                    shutil.move(source, destination)
                totFile+=1    

    except:
        print("Error")

    #----------------------------------------------------

    newDir = p + "/Image files/"
    DirB = p + "/Image\ files/"
    try:
        if filesPhoto:
            print("IMAGE FILES")
            if os.path.exists(newDir) is False:
                os.mkdir(newDir)
                print("Making the directory: " + newDir)
            for f in filesPhoto:
                source = f
                destination = newDir+os.path.basename(f)
                now = datetime.datetime.now()
                a = now.strftime("%Y%m%d%H%M%S")+"[dx]"
                destinationDX = newDir+a+os.path.basename(f)
                if os.path.exists(destination):
                    print("Transfer: " + os.path.basename(source)+" (This is a duplicated, this file will have a [dx] sign to be easily recognized.")
                    shutil.move(source, destinationDX) #duplicated
                else:
                    print("Transfer: " + os.path.basename(source))
                    shutil.move(source, destination)
                totFile+=1
    except:
        print("Error")

    #----------------------------------------------------

    newDir = p + "/Video files/"
    DirB = p + "/Video\ files/"
    try:
        if filesVideo:
            print("VIDEO FILES")
            if os.path.exists(newDir) is False:
                os.mkdir(newDir)
                print("Making the directory: " + newDir)

            for f in filesVideo:
                source = f
                destination = newDir+os.path.basename(f)
                now = datetime.datetime.now()
                a = now.strftime("%Y%m%d%H%M%S")+"[dx]"
                destinationDX = newDir+a+os.path.basename(f)
                if os.path.exists(destination):
                    print("Transfer: " + os.path.basename(source)+" (This is a duplicated, this file will have a [dx] sign to be easily recognized.")
                    shutil.move(source, destinationDX) #duplicated
                else:
                    print("Transfer: " + os.path.basename(source))
                    shutil.move(source, destination)
                totFile+=1 

    except Exception as e:
        print("An error occurred.")
        print(e)

    #----------------------------------------------------

    newDir = p + "/Font files/"
    DirB = p + "/Font\ files/"
    try:
        if filesFont:
            print("FONT FILES")
            if os.path.exists(newDir) is False:
                os.mkdir(newDir)
                print("Making the directory: " + newDir)

            for f in filesFont:
                source = f
                destination = newDir+os.path.basename(f)
                now = datetime.datetime.now()
                a = now.strftime("%Y%m%d%H%M%S")+"[dx]"
                destinationDX = newDir+a+os.path.basename(f)
                if os.path.exists(destination):
                    print("Transfer: " + os.path.basename(source)+" (This is a duplicated, this file will have a [dx] sign to be easily recognized.") 
                    shutil.move(source, destinationDX) #duplicated
                else:
                    print("Transfer: " + os.path.basename(source)) 
                    shutil.move(source, destination)
                totFile+=1 

    except Exception as e:
        print("An error occurred.")
        print(e)

    #----------------------------------------------------

    newDir = p + "/Jar files/"
    DirB = p + "/Jar\ files/"
    try:
        if filesJAR:
            print("JAR FILES")
            if os.path.exists(newDir) is False:
                os.mkdir(newDir)
                print("Making the directory: " + newDir)

            for f in filesJAR:
                source = f
                destination = newDir+os.path.basename(f)
                now = datetime.datetime.now()
                a = now.strftime("%Y%m%d%H%M%S")+"[dx]"
                destinationDX = newDir+a+os.path.basename(f)
                if os.path.exists(destination):
                    print("Transfer: " + os.path.basename(source)+" (This is a duplicated, this file will have a [dx] sign to be easily recognized.") 
                    shutil.move(source, destinationDX) #duplicated
                else:
                    print("Transfer: " + os.path.basename(source)) 
                    shutil.move(source, destination)
                totFile+=1 

    except Exception as e:
        print("An error occurred.")
        print(e)

    #----------------------------------------------------

    newDir = p + "/Packages/"
    DirB = p + "/Packages/"
    try:
        if filesPACK:
            print("PACKAGES FILES")
            if os.path.exists(newDir) is False:
                os.mkdir(newDir)
                print("Making the directory: " + newDir)

            for f in filesPACK:
                source = f
                destination = newDir+os.path.basename(f)
                now = datetime.datetime.now()
                a = now.strftime("%Y%m%d%H%M%S")+"[dx]"
                destinationDX = newDir+a+os.path.basename(f)
                if os.path.exists(destination):
                    print("Transfer: " + os.path.basename(source)+" (This is a duplicated, this file will have a [dx] sign to be easily recognized.") 
                    shutil.move(source, destinationDX) #duplicated
                else:
                    print("Transfer: " + os.path.basename(source)) 
                    shutil.move(source, destination)
                totFile+=1 

    except Exception as e:
        print("An error occurred.")
        print(e)

    #----------------------------------------------------

    newDir = p + "/Compressed files/"
    DirB = p + "/Compressed\ files/"
    try:
        if filesCompressed:
            print("COMPRESSED FILES")
            if os.path.exists(newDir) is False:
                os.mkdir(newDir)
                print("Making the directory: " + newDir)

            for f in filesCompressed:
                source = f
                destination = newDir+os.path.basename(f)
                now = datetime.datetime.now()
                a = now.strftime("%Y%m%d%H%M%S")+"[dx]"
                destinationDX = newDir+a+os.path.basename(f)
                if os.path.exists(destination):
                    print("Transfer: " + os.path.basename(source)+" (This is a duplicated, this file will have a [dx] sign to be easily recognized.") 
                    shutil.move(source, destinationDX) #duplicated
                else:
                    print("Transfer: " + os.path.basename(source)) 
                    shutil.move(source, destination)
                totFile+=1 

    except Exception as e:
        print("An error occurred.")
        print(e)

    #----------------------------------------------------

    newDir = p + "/Source Code files/"
    DirB = p + "/Source\ Code\ files/"
    try:
        if filesSource:
            print("SOURCE CODE FILES")
            if os.path.exists(newDir) is False:
                os.mkdir(newDir)
                print("Making the directory: " + newDir)

            for f in filesSource:
                source = f
                destination = newDir+os.path.basename(f)
                now = datetime.datetime.now()
                a = now.strftime("%Y%m%d%H%M%S")+"[dx]"
                destinationDX = newDir+a+os.path.basename(f)
                if os.path.exists(destination):
                    print("Transfer: " + os.path.basename(source)+" (This is a duplicated, this file will have a [dx] sign to be easily recognized.") 
                    shutil.move(source, destinationDX) #duplicated
                else:
                    print("Transfer: " + os.path.basename(source))
                    shutil.move(source, destination)
                totFile+=1 

    except Exception as e:
        print("An error occurred.")
        print(e)

    #----------------------------------------------------

    newDir = p + "/Icon files/"
    DirB = p + "/Icon\ files/"
    try:
        if filesIcon:
            print("ICON FILES")
            if os.path.exists(newDir) is False:
                os.mkdir(newDir)
                print("Making the directory: " + newDir)

            for f in filesSource:
                source = f
                destination = newDir+os.path.basename(f)
                now = datetime.datetime.now()
                a = now.strftime("%Y%m%d%H%M%S")+"[dx]"
                destinationDX = newDir+a+os.path.basename(f)
                if os.path.exists(destination):
                    print("Transfer: " + os.path.basename(source)+" (This is a duplicated, this file will have a [dx] sign to be easily recognized.") 
                    shutil.move(source, destinationDX) #duplicated
                else:
                    print("Transfer: " + os.path.basename(source))
                    shutil.move(source, destination)
                totFile+=1 

    except Exception as e:
        print("An error occurred.")
        print(e)

    #----------------------------------------------------

    newDir = p + "/Audio files/"
    DirB = p + "/Audio\ files/"
    try:
        if filesAudio:
            print("AUDIO FILES")
            if os.path.exists(newDir) is False:
                os.mkdir(newDir)
                print("Making the directory: " + newDir)

            for f in filesAudio:
                source = f
                destination = newDir+os.path.basename(f)
                now = datetime.datetime.now()
                a = now.strftime("%Y%m%d%H%M%S")+"[dx]"
                destinationDX = newDir+a+os.path.basename(f)
                if os.path.exists(destination):
                    print("Transfer: " + os.path.basename(source)+" (This is a duplicated, this file will have a [dx] sign to be easily recognized.") 
                    shutil.move(source, destinationDX) #duplicated
                else:
                    print("Transfer: " + os.path.basename(source))
                    shutil.move(source, destination)
                totFile+=1 

    except Exception as e:
        print("An error occurred.")
        print(e)
    #----------------------------------------------------

    newDir = p + "/3D model files/"
    DirB = p + "/3D\ model\ files/"
    try:
        if files3DM:
            print("F3D MODEL FILES")
            if os.path.exists(newDir) is False:
                os.mkdir(newDir)
                print("Making the directory: " + newDir)

            for f in files3DM:
                source = f
                destination = newDir+os.path.basename(f)
                now = datetime.datetime.now()
                a = now.strftime("%Y%m%d%H%M%S")+"[dx]"
                destinationDX = newDir+a+os.path.basename(f)
                if os.path.exists(destination):
                    print("Transfer: " + os.path.basename(source)+" (This is a duplicated, this file will have a [dx] sign to be easily recognized.") 
                    shutil.move(source, destinationDX) #duplicated
                else:
                    print("Transfer: " + os.path.basename(source)) 
                    shutil.move(source, destination)
                totFile+=1 
    #----------------------------------------------------

    except Exception as e:
        print("An error occurred.")
        print(e)

    #-----------------------------------------------------------

    newDir = p + "/Disk Image files/"
    DirB = p + "/Disk\ Image\ files/"
    try:
        if filesImage:
            print("DISK IMAGE FILES")
            if os.path.exists(newDir) is False:
                os.mkdir(newDir)
                print("Making the directory: " + newDir)

            for f in filesImage:
                source = f
                destination = newDir+os.path.basename(f)
                now = datetime.datetime.now()
                a = now.strftime("%Y%m%d%H%M%S")+"[dx]"
                destinationDX = newDir+a+os.path.basename(f)
                if os.path.exists(destination):
                    print("Transfer: " + os.path.basename(source)+" (This is a duplicated, this file will have a [dx] sign to be easily recognized.") 
                    shutil.move(source, destinationDX) #duplicated
                else:
                    print("Transfer: " + os.path.basename(source))
                    shutil.move(source, destination)
                totFile+=1 

    except Exception as e:
        print("An error occurred.")
        print(e)

    if totFile == 0:
        print("Any file with recognized extension has been found")
        exit()
    else:
        print("Total transferred files: " + str(totFile))
        exit()
#-------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------[Advanced Reorder]------------------------------------------------------
def aR(dy, e, n):
    totFile=0
    print(textColors.BOLD+"Advanced Reorder"+textColors.RESET)
    if dy == "":
        dy = input("Enter a directory: ")
        print("SELECTED DIRECTORY: ")
        print("["+dy+"]")   
    if e=="":
        e=input("Enter an extension: ")
    if e[0] != ".": #Check
        print("E: you haven't inserted an extension!")
        aR("","","")
    if n=="":
        n=input("Enter the name of the new folder where the files will go: ")
    filesOwn = []
    for r, d, f in os.walk(dy):
        for file in f:
            if e in file:
                filesOwn.append(os.path.join(r, file)) 
        break
    newDir=dy +"/"+n+"/"
    try:
        if filesOwn:
            print(e + " FILES")
            if os.path.exists(newDir) is False:
                os.mkdir(newDir)
                print("Creating the directory: " + newDir)

            for f in filesOwn:
                source = f
                destination = newDir+os.path.basename(f)
                now = datetime.datetime.now()
                a = now.strftime("%Y%m%d%H%M%S")+"[dx]"
                destinationDX = newDir+a+os.path.basename(f)
                if os.path.exists(destination):
                    print("Transfer: " + os.path.basename(source)+" (This is a duplicated, this file will have a [dx] sign to be easily recognized.") 
                    shutil.move(source, destinationDX) #duplicated
                else:
                    print("Transfer: " + os.path.basename(source)) 
                    shutil.move(source, destination)
                totFile+=1    
        print("Total transferred files: "+ str(totFile))

    except Exception as eX:
        print("An error occurred.")
        print(eX)
    input("Press Enter to continue...")
    exit()
#------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------[Reorder by keyword]-----------------------------------------------

def kwR(dy, kw, n):
    print(textColors.BOLD+"Reorder by keyword"+textColors.RESET)
    totFile=0
    if dy == "":
        dy = input("Enter a directory: ")
        print("SELECTED DIRECTORY: ")
        print("["+dy+"]")   
    if kw == "":
        kw=input("Enter a keyword: ")
    if n == "":
      n=input("Enter a name for the folder where the files will go: ")
    filesOwn = []
    for r, d, f in os.walk(dy):
        for file in f:
            if kw in file:
                filesOwn.append(os.path.join(r, file)) 
        break
    newDir=dy +"/"+n+"/"
    try:
        if filesOwn:
            print("The files containing the keyword <" + kw + "> will moved in " + newDir)
            if os.path.exists(newDir) is False:
                os.mkdir(newDir)
                print("Creating the directory: " + newDir)

            for f in filesOwn:
                source = f
                destination = newDir+os.path.basename(f)
                now = datetime.datetime.now()
                a = now.strftime("%Y%m%d%H%M%S")+"[dx]"
                destinationDX = newDir+a+os.path.basename(f)
                if os.path.exists(destination):
                    print("Transfer: " + os.path.basename(source)+" (This is a duplicated, this file will have a [dx] sign to be easily recognized.") 
                    shutil.move(source, destinationDX) #duplicated
                else:
                    print("Transfer: " + os.path.basename(source)) 
                    shutil.move(source, destination)
                totFile+=1    
        print("Total transferred files: "+ str(totFile))

    except Exception as eX:
        print("An error occurred.")
        print(eX)
    input("Press Enter to continue...")
    exit()

#----------------------------------------------------------------------------------------------------------------------
#------------------------------------------[REORDER BY DATE LINUX]-----------------------------------------------------
#It is not a real reorder by creation date, but it takes the "last modified" time.
def LbdR(dy, dR1, dR2, e):
    print(textColors.BOLD+"Reorder by Date"+textColors.RESET)
    totFile=0
    iE=False
    if e == ".*":
        iE=False       
    if dy == "":
        dy = input("Enter a directory: ")
        print("SELECTED DIRECTORY: ")
        print("["+dy+"]")
    if dR1 == "" and dR2 == "" and e == "":
        dR1=input("Enter the first date (YYYY-mm-dd): ")
        dR2=input("Enter the second date (YYYY-mm-dd): ")
    if e == "":
        dwE=input("Do you want to specify an extension?[y or n]: ")
        if dwE == "y":
            iE=True
        elif dwE=="n":
            iE=False
        else:
            print("Unknown answer")
            LbdR("","","","")
        if iE==True:
            e=input("Insert an exstension: ")
        if sys.argv[:0]:
            if e[0] != ".":
                print("E: You haven't inserted an extension!")
                LbdR("","","","")
    
    #Let's Parse the two dates
    d1=datetime.datetime.strptime(dR1, '%Y-%m-%d')
    d2=datetime.datetime.strptime(dR2, '%Y-%m-%d')
    newDir = dy + "/Files from " +d1.strftime("%d")+" "+ d1.strftime("%B") +" "+ d1.strftime("%Y") + " to "+d2.strftime("%d") +" " + d2.strftime("%B") + " " + d2.strftime("%Y")+"/"
    filesOwn = []
    for r, d, f in os.walk(dy): 
        for file in f:
            d=os.path.join(r,file) 
            dC = datetime.datetime.strptime(Date.getDateFromFile(d),'%a %b %d %H:%M:%S %Y')                                                                 #Get the creation date from the file
            if iE == False: 
                if d1 <= dC and d2 >= dC:                                                                                                 #if creation time is included then...    
                    filesOwn.append(os.path.join(r, file))
            else:
                if d1 <= dC and d2 >= dC and e in file:                                                                                   #if creation time is included and also the extension then...    
                    filesOwn.append(os.path.join(r, file))
        break 
    try:
        if iE == False:
            if filesOwn:
                print("The files from "+d1.strftime("%d")+" "+ d1.strftime("%B") + " to "+d2.strftime("%d")+" "+ d2.strftime("%B") +" will moved in " + newDir)
                if os.path.exists(newDir) is False:
                    os.mkdir(newDir)
                    print("Creating the directory: " + newDir)
                for f in filesOwn:
                    source = f
                    destination = newDir+os.path.basename(f)
                    now = datetime.datetime.now()
                    a = now.strftime("%Y%m%d%H%M%S")+"[dx]"
                    destinationDX = newDir+a+os.path.basename(f)
                    if os.path.exists(destination):
                        print("Transfer: " + os.path.basename(source)+" (This is a duplicated, this file will have a [dx] sign to be easily recognized.") 
                        shutil.move(source, destinationDX) #duplicated
                    else:
                        print("Transfer: " + os.path.basename(source)) 
                        shutil.move(source, destination)
                    totFile+=1    
            print("Total transferred files: "+ str(totFile))
        else:  #Extension
            #Change folder name to a new folder name
            newDir = dy + "/Files from " +d1.strftime("%d")+" "+ d1.strftime("%B") +" "+ d1.strftime("%Y") + " to "+d2.strftime("%d") +" " + d2.strftime("%B") + " " + d2.strftime("%Y")+" ("+e+")"+"/"
            if filesOwn:
                print("The files from "+d1.strftime("%d")+" "+ d1.strftime("%B") + " to "+d2.strftime("%d")+" "+ d2.strftime("%B") +" will moved in " + newDir)
                if os.path.exists(newDir) is False:
                    os.mkdir(newDir)
                    print("Creating the directory: " + newDir)
                for f in filesOwn:
                    source = f
                    destination = newDir+os.path.basename(f)
                    now = datetime.datetime.now()
                    a = now.strftime("%Y%m%d%H%M%S")+"[dx]"
                    destinationDX = newDir+a+os.path.basename(f)
                    if os.path.exists(destination):
                        print("Transfer: " + os.path.basename(source)+" (This is a duplicated, this file will have a [dx] sign to be easily recognized.") 
                        shutil.move(source, destinationDX) #duplicated
                    else:
                        print("Transfer: " + os.path.basename(source)) 
                        shutil.move(source, destination)
                    totFile+=1    
            print("Total transferred files: "+ str(totFile))            
    except Exception as eX:
        print("An error occurred.")
        print(eX)
    input("Press Enter to continue...")
    exit()    

#-------------------------------------------------[Reorder by Date]-------------------------------------------------------------------
def bdR(dy, dR1, dR2, e):
    if sys.platform == "linux":
        print("GNU/Linux doesn't support the date reorder. :(")
        exit()
    print(textColors.BOLD+"Reorder by Date"+textColors.RESET)
    totFile=0
    iE=False
    if e == ".*":
        iE=False       
    if dy == "":
        dy = input("Enter a directory: ")
        print("SELECTED DIRECTORY: ")
        print("["+dy+"]")
    if dR1 == "" and dR2 == "" and e == "":
        dR1=input("Enter the first date (YYYY-mm-dd): ")
        dR2=input("Enter the second date (YYYY-mm-dd): ")
    if e == "":
        dwE=input("Do you want to specify an extension?[y or n]: ")
        if dwE == "y":
            iE=True
        elif dwE=="n":
            iE=False
        else:
            print("Unknown answer")
            bdR("","","","")
        if iE==True:
            e=input("Insert an exstension: ")
        if e[0] != ".":
            print("E: You haven't inserted an extension!")
            bdR("","","","")
    
    #Let's Parse the two dates
    d1=datetime.datetime.strptime(dR1, '%Y-%m-%d')
    d2=datetime.datetime.strptime(dR2, '%Y-%m-%d')
    newDir = dy + "/Files from " +d1.strftime("%d")+" "+ d1.strftime("%B") +" "+ d1.strftime("%Y") + " to "+d2.strftime("%d") +" " + d2.strftime("%B") + " " + d2.strftime("%Y")+"/"
    filesOwn = []
    for r, d, f in os.walk(dy): 
        for file in f:
            d=os.path.join(r,file) 
            dC = datetime.datetime.fromtimestamp(os.stat(d).st_birthtime)                                                                 #Get the creation date from the file
            if iE == False: 
                if d1 <= dC and d2 >= dC:                                                                                                 #if creation time is included then...    
                    filesOwn.append(os.path.join(r, file))
            else:
                if d1 <= dC and d2 >= dC and e in file:                                                                                   #if creation time is included and also the extension then...    
                    filesOwn.append(os.path.join(r, file))
        break 
    try:
        if iE == False:
            if filesOwn:
                print("The files from "+d1.strftime("%d")+" "+ d1.strftime("%B") + " to "+d2.strftime("%d")+" "+ d2.strftime("%B") +" will moved in " + newDir)
                if os.path.exists(newDir) is False:
                    os.mkdir(newDir)
                    print("Creating the directory: " + newDir)
                for f in filesOwn:
                    source = f
                    destination = newDir+os.path.basename(f)
                    now = datetime.datetime.now()
                    a = now.strftime("%Y%m%d%H%M%S")+"[dx]"
                    destinationDX = newDir+a+os.path.basename(f)
                    if os.path.exists(destination):
                        print("Transfer: " + os.path.basename(source)+" (This is a duplicated, this file will have a [dx] sign to be easily recognized.") 
                        shutil.move(source, destinationDX) #duplicated
                    else:
                        print("Transfer: " + os.path.basename(source)) 
                        shutil.move(source, destination)
                    totFile+=1    
            print("Total transferred files: "+ str(totFile))
        else:  #Extension
            #Change folder name to a new folder name
            newDir = dy + "/Files from " +d1.strftime("%d")+" "+ d1.strftime("%B") +" "+ d1.strftime("%Y") + " to "+d2.strftime("%d") +" " + d2.strftime("%B") + " " + d2.strftime("%Y")+" ("+e+")"+"/"
            if filesOwn:
                print("The files from "+d1.strftime("%d")+" "+ d1.strftime("%B") + " to "+d2.strftime("%d")+" "+ d2.strftime("%B") +" will moved in " + newDir)
                if os.path.exists(newDir) is False:
                    os.mkdir(newDir)
                    print("Creating the directory: " + newDir)
                for f in filesOwn:
                    source = f
                    destination = newDir+os.path.basename(f)
                    now = datetime.datetime.now()
                    a = now.strftime("%Y%m%d%H%M%S")+"[dx]"
                    destinationDX = newDir+a+os.path.basename(f)
                    if os.path.exists(destination):
                        print("Transfer: " + os.path.basename(source)+" (This is a duplicated, this file will have a [dx] sign to be easily recognized.") 
                        shutil.move(source, destinationDX) #duplicated
                    else:
                        print("Transfer: " + os.path.basename(source)) 
                        shutil.move(source, destination)
                    totFile+=1    
            print("Total transferred files: "+ str(totFile))            
    except Exception as eX:
        print("An error occurred.")
        print(eX)
    input("Press Enter to continue...")
    exit()
#---------------[Reorder by face]----------------
def fR(p, faceModel, d):
    if p != "" and faceModel != "" and d != "":
        if os.path.exists(p) and os.path.isfile(faceModel):
            FR.main(p, faceModel, d)
        else:
            print("An error occurred.")
            fR("","","")
    else:
        p = input("Enter a directory: ")
        faceModel = input("Enter the image face model directory: ")
        d = input("Enter a name for the destination folder: ")
        try:
            if os.path.exists(p) and os.path.isfile(faceModel):
                FR.main(p, faceModel, d)
            else:
                print("An error occurred.")
                fR("","","")
        except Exception as eX:
            print("An error occurred.")
            fR("","","")
    input("Press any key to continue...")
    exit()


