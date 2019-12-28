import os
import subprocess

cmd = "playerctl play-pause"
os.system(cmd)

status = subprocess.check_output("playerctl status") 
if status == "Paused":
    print("")
else:
    print("")

