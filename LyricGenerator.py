from random import randint

song_lyrics = ["I dreamed of you beneath the flowers for a couple of hours",
		"If you care to find me, look to the wester sky",
		"Everyone deserves a chance to fly",
		"I'm starting with the man in the mirror",
		"You are my Sunshine, my only Sunshine",
		"Woke up this morning, put on my slippers, walked in the kitchen and died",
		"Never ending storrrrrrrryyyyyyyyy",
		"Do a deer, a femal deer, Ray, a drop of golden sun, Me, a name I call myself",
		"And IIIII will always love youuuuuuuu",
		"In my mind I'm going to Carolina",
		"He did not know how well he sang, it just made him whole"]
		

class RandomLyric(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def pick_a_song(self):
		songs = len(song_lyrics) - 1
		random_song = randint(0, songs)
		print self.lyrics[random_song]
			
random_song_lyric = RandomLyric(song_lyrics)
			
random_song_lyric.pick_a_song()