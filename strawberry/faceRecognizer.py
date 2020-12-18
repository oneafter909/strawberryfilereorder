import os
import sys
import face_recognition_core as fr
import datetime
import shutil
import threading
import time
global filesOwnA
global imageExt
filesOwnA = []
imageExt = {
	"JPEG" : [".jpg",".JPG",".jpeg",".JPEG"],
	"PNG" : [".png",".PNG"]
}

def loadFaceAndReturn(p, imageInput, des):
	ki = fr.load_image_file(imageInput)
	print("Base image loaded.")
	imageEncodingg = fr.face_encodings(ki)[0]
	print("Base image encoded.")
	return imageEncodingg

def loadDirectory(p):
	for r, d, f in os.walk(p):
		for file in f:
			filename, file_extension = os.path.splitext(file)
			l = str(imageExt.values())
			if file_extension in l:
				filesOwnA.append(os.path.join(r, file))
		break

def sortByFace(p, imageInput, des, reverse, threadID):
	filesOwn = filesOwnA
	nowS = datetime.datetime.now()
	start = nowS.strftime("%H:%M:%S")
	imageEncoding = loadFaceAndReturn(p, imageInput, des)
	print(imageEncoding)
#       print(str(len(filesOwnA)))

	if reverse == "1":
		print("reversing")
		filesOwn = filesOwnA[::-1]

	for file in filesOwn:
		if os.path.exists(file):
			d = os.path.join(file)
			print("---------------------------------------------------------------------------")
			print(d)
			uk = ""
			unknownEncoding = ""
			uk = fr.load_image_file(d)
			print("Load completed")
			try:
				unknownEncoding = fr.face_encodings(uk)[0]
				print("File image encoded")
				result = fr.compare_faces([imageEncoding],unknownEncoding)
				print(result[0])
				if result[0] == True:
					newDir = p +"/"+ des
					if os.path.exists(newDir) == False:
						os.mkdir(newDir)
						print("Creating the directory: " + newDir)
					source = d
					print(os.path.basename(d))
					destination = newDir +"/"+ os.path.basename(d)
					print(destination)
					now = datetime.datetime.now()
					a = now.strftime("%Y%m%d%H%M%S")+"[dx]"
					destinationDX = newDir +"/"+ a + os.path.basename(d)
					if os.path.exists(destination):
						print ("Transfer: " + os.path.basename(source) + " (This is a duplicated, this file will have a [dx] sign to be easily recognized.")
						try:
							if os.path.exists(source):
								shutil.move(source, destinationDX)
						except:
							print("Error during move")
					else:
						try:
							if os.path.exists(source):
								print("Transfer: " + os.path.basename(source))
								shutil.move(source, destination)
						except:
							print("Error during move")
			except Exception as e:
				print("No faces detected")
	nowE = datetime.datetime.now()
	end = nowE.strftime("%H:%M:%S")
	d = datetime.datetime.strptime(end, "%H:%M:%S") - datetime.datetime.strptime(start, "%H:%M:%S")
	print(str(d.seconds) + " seconds elapsed.")


class sortFace(threading.Thread):
	def __init__(self, threadID, p, imageInput, des, reverse):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.p = p
		self.imageInput = imageInput
		self.des = des
		self.reverse = reverse
	def run(self):
		print("Starting " + self.threadID)
		sortByFace(self.p, self.imageInput, self.des, self.reverse, self.threadID)
		print("Exiting " + self.threadID)

#----------------MAIN-----------------#

#path#imageInput#Nome

def main(p, imageInput, d):
#	p = sys.argv[1]
#	imageInput = sys.argv[2]
#	d = sys.argv[3]
	loadDirectory(p)
	try:
		t1 = sortFace("1", p, imageInput, d, "0")
		t2 = sortFace("2", p, imageInput, d, "1")
		t1.start()
		t2.start()
		t1.join()
		t2.join()
		print("End")
	except Exception as e:
		print(str(e))
		print("Error starting thread")
		exit()
