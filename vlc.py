import os
import sys
import subprocess

if os.getenv("VLC_PATH"):
    VLC_PATH = os.getenv("VLC_PATH")
else:
    if sys.platform == "darwin":
        VLC_PATH = "/Applications/VLC.app/Contents/MacOS/VLC"
    else:
        VLC_PATH = "/usr/bin/vlc"
    if not os.path.isfile(VLC_PATH):
        VLC_PATH = "vlc"

black_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "black.png")

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

def vlc_kill():
    subprocess.call(
        ["pkill", "vlc"]
    )

def vlc_play(url):
    vlc_kill()
    subprocess.call(
        [*default_vlc_params, url, "vlc://quit",]
    )

def vlc_text(message, color="0x00FF00", position="0", duration="10"):
    vlc_kill()
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