# lyricscraper.py			Author: Brendan Bena
#
#	Updated: November 1st, 2019
#
#	Program that allows for the scraping of lyrics from popular
#	lyric website genius.com. Primarily based on johnwmiller's
#	lyricsgenius python package with some added functionality for
#	NLP deep learning projects
#
# 	TO-DO modify argument parser to take list of artists and loop through each
#		then write each artist to a text file
#


import lyricsgenius as lg
import argparse
import re


# Argument Parser
parser = argparse.ArgumentParser(
    description = "Choose which artist and how many songs to search for.",
    formatter_class = argparse.ArgumentDefaultsHelpFormatter)
p = parser.add_argument
p("-s", "--songwriter", help="Choose artist to search for", type=str, default="The Beatles")
p("-t", "--token", help="Token for access of API", type=str)
p("-n", "--numofsongs", help="number of songs to grab", type=int, default=5)
p("-f", "--lyricfile", help="file to write lyrics", default='lyrics.txt')
args = parser.parse_args()


# Function to add songs to a list 
#  which will allow us to write to a text file.
#  The function will add songs if they are larger than 500 characters
#  This is an abitrarily chosen number but helps 
#  us cut out lesser quality songs
def addSongs(songs_of_artist):

	list_of_songs = []
	for song in songs_of_artist:
		length = len(song.lyrics)
		if length > 500:
			list_of_songs.append(song.lyrics)
	return list_of_songs


# Function that takes our created list of songs
#  and writes each of the songs to a combined text file
def writeToFile(text_file, song_list):
	
	with open(text_file, 'w') as lyric_file:
    		for song in song_list:
		        lyric_file.write('%s' % song)
	lyric_file.close


# Function that will clean up a text file
#  by removing bracketed phrases
# --This function could be added to if other problems arise
def cleanTextFile(text_file):
	with open(text_file, 'r') as lyric_file:
		lines = lyric_file.readlines()
	with open(text_file, 'w') as lyric_file:
		for line in lines:
			regex = re.compile(r'\[[^)]*\]')
			if regex.match(line.strip("\n")):
				pass
			else:			
				lyric_file.write('%s' % line)
	lyric_file.close


# Main Function
if __name__ == '__main__':

	# Gather CL arguments as variables
	token = args.token
	songwriter = args.songwriter
	numofsongs = args.numofsongs
	lyricfile = args.lyricfile

	# Added lyricsgenius functionality to change particulars about songs
	lg.verbose = True # Turn off status messages
	lg.remove_section_headers = True # Remove section headers (e.g. [Chorus]) from lyrics when searching
	lg.skip_non_songs = True # Include hits thought to be non-songs (e.g. track lists)
	lg.excluded_terms = ["(Remix)", "(Live)"] # Exclude songs with these words in their titles

	# Create Genius object that allows us to search for artists
	genius = lg.Genius(token)
	artist = genius.search_artist(artist_name=songwriter, max_songs=numofsongs, sort="title")

	# Create list of songs then write to text file and clean it up
	song_list = addSongs(artist.songs)
	writeToFile(lyricfile, song_list)
	cleanTextFile(lyricfile)
	





































# JUNK
# 
#song = lg.search_song("Come Together", artist.name)
#print(song.lyrics)print(artist.songs)
#artist.save_lyrics(extension='txt')
#print(artist.songs)
#print(type(artist.songs))
#	list_of_songs = []	
#	
#	for s in artist.songs:
#		length = len(s.lyrics)
#		print(length)
#		if length > 500:	
#			list_of_songs.append(s.lyrics)			
#			#print(s)
#
#	with open('lyrics.txt', 'w') as lyric_file:
#    		for song in list_of_songs:
#		        lyric_file.write('%s\n' % song)
#	
#	lyric_file.close
#
#	testString = "A test string with [brackets] in it"
#	newString = re.sub(r'\[[^)]*\]', '', testString)
#	print(newString)
