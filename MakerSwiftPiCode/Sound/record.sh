arecord -f S16_LE -r 44100 -D hw:1,0 test.wav 
python convertWav.py
scp ~/MakerSwiftPiCode/Sound/test.wav ben@192.168.1.14:~/Music
