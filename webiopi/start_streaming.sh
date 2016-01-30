#!/bin/bash

MJPEG_STREAMER_PATH=/home/pi/Downloads/mjpeg-streamer/mjpg-streamer/mjpg-streamer-experimental/

export LD_LIBRARY_PATH=$MJPEG_STREAMER_PATH

$MJPEG_STREAMER_PATH/mjpg_streamer -o "output_http.so -w $MJPEG_STREAMER_PATH/www" -i "input_raspicam.so -x 320 -y 240 -fps 25 -ex night -vf" 
