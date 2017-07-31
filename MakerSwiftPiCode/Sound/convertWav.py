import codecs
import wave
import struct
import plotly.plotly as py
import plotly.graph_objs as go
#import os

#os.system("mpg321 -w test.wav test.mp3")

f = wave.open("test.wav", 'r')

username = 'wwrightb'
api_key = 'dBgEpMAHIDaqMKmE90D8'
py.sign_in(username, api_key)

values = f.readframes(f.getnframes())
result = struct.unpack('h'*f.getnframes(), values)
print result[:10]

newList = []

for i in range(0,len(result)):
	if(i%200==0):
		newList.append(result[i])

trace = go.Scattergl(
	x = range(1,f.getnframes()/200),
	y = newList,
	mode = 'lines'
)

data = [trace]
py.plot(data, filename='Sound Data')
