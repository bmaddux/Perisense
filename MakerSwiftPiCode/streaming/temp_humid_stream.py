#!/usr/bin/env python

import smbus
import RPi.GPIO as GPIO
import plotly.plotly as py
import plotly.graph_objs as go
import datetime
import time
import pigpio

import sys
sys.path.insert(0,'/home/pi/MakerSwiftPiCode/Code_Libraries')
import HTU21DF

time.sleep(10)

username = 'wwrightb'
api_key = 'dBgEpMAHIDaqMKmE90D8'
temp_stream_token = 'lr3h6wqc6n'
humidity_stream_token = 'dpzhgtnwmg'

py.sign_in(username, api_key)

temp_trace = go.Scattergl(
	x = [],
	y = [],
	mode = 'lines+markers',
	stream = dict(
		token = temp_stream_token,
		maxpoints = 1000
	)
)

humidity_trace = go.Scattergl(
	x = [],
	y = [],
	mode = 'lines+markers',
	stream = dict(
		token = humidity_stream_token,
		maxpoints = 1000
	)
)

temp_layout = go.Layout(
		title='Box Temperature Test',
		yaxis = dict(
			title='Temperature (F)',
	
			titlefont=dict(
				family = 'Calibri, serif',
				size = 18,
				color = 'blue'
			),

			range = [40,100]
		)
)

humidity_layout = go.Layout(
		title='Box 2 Humidity Data',
		yaxis = dict(
			title='% Humidity',
	
			titlefont=dict(
				family = 'Calibri, serif',
				size = 18,
				color = 'blue'
			),

			range = [0,100]
		)
)

temp_fig = go.Figure(data=[temp_trace], layout = temp_layout)
humidity_fig = go.Figure(data=[humidity_trace], layout = humidity_layout)

py.plot(temp_fig, filename='ACE Clearwater Graphs/Live Data/Box 2 Temperature Data')
py.plot(humidity_fig, filename='ACE Clearwater Graphs/Live Data/Box 2 Humidty Data')

temp_stream = py.Stream(temp_stream_token)
humidity_stream = py.Stream(humidity_stream_token)

temp_stream.open()
humidity_stream.open()

count = 0

while True:			
	try:
		time.sleep(5)
	
		now = datetime.datetime.now().isoformat()

		HTU21DF.htu_reset
		temperature = HTU21DF.read_temperature()
		temperature = temperature*9/5 + 32

		humidity = HTU21DF.read_humidity()

		temp_stream.write(dict(x=now, y=temperature))
		humidity_stream.write(dict(x=now, y=humidity))

		temp_data_storage = open("/home/pi/MakerSwiftPiCode/outputs/temperature_data.txt", 'a')
		humidity_data_storage = open("/home/pi/MakerSwiftPiCode/outputs/humidity_data.txt", 'a')

		temp_data_storage.write(str(now)+'\n')
		temp_data_storage.write(str(temperature)+'\n')
				
		humidity_data_storage.write(str(now)+'\n')
		humidity_data_storage.write(str(humidity)+'\n')

		temp_data_storage.close()
		humidity_data_storage.close()

	except:
		pass
