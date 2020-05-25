#! /usr/bin/python3
#################################################################
#                                                               #
#                                                               #
#                                                               #
#               JONIO STRAWBERRY FILE REORDER 1.0               #
#                    2020 JONIO SOFTWARE                        #
#                                                               #
#                                                               #
#                                                               #    
#################################################################

import os
import sys
from os import listdir
from os.path import isfile, join
import shutil
import datetime
p = "" #Path
#Check args
try:
    p = sys.argv[1]
except:
    os.system("clear")
    print("Jonio Strawberry 1.0.0 release_20200525")
    print("The correct syntax is: swb [directory to reorder]")
    exit()

#Begin program
os.system("clear")
print("Jonio Strawberry 1.0.0 release_20200525")
print("SELECTED DIRECTORY: ")
print("["+p+"]")

#LET'S GO

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
totFile = 0
#----------------------------------------

#---[Check the formats]---
for r, d, f in os.walk(p):    
    for file in f:
        if '.txt' in file or '.docx' in file or '.pdf' in file or '.xlsx' in file or '.pptx' in file or '.odt' in file or '.ods' in file or '.odp' in file or '.odm' in file or '.rtf' in file or '.odd' in file or '.sxw' in file or '.readme' in file or '.sxi' in file or '.ppt' in file or '.doc' in file or '.xls' in file or '.odb' in file:
            filesDocs.append(os.path.join(r, file)) 
        if '.png' in file or '.jpeg' in file or '.jpg' in file or '.JPG' in file or '.JPEG' in file or '.PNG' in file or '.jfif' in file or '.tiff' in file or '.cr2' in file or '.CR2' in file or '.gif' in file or '.GIF' in file or '.JFIF' in file or '.bmp' in file or '.BMP' in file or '.webp' in file or '.WEBP' in file or '.heic' in file or '.heif' in file or '.HEIC' in file or '.HEIF' in file or '.SVG' in file or '.svg' in file or '.raw' in file or '.RAW' in file or '.pict' in file or '.EPS' in file or '.eps' in file:
            filesPhoto.append(os.path.join(r, file))
        if '.mp3' in file or '.m4a' in file or '.ogg' in file or '.m4b' in file or '.wav' in file or '.flac' in file or '.m4r' in file or '.midi' in file or '.mid' in file:
            filesAudio.append(os.path.join(r, file)) 
        if '.mp4' in file or '.m4v' in file or '.mov' in file or '.MOV' in file or '.MP4' in file or '.flac' in file or '.avi' in file:
            filesVideo.append(os.path.join(r, file)) 
        if '.ttf' in file or '.otf' in file or '.woff' in file or '.eot' in file:
            filesFont.append(os.path.join(r, file))
        if '.c' in file or '.h' in file or '.cs' in file or '.py' in file or '.cpp' in file or '.vb' in file or '.csproj' in file or '.sln' in file or '.htm' in file or '.html' in file or '.css' in file or '.js' in file or '.xml' in file or '.xaml' in file or '.sh' in file:
            filesSource.append(os.path.join(r, file)) 
        if '.zip' in file or '.rar' in file or '.7z' in file or '.tar' in file or '.xz' in file or '.gz' in file or '.tgz' in file or '.tbz' in file or '.tbz2' in file or '.bz' in file:
            filesCompressed.append(os.path.join(r, file))
        if '.deb' in file or '.pkg' in file or '.snap' in file or '.rpm' in file or '.dnf' in file:
            filesPACK.append(os.path.join(r, file))  
        if '.ico' in file:
            filesIcon.append(os.path.join(r, file))
        if '.jar' in file:
            filesJAR.append(os.path.join(r, file))
        if '.iso' in file or '.img' in file or '.bin' in file or '.cue' in file:
            filesImage.append(os.path.join(r, file))
        if '.blend'in file:
            files3DM.append(os.path.join(r, file))    
    break
#----------------------------------------------------

newDir = p + "/Documents Files/"
DirB = p + "/Documents\ Files/"
try:
    if filesDocs:
        print("DOCS FILES")
        if os.path.exists(newDir) is False:
            os.mkdir(newDir)
            print("Create the directory: " + newDir)

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

except Exception as e:
    print("Error: " + e.message)
    print(e)

#----------------------------------------------------

newDir = p + "/Images file/"
DirB = p + "/Images\ file/"
try:
    if filesPhoto:
        print("IMAGES FILE")
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

except Exception as e:
    print("Error: " + e.message)
    print(e)

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
    print("Error: " + e.message)
    print(e)

#----------------------------------------------------

newDir = p + "/Font file/"
DirB = p + "/Font\ file/"
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
    print("Error: " + e.message)
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
    print("Error: " + e.message)
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
    print("Error: " + e.message)
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
    print("Error: " + e.message)
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
    print("Error: " + e.message)
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
            a = now.strftime("%Y%m%d%print("Trasferisco: " + os.path.basename(source)) H%M%S")+"[dx]"
            destinationDX = newDir+a+os.path.basename(f)
            if os.path.exists(destination):
                print("Transfer: " + os.path.basename(source)+" (This is a duplicated, this file will have a [dx] sign to be easily recognized.") 
                shutil.move(source, destinationDX) #duplicated
            else:
                print("Transfer: " + os.path.basename(source))
                shutil.move(source, destination)
            totFile+=1 

except Exception as e:
    print("Error: " + e.message)
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
    print("Error: " + e.message)
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
    print("Error: " + e.message)
    print(e)

#-----------------------------------------------------------

newDir = p + "/Disk Image files/"
DirB = p + "/Disk\ Image\ files/"
try:
    if filesImage:
        print("FILE IMMAGINE DISCO")
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
    print("Error: " + e.message)
    print(e)

if totFile is 0:
    print("No file with recognized extension has been found")
else:
    print("Total transfered files: " + str(totFile))

