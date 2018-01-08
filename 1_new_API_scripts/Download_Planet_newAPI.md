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

- For searching planet scenes images (i.e. PSScene) within AOI, for example all PSScenes3Band within the AOI:

`planet data search --item-type pssTRYTHIS in athena