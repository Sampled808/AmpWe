#!/bin/bash

#handle keyboard interrupt
catch_int(){
	echo -e "\n\n stopping"
	killall qjackctl
	exit
}

trap catch_int SIGINT
trap catch_int SIGTSTP

# changes errors
# jackd -R -d alsa -d hw:0,3 & > err_jackd
# idk what it does, new sollution is to start jack server:
killall qjackctl
qjackctl -s
# start test server
./testserver.py 2> err_server &

# start recordeing
./record_linux.py
