import hashlib
import os
import sys
import datetime
import time

class DB:
    """
    Database Class
    """
    def __init__(self, p, s):
        self.percorso = ""
        self.SHA = ""
        if p != "":
            self.percorso = p
        self.SHA = s

class DBUguali:
    """
    This Database serves to merge two Database Classes
    """
    def __init__(self, p1, p2, s1, s2):
        self.percorso1 = p1
        self.SHA1 = s1
        self.percorso2 = p2
        self.SHA2 = s2

def fD(p):
    """
    Find duplicate files function
    :param p: Path
    """
    l1 = []
    l2 = []
    filesOwn = []
    filesOwn2 = []
    filesUguali = []

    if p == "":
        p = input("Enter a directory: ")
    print("Selected DIRECTORY: ")
    print("["+p+"]")
    print("Analyzing...")
    for r, d, f in os.walk(p):
        for file in f:
            l1.append(os.path.join(r, file))
            l2.append(os.path.join(r, file))
            #break <= Not R command

    for file in l1:
        if l1:
            try:
                with open(file, "rb") as fi:
                    bytes = fi.read()
                    readHash = hashlib.sha256(bytes).hexdigest()
                filesOwn.append( DB(os.path.join(r, file), readHash) )
                filesOwn2.append( DB(os.path.join(r, file), readHash) )
                filesOwn2.reverse()
            except Exception as ex:
                print(ex)

    for item in filesOwn:
        for item2 in filesOwn2:
            if (item.SHA == item2.SHA and item.percorso != item2.percorso):
                filesUguali.append( DBUguali(item.percorso, item2.percorso, item.SHA, item2.SHA) )

    if(filesUguali):
        for obj in filesUguali:
            print(obj.percorso1, obj.SHA1, obj.percorso2, obj.SHA2, sep = '\n')
            print("")
            now = datetime.datetime.now()
            a = now.strftime("%Y%m%d%H%M%S")
            f = open(p+"/DuplicateReport"+a+".txt", "a")
            f.write(obj.percorso1 +'\n'+ obj.percorso2 + '\n' + '\n')
            f.close()
            print("Report file saved in " + p + "DuplicateReport"+a+".txt")
        exit()
    else:
        print("No duplicated.")
        exit()


def test():
    if sys.argv[1:]:
        try:
            p = sys.argv[1]
            fD(p)
        except Exception as ex:
            print(ex)
    else:
        p = input("Inserisci directory: ")
        fD(p)

