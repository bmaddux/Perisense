#!/usr/bin/env python

import smbus
import time
import datetime
import plotly.plotly as py
import plotly.graph_objs as go

bus = smbus.SMBus(1)

time.sleep(10)

username = 'wwrightb'
api_key = 'dBgEpMAHIDaqMKmE90D8'
light_stream_token = '6uo6wg2wib'

py.sign_in(username, api_key)

light_trace = go.Scatter(
	x=[],
	y=[],
	stream = dict(
		token = light_stream_token,
		maxpoints=1000
	)
)

light_layout = go.Layout(title='Box 2 Light Data')

light_fig = go.Figure(data=[light_trace], layout = light_layout)

py.plot(light_fig, filename='ACE Clearwater Graphs/Live Data/Box 2 Light Data')

light_stream = py.Stream(light_stream_token)

light_stream.open()

while True:
	try:	
		bus.write_byte_data(0x39, 0x00 | 0x80, 0x03)
		bus.write_byte_data(0x39, 0x01 | 0x80, 0x02)

		time.sleep(0.5)				#Change 0x39 to be whatever i2cdetect says

		data = bus.read_i2c_block_data(0x39, 0x0C | 0x80, 2)
		data1 = bus.read_i2c_block_data(0x39, 0x0E | 0x80, 2)

		ch0 = data[1]*256 + data[0]  	#ir + visible lux
		ch1 = data1[1]*256 + data1[0] 	#ir lux, ch0-ch1 = visible lux
		
		now = datetime.datetime.now().isoformat()

		print(ch0)

		light_data_storage = open("/home/pi/MakerSwiftPiCode/outputs/light_data.txt", 'a')

		light_data_storage.write(str(now)+'\n') #store data on system
		light_data_storage.write(str(ch0)+'\n')
		
		light_stream.write(dict(x=now, y=ch0)) #stream data to plotly

		light_data_storage.close()

		time.sleep(5)
	except: 
		print("Error skipped")
		pass
