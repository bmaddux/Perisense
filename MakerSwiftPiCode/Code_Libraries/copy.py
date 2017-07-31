# A simple program to test the driver

import time
import HTU21DF

print("sending reset...")
temperature = HTU21DF.read_temperature()
print("The temperature is %f C." % temperature)
