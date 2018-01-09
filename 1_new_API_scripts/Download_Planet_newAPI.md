### This is summary of main API (the "new" one) features/examples.

This summary was compiled from the [Planet-client-python](https://planetlabs.github.io/planet-client-python/index.html) , the cheat sheet by [Phil Parton](https://github.com/pparton/planet-satellite-analysis/blob/master/PlanetApiCheatSheet.md) and my experience running the API. 

Initializing the API :

`planet init`

you should be prompted to:

```
Email: *enter your email you signed up for planet here*

password: *enter the password you sign up for planet here*

```

you should receive a confirmation that your Planet API is ready to run:

`initialized`

Now practical examples how to get images based on different filters:

- For downloading planet scenes images (e.g. PSScene3Band/PSScene4band/PSOrthoTile) within a defined AOI: for example to download all PSScenes3Band, analytic, within the AOI previously downloaded `map.geojson` between dates 1/10/2017 and 30/10/2017 you type this:

`planet data download --item-type PSScene3band --asset-type analytic --date acquired gt 2017-10-01 --date acquired lt 2017-10-30 --geom map.geojson

*running this script will produce a window indicating that images are activated first and then downloaded* 

- Other practical examples to follow......