import os
import sys
import shutil

class infoStrawberry:
    version = "5.0"
    month_release = "January"
    year_release = "2022"

class textColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BOLD     = '\33[1m'
    ITALIC   = '\33[3m'
    SELECTED = '\33[7m'
    RED    = '\33[31m'
    GREEN  = '\33[32m'
    YELLOW = '\33[93m'

def homeScreen():
    os.system("clear")
    info = f"Jonio Strawberry File Administrator {infoStrawberry.version} ({infoStrawberry.month_release} {infoStrawberry.year_release})"
    print(f"{info}")
    print ("Running on: " + sys.platform)
 
def helpPage():
    print("")
    print(textColors.BOLD+"Welcome to Strawberry File Administrator help page!" + textColors.RESET)
    print("")
    print(textColors.YELLOW+"-h --help"+textColors.RESET+"                                                    Print this help text and exit.")
    print("")
    print(textColors.YELLOW+"--version"+textColors.RESET+"                                                    Print the actual version")
    print("")
    print(textColors.YELLOW+"-eR PATH"+textColors.RESET+"                                                     Extension (or Elementary) Reorder.")
    print("                                                             Reorder the files inside a directory")
    print("                                                             by their extension.")
    print("")
    print(textColors.YELLOW+"-aR PATH -e .EXTENSION -d FOLDER_NAME"+textColors.RESET+"                        Advanced Reorder.")
    print("                                                             Reorder the files inside a directory. You have")
    print("                                                             to specify the directory to reorder, the arrival")
    print("                                                             folder and the extension.")
    print("")
    print(textColors.YELLOW+"-kwR PATH -kw KEYWORD -d FOLDER_NAME"+textColors.RESET+"                         KeyWord Reorder.")
    print("                                                             Reorder the files inside a directory by a keyword")
    print("                                                             which you have to specify.")
    print("")
    print(textColors.YELLOW+"-bdR PATH -i YYYY-mm-dd -f YYYY-mm-dd -e .EXTENSION"+textColors.RESET+"          By Date Reorder.")
    print("                                                             Reorder the files inside a directory")
    print("                                                             by their date time creation.")
    print("                                                             You have to specify an initial date")
    print("                                                             and a final date to make a date range. If the")
    print("                                                             file creation date time respect the range, the file")
    print("                                                             will moved inside the new folder")
    print("                                                             The program will provide to create a new folder.")
    print("                                                             (Not available on Linux systems. For now.)")
    print("")
    print("")
    print(textColors.YELLOW+"-fD PATH"+textColors.RESET+"                                                     Find duplicate files")
    print("                                                             Find duplicate files recursively within a folder.")

