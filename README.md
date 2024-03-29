# Data Scraping Tools
A github repo that include tools used to gather data for deep learning based projects. 

*This repo assumes you have gone through the beginning projects of the DL@DU repo and have some basic command line and python knowledge. 

## NLP Lyrics-based Tool 
Our first tool will assist in NLP-based deep learning projects. With this we can make use of a python library created by GitHub user johnwmiller that allows us to scrape song lyric data from the popular lyrics website [Genius](Genius.com).
#### Step 1:
First, on top of the libraries we have already installed for prior work in Simmon's DL repo, we install the lyricsgenius library via the package-manager pip.
To do so, issue the command via terminal: 
~~~
pip3 install lyricsgenius
~~~
This will install not only the lyricsgenius library, but also some other useful libraries for data scraping such as beautifulsoup and requests.
#### Step 2:
Next, to make use of this library and Genius's API, we must obtain an access token from their website. This portion requires us to sign up for an account (if you don't happen to have one already). Do this by visiting the [Genius Account Sign Up Page](https://genius.com/signup).


![Lyrics Genius Sign Up](/images/geniussignup.png)


After making an account, visit the [API Client Management Page](https://genius.com/api-clients) to sign up for an access token. On this page, you must add a name for your "application" as well as a website URL to link to. Name it whatever you would like and I, personally, just put my github as the link for the website. If you intend on using this for a proper application, then you may want to add the associated website, icon, etc.


![Lyrics Genius API](/images/lyricsapi.png)


Now that you have created an API client, you'll be able to generate an access token to make us of this website. The link for this page is [here](https://genius.com/api-clients) in case you need to regenerate an access token.

#### Step 3:
Finally, it's time to make use of the Genius API token. I've written a program that adds some functionality on top of the lyricsgenius library that will allow us to create text files that are relativity clean and suited for NLP task. 
If you haven't done so already, clone or download the repo and, for convenience, I would suggest just working inside this directory. Run the following program with the *-h* argument so you can see what options are available.
~~~
python3 lyricscraper.py -h
~~~
Once you have see the options available, rerun the program adding your preffered artist, number of songs, and personal Genius API token. There are defaults set if you wish to just see how it works, otherwise enter something like this:
~~~
python3 lyricscraper.py -a "Bob Dylan" -n 50 -t "YOUR GENIUS TOKEN"
~~~
Let it run for a bit (the time it takes will depend on how many songs you choose to fetch), then out should pop a text file for NLP work.
