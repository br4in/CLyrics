# Simple Kivi script that search for lyrics on 'songlyrics.com'

# Kivy modules
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

# Python modules
from subprocess import check_output
from lxml import html
import requests

# kv language
Builder.load_string('''
<Clyrics_s1>:
	BoxLayout:
		BoxLayout:
			id: client_box
			size_hint: 1, 1
			spacing: 10
			orientation: 'vertical'
			Label:
				id: artist_lbl
				markup: True
				size_hint: 1, .5
				text: 'Artist name:'
			TextInput:
				id: artist_input
				size_hint: 1, .2
				text: ''
				multiline: False
			Label:
				id: song_lbl
				markup: True
				size_hint: 1, .5
				text: 'Song name:'
			TextInput:
				id: song_input
				size_hint: 1, .2
				text: ''
				multiline: False
			BoxLayout:
				id: action_box
				size_hint: 1, 1
				spacing: 10
				orientation: 'vertical'
				Button:
					size_hint: 1, .1
					text: 'Get lyrics'
					on_release: root.crawl_lyrics()
				Button: 
					size_hint: 1, .1
					text: 'Watch video'
				Button:
					size_hint: 1, .1
					text: 'Refresh'
					on_release: root.refresh()
		ScrollView:
			Label:
				id: lyrics_box
				text: ''
				markup: True
        		text_size: self.width, None
				size_hint_y: None
				height: self.texture_size[1]
	
	''')
	
class Clyrics_s1(Screen):
	def __init__(self, **kwargs):
		super(Clyrics_s1, self).__init__(**kwargs)
		
	def crawl_lyrics(self):
		''' Function that collects lyrics'''
		
		self.client_box = self.ids['client_box']
		self.artist_lbl = self.ids['artist_lbl']
		self.artist_input = self.ids['artist_input']
		self.song_lbl = self.ids['song_lbl']
		self.song_input = self.ids['song_input']
		self.lyrics_box = self.ids['lyrics_box']
		# Get user input and process it to match url formatting
		artist_name = self.artist_input.text
		song_name = self.song_input.text
		artist_name = artist_name.replace(' ', '-').lower()
		song_name = song_name.replace(' ', '-').lower()
		# Collect lyrics
		try:
			page = 'http://www.songlyrics.com/{}/{}-lyrics/'.format(artist_name, song_name)
			tree = html.parse(page)

			lyrics = tree.xpath('//p[@id="songLyricsDiv"]/text()')
			lyrics_text = ' '.join(lyrics)
		# Display lyrics in lyrics_box
			self.lyrics_box.text = ('[color=00ff00][i]{}[/i][/color]'.format(lyrics_text))
		except:
			pass
	
	
	def refresh(self):
		'''Function that erase all the content in the boxes'''
		try:
			self.artist_input.text = ''
			self.song_input.text = ''
			self.lyrics_box.text = ''
		except:
			pass
		
		
class Clyrics(App):
	def build(self):
		return sm

sm = ScreenManager()

sm.add_widget(Clyrics_s1(name='Clyrics_s1'))

if __name__ == '__main__':
	Clyrics().run()
