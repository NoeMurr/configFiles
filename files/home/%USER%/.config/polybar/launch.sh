#!/usr/bin/env sh

## Add this to your wm startup file.

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch bar1 and bar2
#polybar top -c ~/.config/polybar/config-top.ini &
#polybar bottom -c ~/.config/polybar/config-bottom.ini &

for m in `xrandr --query | grep " connected " | cut -d ' ' -f 1`; do
	if xrandr --query | grep "$m" | grep 'primary' > /dev/null; then 
		traypos='right' monitor=$m polybar --reload top -c \
			~/.config/polybar/config-top.ini &
	else 
		monitor=$m polybar --reload top -c \
			~/.config/polybar/config-top.ini &
	fi

	monitor=$m polybar --reload bottom -c  ~/.config/polybar/config-bottom.ini &
done

