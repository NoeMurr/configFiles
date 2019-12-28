#!/usr/bin/env bash

if [ -x `command -v feh` ] &&\
   [ -f `cat ~/.i3_bg` ]; 
then 
    feh --bg-fill `cat ~/.i3_bg`
    echo 'bg changed'
    exit 0
fi

[ ! -x `command -v feh` ] && echo "command feh not found"
[ ! -f `cat ~/.i3_bg` ] && echo "bg image not found"

