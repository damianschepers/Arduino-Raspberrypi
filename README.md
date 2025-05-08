# AR
Material 

Aduino: 

Aduino 2560 MEGA 

LCD Display 

Aduino Kabel 

 

 

Raspberry Pi 3B+ 

Raspberry Pi Netzteil 

SD Karte (mindestens 16GB) 

SD Kartenlesegerät 

Raspberry Pi Imager1  

 

 

 

 

 

  

 

 

Pi flashen 

    Lade dir den Raspberry Pi Imager2 herunter 

    Stecke deine SD Karte in deinen PC 

    Starte den Raspberry Pi Imager. Das Fenster sollte wie folgt aussehen: 

    Bei „Choose Device“ muss man die SD Karte als Medium auswählen  

    Bei „Choose OS“ muss man auf other gehen und dort die Lite Version auswählen 

    Flashen rausnehmen und in den Raspberry Pi stecken. 

Aufbau 

 

Passwort/Login/Verbindungen 

SSH 

SSH ermöglicht die Verbindungen von einem PC zu einem anderen verbinden. Dies gelingt mit folgendem Befehl: 

ssh username@hostname 

dieser wird ins Terminal bzw dem cmd eingegeben. Falls die IP des Raspberrypi’s bekannt ist, kann der hostname dadurch ersetzt werden. Im Folgenden muss man dann sein oben gesetztes Passwort eingeben. 

 

 

 

Installation 

Ziel: 

Code von GitHub auf den Raspberry PI 3 B+ ziehen 

    Raspberry Pi updaten 

sudo apt update && apt upgrade 

 

    Git installieren 

sudo apt install git 

 

    Das Repository clonen 

git clone https://github.com/Tech08mag/AR.git 

    Authentifiziere dich mit deinem GitHub Account (Hierfür musst man einen Authentifizierungstoken angelegt haben und diesen bei Aufforderung eingeben 

    Nun kann man: 

ls -l 

    ins terminal eingeben. Wenn man eine Rückgabe bekommt, war das clonen des Repositorys erfolgreich. 

    Mit dem folgendem Command geht man in den Ordner “AR”, in dem sich das Projekt befindet 

cd AR 

 

    Nun gibt es zwei Möglichkeiten die Dependencies zu installieren: 

    Durch ein virtual Environment, welches sich wie folgt erstellen lässt: 

python3 -m venv .venv 

 

und wird wie folgt aktiviert: 

source .venv/bin/activate 

 

und hiermit werden die Dependencies installiert: 

python3 -m pip install -r requirements.txt 

 

 

Dieser Vorgang kann einige Zeit in Anspruch nehmen... 

 

    Dies ist nur eine Notlösung. Bei dieser Installationsmethode könnte dein System crashen und ist nicht zu empfehlen. 

python3 /helpers/install.py 

(Notiz: unter Windows kann diese Installationsmethode ohne Bedenken durchgeführt werden)  

 

    Nun kann der Webserver gestartet werden: 

flask run -h raspberrypi.local 

    Öffne einen Browser deiner Wahl und stelle sicher, dass der Raspberry Pi und dein Gerät sich im selben WLAN befinden. Wenn beides zutrifft, kannst du im Browser http://raspberrypi.local:5000/ öffnen. 

    Hiermit hast du das Webinterface geöffnet und den Webserver gestartet. 

Arduino  

Web 

HTML 

CSS 

Code erklären 

 

dieser wird ins Terminal bzw dem cmd eingegeben. Falls die IP des Raspberrypi’s bekannt ist, kann der hostname dadurch ersetzt werden. Im folgenden muss man dann sein oben gesetztes Passwort eingeben. 

 

Die Limitierungen der Schule 

 

 

 

 

 

Nützliche Software  

Github3 

Git4 

Visual Studio Code5 

Raspberry Pi Imager6  

 

 

 

 

 

 

 

 

 

 

Quellen 

https://stackoverflow.com/questions/43069780/how-to-create-virtual-env-with-python-3  

https://stackoverflow.com/questions/76057643/passing-values-from-html-form-to-python-flask  

https://medium.com/@gitauharrison/build-a-tag-system-in-your-flask-blog-app-f7d9b915fc1  

https://www.w3schools.com/python/python_file_write.asp 

https://stackoverflow.com/questions/13279399/how-to-obtain-values-of-request-variables-using-python-and-flask  

https://stackoverflow.com/questions/20689195/flask-error-method-not-allowed-the-method-is-not-allowed-for-the-requested-url  

https://www.w3schools.com/python/python_lists_sort.asp 

https://blog.teclado.com/flashing-messages-with-flask/  

https://roboticsbackend.com/raspberry-pi-arduino-serial-communication/  

 