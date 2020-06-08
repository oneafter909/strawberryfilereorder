# Jonio Strawberry File Reorder

Strawberry is a software which will reorder the files inside a directory by their extension
It's very simple to use, you have to write this command:

<pre>python swb_release20200525.py [DIRECTORY TO REORDER]</pre>

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

<b>How does it work?</b>
<p>The program will read all the files inside a directory. Then the program takes the extensions and put the file with the extension inside a specific folder. The name of the folder is selected by the program.
The program will create a copy of the file if the file already exists inside a folder and will rename it with the tag "[dx]".
</p>
<b>Supported OS</b>

<ul>
  <li>GNU/Linux</li>
  <li>macOS</li>
</ul>  
