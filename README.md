# Planet_acquisition
This repository describes ways to acquire Planet satellite data using two (2) versions of the Planet API refered to as the "new" and the "old" ones. Below step-by-step guide how to use these API to download bulk data from planet.

There are common steps for both the new and the old API. 

1) Download Anaconda (https://www.anaconda.com/download/): it comes with a nice suit of packages with python distribution. Install the 32 version for python 2.7 as the 64 bit will conflict with your Arcmap distribution. If you are not doing anything with arcpy then get the 64 bit. It's better and include a Jupiter Console
2) Install Planet API in Anaconda: go to >start>All programs>Anaconda Prompt and type > pip install planet at the command prompt. You will be prompted to say "y" to complete the installation. This process works better when no proxy is limiting software installation, in this case send me an email to rodbio2008@gmail.com/download/


if the intention is to download data filtered by a spatial extent (i.e. AOI), the new API differs slightly from the old one. First let's do it for the new one.

3) Open the folder above "1_new_API_scripts", you will see a PDF with instruccions how to draw and save a .geojson file that will be an argument for the API. To better read this PDF click on it and press the Download button on the right upper corner
   Save the map.geojeson file (name as default as "map") in a prefered location. This location will be where all script should be, will go to this later. 

