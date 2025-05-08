# importing Flask and other modules
from flask import Flask, request, render_template, flash, redirect, url_for
import serial
import time


# Flask constructor
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['TESTING'] = True
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)

def send_data_to_arduino(data: int):    
    ser.write(str(data + "\n").encode('utf-8'))
    time.sleep(0.1)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/', methods = ["POST"])
def login():
    if request.method == "POST":
        username =  request.form.get('user')
        password =  request.form.get('psswrd')
        if username == "admin" and password == "admin":
            flash("You were successfully logged in!")
            return redirect(url_for('led'))
        else:
          flash("Invalid credentials")
          return redirect(url_for('home'))
        
@app.route('/led', methods = ["GET", "POST"])
def led():
  if request.method == "POST":
    send_data_to_arduino("100")
    checkbox = request.form.getlist('checkbx')
    if checkbox != "":
      for i in checkbox:
        send_data_to_arduino(i)
      flash("Daten wurden gesendet!")
      return redirect(url_for('led'))
    else:
      flash("An error has occurred!")
      return redirect(url_for('home'))
      
  return render_template('led.html')


if __name__=='__main__':
   app.run(host='0.0.0.0')