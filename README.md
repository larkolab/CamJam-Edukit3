# CamJam-Edukit3
Test software for CamJam EduKit3 robot

1) 2-motors-pygame.py

The robot is controlled remotely through SSH, with a wifi adapter.

The keyboard handling is done with pygame, which need an active window to be functionnal.
So the SSH session has to be opened with X support (using -X option), then focus has to be set on the window at startup.

Then following keys are handled:
- up, down, left, right arrows for direction
- 'v' and 'b' keys for fast turning
- SPACE for stopping
- ESCAPE to exit the application

2) webiopi

The Robot is controlled from a remote webpage, relying on WebIOPi.

http://webiopi.trouch.com/DOWNLOADS.html

2.1) Install
$ tar xvzf WebIOPi-0.7.1.tar.gz
$ cd WebIOPi-0.7.1
$ sudo ./setup.sh

2.2) Configuration
Edit /etc/webiopi/config to change html page and python script location.

[SCRIPTS]
\# Load custom scripts syntax :
\# name = sourcefile
\#   each sourcefile may have setup, loop and destroy functions and macros
myscript = /home/pi/EduKit3/CamJam-Edukit3/webiopi/python/script.py

et

\# Use doc-root to change default HTML and resource files location
doc-root = /home/pi/EduKit3/CamJam-Edukit3/webiopi/html

2.3) Start
$ sudo webiopi -d -c /etc/webiopi/config

Then, from any internet browser on the network:
http://192.168.1.XX:8000

2.4) Control the robot

- Using the mouse to click on arrow buttons displayed on the webpage
- Using keyboard arrow keys. For this the focus has to be set on html invisible canvas below the buttons.

2.5) Streaming video from the Pi Camera

https://github.com/jacksonliam/mjpg-streamer

$ export LD_LIBRARY_PATH=.
$ ./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so -x 320 -y 240 -fps 15 -ex night"

