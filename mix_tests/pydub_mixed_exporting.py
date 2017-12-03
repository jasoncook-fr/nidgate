"""
The following code will mix and layer random clips of sound into ten second segments.
It begins with using only one sound clip and loops all the way to 100 sound clips.
If I remember correctly, I have added analysis to the length of the sounds chosen before applying to the mix, 
so as to avoid passing the 10 second cutoff (ex. if a clip is 3 seconds long, 
it will be constrained to start anywhere before 7 second mark of resulting mix)

To do: Random here is not true. would be best to improve the code so as to avoid reusing a same clip of sound in the same mix 
"""
from pydub import AudioSegment
import random
import dircache
import os
from pydub.playback import play
from time import sleep

#declare the path where we will be seeking our sound files to use in mix
dir = '/path/to/directory/origin/soundfiles/'

#initialize variables
sounds = []
pos_x = []
mixed = []
count = 10
mix_length = 11000
#mixed = AudioSegment.silent(duration=10000)

try:
	while count < 100:
		for x in range(count):
			if x == 1:
				""" 
				Here we declare our final mixed clip duration.
				To avoid confusion, overlay function in pydub uses first sound clip
				to determine the permitted length for all following sound clips
				"""
				sounds.append(AudioSegment.silent(duration=mix_length))
			else:
				filename = random.choice(dircache.listdir(dir))
				print "file is ",filename 
				path = os.path.join(dir, filename)

				clip_length = len(AudioSegment.from_wav(path))
				cutoff = mix_length - clip_length
				pos_x.append(random.randint(0, cutoff))
				sounds.append(AudioSegment.from_wav(path))

		mixed = sounds[1].overlay(sounds[2])

		pos_count = 0
		for sound in sounds:
			try:
				x_int = pos_x[pos_count]
			except IndexError: 
				pass
			mixed = mixed.overlay(sound, position=x_int)
			pos_count += 1
				
		#play(mixed)
		# save file
		mixed.export("/path/to/export/directory/" + str(count) + ".wav", format='wav') # export mixed  audio file
		count += 1
		del sounds[:] # clear all list of sounds
		del pos_x[:]
		print "count is ",count

except KeyboardInterrupt:
	print " " 
	print "script terminated. goodbye!"
	exit(0)
