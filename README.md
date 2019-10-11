# Data Scraping Tools
A github repo that include tools used to gather data for deep learning based projects. 

## NLP Lyrics-based Tool 
Our first tool will assist in NLP-based deep learning projects. With this we can make use of a python library created by GitHub user johnwmiller that allows us to scrape song lyric data from the popular lyrics website [Genius](Genius.com).
#### Step 1:
First, on top of the libraries we have already installed for prior work in Simmon's DL repo, we install the lyricsgenius library via the package-manage pip.
To do so, issue the command via terminal: 
~~~
pip3 install lyricsgenius
~~~
This will install not only the lyricsgenius library, but also some other useful libraries for data scraping such as beautifulsoup and requests.
#### Step 2:
Next, to make use of this library and Genius's API, we must obtain an access token from their website. This portion requires us to sign up for an account (if you don't happen to have one already). Do this by visiting the [Genius Account Sign Up Page](https://genius.com/signup).


![Lyrics Genius Sign Up](/images/geniussignup.png)


After making an account, visit the [API Client Management Page](https://genius.com/api-clients) to sign up for an access token. On this page, you must add a name for your "application" as well as a website URL to link to. Name it whatever you would like and I, personally, just put my github as the link for the website. If you intend on using this for a proper application, then you may want to add the associated website.


![Lyrics Genius API](/images/lyricsapi.png)


Now that you have created an API client, you'll be able to generate an access token to make us of this website. The link for this page is [here](https://genius.com/api-clients) in case you need to regenerated an access token.



~~Bena's personal repo for a side project in data scraping from Genius.com to assist in future NLP-based deep learning projects.~~
