<h1 align="center">Strawberry File Administrator</h1>

<p align="center">
  <img src="https://raw.githubusercontent.com/oneafter909/strawberryfileadministrator/master/media/home.png">
</p>

<h3 align="center">A powerful tool to tidy up folders</h2>

<br>

Strawberry is a lightweight, powerful tool to tidy up a messy folder. It has 4 technique to reoder a folder plus an additional tool to find duplicate files.
<br>

<b>1. Reorder by extension: </b></br>

<img src="https://raw.githubusercontent.com/oneafter909/strawberryfileadministrator/master/media/elementary.png">
The program will read all the files inside a directory and reorder them by their extension putting inside a specific folder

<b>2. Advanced reorder: </b></br>

<img src="https://raw.githubusercontent.com/oneafter909/strawberryfileadministrator/master/media/advanced.png">
You have the power! You can choose the extension and the name of the folder.

<b>3. Reorder by keyword:</b></br>

<img src="https://raw.githubusercontent.com/oneafter909/strawberryfileadministrator/master/media/keyword.png">
You have to enter a keyword and the name of the folder, if the folder already exists, the program will move the file inside the existing folder. If the files contains the keyword you entered, the program will move inside the folder you entered before all the files containing that keyword.

<b>4. Reorder by date:</b></br>

<img src="https://raw.githubusercontent.com/oneafter909/strawberryfileadministrator/master/media/byDate.png">
You have to enter two dates, the exstension and the directory to reorder. The program will sort only the files which are inside the range of the two dates, and takes those files and put them inside a new folder, created by the program. You can select if the program have to rename the folder with the precise day.

<b>5. Search duplicate files</b></br>

<img src="https://raw.githubusercontent.com/oneafter909/strawberryfileadministrator/master/media/findDuplicate.png">
You have to enter a directory. This function will find all duplicate files inside a directory recursively. The report file will be printed inside the selected directory.
<h3>How to install it</h3>
<b>From release</b><br>
Give the X permission to swb file then execute it with ./swb </br>
<b>From source</b></br>
Run setup.py with the following command:
<pre>sudo ./setup.py install</pre>
or run 
<pre>make</pre> 
to create the python executable file. <b>You must have to install zipapp</b>
<pre>pip3 install zipapp</pre>
<b>From Ubuntu</b>
<pre>sudo add-apt-repository ppa:jonio/strawberry && sudo apt update</pre>
then
<pre>sudo apt install strawberry</pre>
run with:
<pre>strawberry</pre>
