#!/usr/bin/env bash

# check if I'm using nvidia card
if [[ `prime-select query` == 'nvidia' ]]; then
	compton -b
fi

