# Planet_acquisition
This repository describes ways to acquire Planet satellite data using two (2) versions of the Planet API refered to as the "new" and the "old" ones. Below step-by-step guide how to use these API to download bulk data from planet.

There are common steps for both the new and the old API. 

1) Download Anaconda (https://www.anaconda.com/download/): it comes with a nice suit of packages with python distribution. Install the 32 version for python 2.7 as the 64 bit will conflict with your Arcmap distribution. If you are not doing anything with arcpy then get the 64 bit. It's better and include a Jupiter Console
2) Install Planet API in Anaconda: go to >start>All programs>Anaconda Prompt and type > pip install planet at the command prompt. You will be prompted to say "y" to complete the installation. This process works better when no proxy is limiting software installation, in this case send me an email to rodbio2008@gmail.com/download/


If the intention is to download data filtered by a spatial extent (i.e. AOI), the new API differs slightly from the old one. First let's do it for the new one.

3) Draw and save an .geojson with geographic extent: Open the folder above "1_new_API_scripts", you will see a PDF with instruccions how to draw and save a .geojson file that will be the argument for the APIs. To better read this PDF click on it and press the Download button on the right upper corner
   Save the map.geojeson file (name as default as "map") in a prefered location. This location will be where all scripts should be, will touch this later. 
   

Let's initialize the "new" Planet API in Anaconda:

4) Authenticating your credentials: go to >start>All programs>Anaconda Prompt and search for the location where the map.geojson is. Say your file is in the directory "planet_data" in D. To go to this dir, type in the command prompt first D: press enter and then type cd planet data. You should now be in D:\planet_data>. If you type dir you should see your map.geojeson file in this location


