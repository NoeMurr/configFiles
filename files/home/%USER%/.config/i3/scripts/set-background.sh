#!/usr/bin/env bash

[ ! -x `command -v feh` ] && echo "command feh not found" && exit -1;

if [ $# -eq 0 ]; then
	
	[ ! -f `cat ~/.i3_bg` ] && echo "bg image not found" && exit -1

    feh --bg-fill `cat ~/.i3_bg`
	echo 'bg changed'
    exit 0
else
	[ ! -f "$1" ] && echo "The file $1 does not exists" && exit -1

	if ! (file "$1" | grep -qE "image|bitmap"); then
		echo "the file is not an image"
		exit -1
	else
		echo "$1" > ~/.i3_bg
		feh --bg-fill `cat ~/.i3_bg`
		exit 0
	fi
fi

