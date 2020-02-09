# flask-vlc

Minimal, single-threaded flask app to play video and display messages on a screen with VLC.

Ideal for a Raspi remote-controlled screen.

## Usage

```sh
export VLC_PATH=/usr/bin/vlc
python3 server.py
```

## HTTP Commands

```sh

# Play some local video
curl "http://127.0.0.1:5000/play/local.mp4"

# Play some remote video
curl "http://127.0.0.1:5000/play/http://techslides.com/demos/sample-videos/small.mp4"

# Show a text message
curl "http://127.0.0.1:5000/text/hello%20world%200x0001F607?color=0xff0000&duration=5"

```

⚠ Be sure to url encode the text message

## Raspi setup

### Create the SD card

Utiliser Raspbian Desktop https://www.raspberrypi.org/downloads/raspbian
Login : pi / raspberry

- Activer ssh en créant un fichier `.ssh` à la racine
- Installer le service VNC
- Disable toolbar and screensaver in `/etc/xdg/lxsession/LXDE-pi/autostart`

```
venv .venv
sh ./.venv/bin/activate
python3 -m pip install -r requirements.txt
python3 server.py

```

```

```
