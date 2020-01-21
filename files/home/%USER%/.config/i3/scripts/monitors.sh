#!/usr/bin/env bash

if [[ `prime-select query` == 'nvidia' ]]; then
	if [[ `cat ~/.monitor-pos` == 'left' ]]; then
		xrandr --output HDMI-0 --auto --left-of eDP-1-1
	else
		xrandr --output HDMI-0 --auto --right-of eDP-1-1
	fi
	xrandr --output eDP-1-1 --primary
	if [ -f ~/.fehbg ]; then
		~/.fehbg
	fi
fi

