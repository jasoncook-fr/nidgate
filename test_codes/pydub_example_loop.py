#this is a very basic loop of 3 audio files
from pydub import AudioSegment
from pydub.playback import play

audio1 = AudioSegment.from_file("/path/to/file_1.wav") #your first audio file
audio2 = AudioSegment.from_file("/path/to/file_2.wav") #your second audio file
audio3 = AudioSegment.from_file("/path/to/file_3.wav") #your third audio file

mixed = audio1.overlay(audio2)          #combine , superimpose audio files
mixed1  = mixed.overlay(audio3)          #Further combine , superimpose audio files
#If you need to save mixed file
mixed1.export("mixed.wav", format='wav') #export mixed  audio file

try:
	while True:  
		play(mixed1)                             #play mixed audio file

except KeyboardInterrupt:
	print "script terminated. goodbye!"
	exit(0)
