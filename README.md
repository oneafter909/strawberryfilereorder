# Jonio Strawberry File Administrator

Strawberry File Reorder is an CL application which will reorder your files.</br>

M
On Debian/Linux based systems you can download the deb package from the release tab.

Or if you want to use it from the original code, you have to write this command:

<pre>python3 strawberry</pre>
<b>Required PIP packages</b>
- conda
- pillow
- numpy
- pycoast
- cmake
- FaceRecognition

<b>How does it work?</b>
<p>
The program has 5 modalities to reorder. 

<b>1. Reorder by extension: </b></br>
The program will read all the files inside a directory and reorder them by their extension putting inside a specific folder

<b>2. Advanced reorder:</b></br>
You have the power! You can choose the extension and the name of the folder.

<b>3. Reorder by keyword:</b></br>
You have to enter a keyword and the name of the folder, if the folder already exists, the program will move the file inside the existing folder. If the files contains the keyword you entered, the program will move inside the folder you entered before all the files containing that keyword.</p>

<b>4. Reorder by date:</b></br>
You have to enter two dates, the exstension and the directory to reorder. The program will sort only the files which are inside the range of the two dates, and takes those files and put them inside a new folder, created by the program. You can select if the program have to rename the folder with the precise day.</p>

<b>5. Reorder by Face Recognition:</b></br>
You have to enter a directory, the destination and the image containing a human face. All the images which containing this face will be moved inside a new folder.

<b>Extensions supported by Strawberry</b>

<ul>
  <li>Photo: .jpeg .png .jfif .tiff .cr2 .gif .bmp .webp .heic .heif .svg .raw .eps</li>
    <li>Doc: .ods .ods .odp .docx .xlsx .ppts .rtf .odd .odb .txt .pdf</li>
    <li>Video: .mp4 .mov .m4v .avi </li>
    <li>Audio: .mp3 .m4a .ogg .m4b .wav .flac .m4r .mid .midi</li>
  <li>Font: .otf .ttf .eot .woff</li>
  <li>Source code: .c .h .cs .py .cpp .vb .xaml .sh .cproj .htm .html .css .js .sh</li>
  <li>Compressed Files: .zip .7z .rar .tar.gz .tar.xz .bz .tbz2 .tbz</li>
  <li>Packages: .deb .rpm .snap .pkg</li>
  <li>JAR: .jar</li>
  <li>Icon: .ico</li>
  <li>Images: .iso .dmg .bin .cue</li>
  <li>Blend: .blend. </li>
</ul>

<b>Supported OS</b> </br>
<b>Python Script</b>
<ul>
  <li>GNU/Linux</li>
  <li>macOS</li>
</ul>  
<b>VB.net</b>
<ul>
  <li>Windows</li>
</ul> 

*It's recommended to compile the source from the win-version section if you want to use Strawberry File Reorder on Windows.
