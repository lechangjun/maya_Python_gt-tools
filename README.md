<!-- GT Tools README.md file -->
<p></p>

<img src="./docs/media/gt_logo.png">

<p></p>
<p align="center"> 
<a href="https://github.com/TrevisanGMW/gt-tools/graphs/contributors">
<img alt="GitHub contributors" src="https://img.shields.io/github/contributors/TrevisanGMW/gt-tools.svg?style=flat-square" ></a>
<img alt="GitHub language count" src="https://img.shields.io/github/languages/count/TrevisanGMW/gt-tools?style=flat-square">
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/TrevisanGMW/gt-tools?style=flat-square">

<a href="https://github.com/TrevisanGMW/gt-tools/network/members">
<img alt="GitHub forks" src="https://img.shields.io/github/forks/TrevisanGMW/gt-tools.svg?style=flat-square" ></a>

<a href="https://github.com/TrevisanGMW/gt-tools/stargazers">
<img alt="GitHub stars" src="https://img.shields.io/github/stars/TrevisanGMW/gt-tools.svg?style=flat-square" ></a>

<a href="https://github.com/TrevisanGMW/gt-tools/issues">
<img alt="GitHub issues" src="https://img.shields.io/github/issues/TrevisanGMW/gt-tools.svg?style=flat-square" ></a>

<a href="https://github.com/TrevisanGMW/gt-tools/blob/master/LICENSE">
<img alt="GitHub license" src="https://img.shields.io/github/license/TrevisanGMW/gt-tools.svg?style=flat-square" ></a>

<a href="https://www.paypal.me/TrevisanGMW"> 
<img src="https://img.shields.io/badge/$-donate-blue.svg?maxAge=2592000&amp;style=flat-square">

<a href="https://www.linkedin.com/in/trevisangmw/">
<img alt="GitHub stars" src="https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555" ></a>

</p>


<h1> Maya Python gt Tools 수정 </h1>
This is my collection of scripts for Autodesk Maya – These scripts were created ???
공부 중 ....  
<p><b>Tested using Autodesk Maya 2022 (Windows 10)</b></p>


<h1> Organization </h1>
<p><code>docs</code>: contains documentation about the scripts</p>
<p><code>mel-scripts</code>: contains scripts written in MEL</p>
<p><code>python-scripts</code>: contains scripts written in Python</p>

<h1> Installation </h1>

<b>TL;DR :</b> Download files, then open "setup.bat". 
<br>You can also click <a href="https://youtu.be/7Xa05b0cSXE">here</a> to watch a video tutorial. (Manual installation is slightly different now, I'll upload a new video soon)

It's possible to use most scripts without installing the whole package. Most of them are standalone and will work on their own, but for a better experience it's recommended that you include all scripts. This way you won't miss any dependencies.

PS: for "gt_utilities" you will have to uncomment a function at the bottom of the script, as it wouldn't make sense to call all of them at once.

The text below explains how to install it on a Windows PC, in case you're looking for MacOS or Linux check the <a href="./docs">"docs"</a> folder.

<h3>Auto Installation</h3>

This script collection comes with an auto installer (setup.bat) you can simply download it, run the setup and reopen Maya.
Here is how you do it in more details:
<ol>
	<li>Close Maya (in case it's opened).</li>
	<li>Download the latest release (or clone this repository).</li>
	<li>Un-zip (Decompress) the file you downloaded. (the setup won't work if it's still compressed)</li>
	<li>Open "setup.bat". (It will show you the options - "Install, Uninstall and About")</li>
	<li>Type "1" to "Install", then press enter.</li>
	<li>Open Autodesk Maya.</li>
</ol>


If you want, you can now delete the downloaded/extracted files (as they have already been installed)

<h3>Manual Installation</h3>

In case you need/want to manually install the scripts. It's also a pretty straightforward process.
<ol>
	<li>Close Maya (in case it's opened).</li>
	<li>Download the latest release (or clone this repository).</li>
	<li>Un-zip (Decompress) the file you downloaded.</li>
	<li>Move all the contents from the folders "mel-scripts" to your scripts folder (usually located under the path below):
	<b>C:\Users\USERNAME\Documents\maya\VERSION\scripts\ </b></li>
	<li>Move all the contents from the folders "python-scripts" to a folder called "gt_tools" inside your scripts folder:
	<b>C:\Users\USERNAME\Documents\maya\VERSION\scripts\gt_tools\ </b></li>
	<li>In case you don't want to replace an already existing <b>"userSetup.mel" </b> script (inside your scripts folder), you can easily merge them by opening the existing one and adding the line: <code>source "gt_tools_menu.mel"; </code></li>
	(This command adds the menu when Maya opens)
	<li>Open Autodesk Maya. </li>
</ol>

<h3>Updating</h3>
<p>Simply install it again. The auto setup will overwrite all files essentially updating them.
<br>If updating a major version, it's recommended that you uninstall it first before installing it again. This will eliminate any unnecessary files.
<br>In case updating it manually, make sure to overwrite (replace) the files when moving them to the scripts folder.</p>

<h1> Uninstallation </h1>

<h3>Auto Uninstallation</h3>

<ol>
	<li>Close Maya (in case it's opened).</li>
	<li>Download the latest release (or clone this repository).</li>
	<li>Un-zip (Decompress) the file you downloaded.</li>
	<li>Open "setup.bat". (It will show you the options - "Install, Uninstall and About")</li>
	<li>Type "2" to "Uninstall", then press enter.</li>
	<li>Open Autodesk Maya.</li>
</ol>

<h3>Manual Uninstallation</h3>

<ol>
	<li>Close Maya (in case it's opened).</li>
	<li>Navigate to your scripts folder, usually located under the following path:
	<b>C:\Users\USERNAME\Documents\maya\VERSION\scripts\ </b></li>
	<li>Delete "gt_tools_menu.mel" and the folder "gt_tools"</li>
	<li>Open your <b>"userSetup.mel" </b> script (inside your scripts folder), and remove the line: <code>source "gt_tools_menu.mel"; </code></li>
	<li>Open Autodesk Maya. </li>
</ol>

<h1> Frequently Asked Questions </h1>
<ul>
	<li><b>How do I update GT Tools to a new version?</b> <br>A: Simply uninstall and install it again.</li>
	<li><b>What do I do if I have multiple "userSetup.mel" files?</b> One inside "maya/####/scripts" and another one inside "maya/scripts"<br>A: The "userSetup.mel" file gets executed when you open Maya, but Maya supports only one file. In case you have two files it will give priority to the file located inside "maya/####/scripts", so manage your initialization commands there.</li>
	<li><b>Where are the other scripts you had in this repository?</b> <br> A: I moved all other scripts that are not part of GT Tools to another reposity. Here is the link: <a href="https://github.com/TrevisanGMW/maya-scripts">TrevisanGMW/maya-scripts</a> </li>
</ul>

<h1> Contributors </h1>
If you'd like to contribute, please fork the repository and make changes as you'd like. <br><b>Pull requests are warmly welcome.</b>
<p></p>
<a href="https://github.com/TrevisanGMW/gt-tools/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=TrevisanGMW/gt-tools" />
</a>

Don't know how to code but want to contribute? You could [__buy me a coffee! :coffee:__](https://www.buymeacoffee.com/TrevisanGMW)

<h1> Licensing </h1>
The MIT License 2020 - Guilherme Trevisan
