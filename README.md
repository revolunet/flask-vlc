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
curl "http://127.0.0.1:5000/text/hello%20world?color=0xff0000&duration=5"

```

⚠ Be sure to url encode the text message

## Security

Anyone with access to this API can control the screen or execute random command on the player.

You need to secure your network or access to this device via iptables or your preferred filtering mechanism.

## Raspi setup

### Create the SD card

Utiliser Raspbian Desktop https://www.raspberrypi.org/downloads/raspbian
Login : pi / raspberry

- Activer ssh en créant un fichier `.ssh` à la racine

#### Au 1er démarrage :

- Mettre le hostname à "video"
- [Désactiver le pointeur souris](https://raspberrypi.stackexchange.com/a/10415)

#### /etc/xdg/lxsession/LXDE-pi/autostart

```
@/usr/bin/pqiv -f -i /home/pi/wallpaper.png
@/usr/bin/python3 /home/pi/flask-vlc/server.py
```

### Cloner le projet dans /home/pi/flask-vlc

```
git clone https://github.com/revolunet/flask-vlc
cd flask-vlc
python3 -m pip install -r requirements.txt
```

Au prochain reboot, le serveur sera dispo sur `http://video.local:5000/`

