import os
import sys
import subprocess
from pathlib import Path

if os.getenv("VLC_PATH"):
    VLC_PATH = os.getenv("VLC_PATH")
else:
    if sys.platform == "darwin":
        VLC_PATH = "/Applications/VLC.app/Contents/MacOS/VLC"
    else:
        VLC_PATH = "/usr/bin/vlc"
    if not os.path.isfile(VLC_PATH):
        VLC_PATH = "vlc"

black_path = path.join(Path().absolute(), "black.png")

default_vlc_params = [
    VLC_PATH,
    "-vvv",
    "--video-on-top",
    "--fullscreen",
    "--no-video-title-show",
]

if sys.platform != "darwin":
  default_vlc_params.append("--intf")
  default_vlc_params.append("dummy")

def marquee(message, color, position):
    return (
        'marq{marquee="' + message + '",color=' + color + ",position=" + position + "}"
    )

def vlc_play(url):
    subprocess.call(
        [*default_vlc_params, url, "vlc://quit",]
    )

def vlc_text(message, color="0x00FF00", position="0", duration="10"):
    subprocess.call(
        [
            *default_vlc_params,
            "--image-duration",
            duration,
            "--sub-source",
            marquee(message, color, position),
            black_path,
            "vlc://quit",
        ]
    )