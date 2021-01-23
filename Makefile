default : bundle clean

bundle:
	mkdir bundle
	cp strawberry/__main__.py bundle
	cp strawberry/GUI.py bundle
	cp strawberry/swb.py bundle
	cp strawberry/reorderutility.py bundle
	cp strawberry/creationdateutils.py bundle
	cp strawberry/face_recognition_core.py bundle
	cp strawberry/face_recognition.py bundle
	cp strawberry/face_detection.py bundle
	cp strawberry/faceRecognizer.py bundle
	cp strawberry/identifier.py bundle
	rm -rf bundle/*.dist-info
	python3 -m zipapp bundle/ -o swb --python "/usr/bin/env python3" --compress
	chmod +x swb

clean:
	rm -rf bundle
