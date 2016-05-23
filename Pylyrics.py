from lxml import html
import requests


def clyrics(artistName, songName):
	''' Function that collects lyrics'''
	
	page = 'http://www.songlyrics.com/{}/{}-lyrics/'.format(artistName, songName)
	tree = html.parse(page)

	lyrics = tree.xpath('//p[@id="songLyricsDiv"]/text()')

	for word in lyrics:
		print(word)
def main():
	
	# Ask for artist and song name
	artistName = raw_input('Artist name : ')
	songName = raw_input('Song name : ')
	
	# Process words to match site's url formatting
	artistName = artistName.replace(' ', '-').lower()
	songName = songName.replace(' ', '-').lower()

	clyrics(artistName, songName)

if __name__ == '__main__':
	main()