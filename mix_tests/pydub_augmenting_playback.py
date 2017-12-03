from pydub import AudioSegment
import random
import dircache
import os
from pydub.playback import play
from time import sleep

dir = '/home/captain/nidgate/final_clips/'

#initialize variables
count = 1
myDelay = 10 #start delay at 10 seconds

try:
	while count < 100:
			if count < 10:
				filename = random.choice(dircache.listdir(dir))
				print "file is ",filename 
				path = os.path.join(dir, filename)
				audio = AudioSegment.from_file(path)
				play(audio)
				sleep(myDelay)
				myDelay -= 1

			else:
				dir = '/home/captain/nidgate/mix_tree/' + str(count) + '.wav'
				print dir
				filename = dir
				print "file is ",filename 
				path = os.path.join(dir, filename)
				audio = AudioSegment.from_file(path)
				play(audio)

			count += 1


except KeyboardInterrupt:
	print " " 
	print "script terminated. goodbye!"
	exit(0)