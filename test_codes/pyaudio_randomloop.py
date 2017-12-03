#!usr/bin/env python  
#coding=utf-8  

#This is a basic example code using pyaudio and generating a randomloop of sound files

import os
import random
import dircache
import pyaudio  
import wave  

#define stream chunk   
chunk = 1024  

dir = '/path/to/dir/sound/files/'

while True:
	#open a wav format music
	filename = random.choice(dircache.listdir(dir))
        path = os.path.join(dir, filename)  
	f = wave.open(path,"rb")  
	#instantiate PyAudio  
	p = pyaudio.PyAudio()  
	#open stream  
	stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
		channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
#read data  
data = f.readframes(chunk)  

#play stream  
while data:  
    stream.write(data)  
    data = f.readframes(chunk)  

#stop stream  
stream.stop_stream()  
stream.close()  

#close PyAudio  
p.terminate()  
