sudo apt update && apt upgrade
sudo apt install git
git clone https://github.com/Tech08mag/AR.git
ls -l
cd AR
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
#python3 /helpers/install.py
flask run -h raspberrypi.local 
# or use the IP 