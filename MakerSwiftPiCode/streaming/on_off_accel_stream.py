#!/usr/bin/env python

import smbus
import RPi.GPIO as GPIO
import plotly.plotly as py
import plotly.graph_objs as go
import datetime
import time
import pigpio
import os

#os.system("sudo python /home/pi/MakerSwiftPiCode/streaming/light_stream.py")

import sys
sys.path.insert(0, '/home/pi/MakerSwiftPiCode/Code_Libraries')
from adxl345 import ADXL345

time.sleep(10)

adxl345 = ADXL345()

username = 'wwrightb'
api_key = 'dBgEpMAHIDaqMKmE90D8'
accel_stream_token = 'noxq2i8egi'
status_stream_token = 'rau4198ct2'

py.sign_in(username, api_key)

accel_trace = go.Scatter(
	x=[],
	y=[],
	stream = dict(
		token=accel_stream_token,
		maxpoints=1000
	)
)

status_trace = go.Scatter(
	x=[],
	y=[],
	stream = dict(
		token = status_stream_token,
		maxpoints = 1000
	),
	name = '0 = Off, 1 = On'
)

accel_layout = go.Layout(title = 'Box 2 Accelerometer Data')
status_layout = go.Layout(title = 'Box 2 On\Off Data')

accel_fig = go.Figure(data=[accel_trace], layout= accel_layout)
status_fig = go.Figure(data=[status_trace], layout = status_layout)

py.plot(accel_fig, filename='ACE Clearwater Graphs/Live Data/Box 2 Accelerometer Data')
py.plot(status_fig, filename='ACE Clearwater Graphs/Live Data/Box 2 On\Off Data')

accel_stream = py.Stream(accel_stream_token)
status_stream = py.Stream(status_stream_token)

accel_stream.open()
status_stream.open()

count = 0
average = 0
baseline = 0
calibrated = 0

while True:
	try:
		accel_data_storage = open("/home/pi/MakerSwiftPiCode/outputs/accel_data.txt", 'a')

		count += 1
    		axes = adxl345.getAxes(True)
    		totMag = abs(axes['x']) + abs(axes['y']) + abs(axes['z'])
		now = datetime.datetime.now().isoformat()

		accel_stream.write(dict(x=now, y=totMag)) #write accel data to plotly

		accel_data_storage.write(str(now)+'\n') #store accel data on system
		accel_data_storage.write(str(totMag)+'\n')		

		time.sleep(.1)
			
		average += totMag

		accel_data_storage.close()

		if count == 100:					
			try:
				if(calibrated == 0): #set average off value
					calibrated = 1
					baseline = average/count + .02
					print str(baseline) + " " + str(average)
					average = 0
					count = 0
					continue

				now = datetime.datetime.now().isoformat()
				print "Test: " + str(average/count)

				status_data_storage = open("/home/pi/MakerSwiftPiCode/outputs/status_data.txt", 'a')

				if(average/count > baseline): #machine on
					status_stream.write(dict(x=now, y=1))	
					
					status_data_storage.write(str(now)+'\n')
					status_data_storage.write("On\n")		
				else:
					status_stream.write(dict(x=now, y=0))

					status_data_storage.write(str(now)+'\n')	
					status_data_storage.write("Off\n")

				status_data_storage.close()

				average = 0
				count = 0

			except:
				pass
			
	except:
		pass
