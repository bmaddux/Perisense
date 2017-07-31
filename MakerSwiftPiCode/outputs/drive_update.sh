#!/bin/bash

#timestamp function
timestamp() {
   date +"%Y-%m-%d_%H-%M-%S"
}

i="10"
while [ $i -gt 9 ]
do
sleep 600

t=$(timestamp)
cp /home/pi/MakerSwiftPiCode/outputs/accel_data.txt /home/pi/MakerSwiftPiCode/outputs/$t.txt
rm /home/pi/MakerSwiftPiCode/outputs/accel_data.txt
gdrive upload --parent 0BxcrH6CG152xYzM3MUg5NGtudFU /home/pi/MakerSwiftPiCode/outputs/$t.txt
rm /home/pi/MakerSwiftPiCode/outputs/$t.txt

t=$(timestamp)
cp /home/pi/MakerSwiftPiCode/outputs/humidity_data.txt /home/pi/MakerSwiftPiCode/outputs/$t.txt
rm /home/pi/MakerSwiftPiCode/outputs/humidity_data.txt
gdrive upload --parent 0BxcrH6CG152xOWJGa2FMV2xWNEE /home/pi/MakerSwiftPiCode/outputs/$t.txt
rm /home/pi/MakerSwiftPiCode/outputs/$t.txt


t=$(timestamp)
cp /home/pi/MakerSwiftPiCode/outputs/light_data.txt /home/pi/MakerSwiftPiCode/outputs/$t.txt
rm /home/pi/MakerSwiftPiCode/outputs/light_data.txt
gdrive upload --parent 0BxcrH6CG152xRURRRy02YXdaR1E /home/pi/MakerSwiftPiCode/outputs/$t.txt
rm /home/pi/MakerSwiftPiCode/outputs/$t.txt

t=$(timestamp)
cp /home/pi/MakerSwiftPiCode/outputs/dust_data.txt /home/pi/MakerSwiftPiCode/outputs/$t.txt
rm /home/pi/MakerSwiftPiCode/outputs/dust_data.txt
gdrive upload --parent 0BxcrH6CG152xV3h1OVVaR2p2LTA /home/pi/MakerSwiftPiCode/outputs/$t.txt
rm /home/pi/MakerSwiftPiCode/outputs/$t.txt

t=$(timestamp)
cp /home/pi/MakerSwiftPiCode/outputs/temperature_data.txt /home/pi/MakerSwiftPiCode/outputs/$t.txt
rm /home/pi/MakerSwiftPiCode/outputs/temperature_data.txt
gdrive upload --parent 0BxcrH6CG152xWHo1MGp4Uk1TU00 /home/pi/MakerSwiftPiCode/outputs/$t.txt
rm /home/pi/MakerSwiftPiCode/outputs/$t.txt

t=$(timestamp)
cp /home/pi/MakerSwiftPiCode/outputs/status_data.txt /home/pi/MakerSwiftPiCode/outputs/$t.txt
rm /home/pi/MakerSwiftPiCode/outputs/status_data.txt
gdrive upload --parent 0BxcrH6CG152xa1ZIY3BtdWdRbDg /home/pi/MakerSwiftPiCode/outputs/$t.txt
rm /home/pi/MakerSwiftPiCode/outputs/$t.txt

done
