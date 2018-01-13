#!/bin/bash
export DISPLAY=:0
while true; do nc -l 8000 | mplayer -fps 50 -cache 512 -; done

