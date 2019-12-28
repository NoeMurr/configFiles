#!/usr/bin/env bash

if pgrep -u $UID -x conky >/dev/null; then # if conky is not active start it
    echo "Killing conky..."
    killall -q conky
    echo "Killed..."
else # kill it
    echo "---" | tee -a /tmp/conky.log

    if [[ $# -lt 1 ]]; then 
        conky -b >> /tmp/conky.log 2>&1 & 
    else
        conky -b -c $1 >> /tmp/conky.log 2>&1 &
    fi

    echo "Conky started..."
fi
