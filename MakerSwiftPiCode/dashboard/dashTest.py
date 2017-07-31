import plotly.plotly as py
import plotly.dashboard_objs as dashboard
from IPython.display import display, Image

my_dboard = dashboard.Dashboard()

def fileID_from_url(url):
	index = url.find('~')
	fileId = url[index + 1:]
	local_id_index = fileId.find('/')

	share_key_index = fileId.find('?share_key')
	if share_key_index == -1:
		return fileId.replace('/', ':')
	else:
		return fileId[:share_key_index].replace('/', ':')

def sharekey_from_url(url):
	index = url.find('share_key=')
	return url[index + len('share_key='):]

liveParticulateID = fileID_from_url('https://plot.ly/~wwrightb/39')
liveAccelID = fileID_from_url('https://plot.ly/~wwrightb/30')
liveTempID = fileID_from_url('https://plot.ly/~wwrightb/34')
liveHumidID = fileID_from_url('https://plot.ly/~wwrightb/35')

accelerometer = {
	'type': 'box',
	'boxType': 'plot',
	'fileId': liveAccelID,
	'title': 'Live Accelerometer Data'
}

particulate = {
	'type': 'box',
	'boxType': 'plot',
	'fileId': liveParticulateID,
	'title': 'Accelerometer Data Dashboard'
}

temperature = {
	'type': 'box',
	'boxType': 'plot',
	'fileId': liveTempID,
	'title': 'Live Accelerometer Dashboard'
}

humidity = {
	'type': 'box',
	'boxType': 'plot',
	'fileId': liveHumidID,
	'title': 'Live Humidity Dashboard'
}

my_dboard.insert(accelerometer)
my_dboard.insert(particulate, 'below', 1)
my_dboard.insert(temperature, 'below', 1)
my_dboard.insert(humidity, 'right', 1)

my_dboard['settings']['foregroundColor'] = '#000000'
my_dboard['settings']['backgroundColor'] = '#72EEB8'
my_dboard['settings']['headerForegroundColor'] = '#000000'
my_dboard['settings']['headerBackgroundColor'] = '#71EEB8'
my_dboard['settings']['boxBackgroundColor'] = '#000000'
my_dboard['settings']['boxBorderColor'] = '#000000'
my_dboard['settings']['boxHeaderBackgroundColor'] = '#000000'

my_dboard['layout']['size'] = 3000

username = 'wwrightb'
api_key = 'dBgEpMAHIDaqMKmE90D8'
py.sign_in(username, api_key)

py.dashboard_ops.upload(my_dboard, 'Dashboard Test V1')



