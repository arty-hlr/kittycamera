from flask import Flask, flash, render_template, Response, redirect, request, session
import os
from pantilthat import *
app = Flask(__name__)
app.secret_key = os.urandom(12)
import credentials

@app.route('/')
def index():
    # Login page
    if not session.get('logged_in'):
        return render_template('login.html')
    # Video streaming home page
    else:
        return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] == credentials.username and request.form['password'] == credentials.password:
        session['logged_in'] = True
    else:
        flash('Wrong Credentials!')
    return index()     

@app.route('/video_stream')
def video_stream():
    return redirect('http://kitty_watcher:QH9SJHJH5D6H4CJH7D5H4HKC@www.kittycamera.live:8081')

@app.route('/pan_left')
def pan_left():
    cur = get_pan()
    pan(cur+10)
    return (''), 204

@app.route('/pan_right')
def pan_right():
    cur = get_pan()
    pan(cur-10)
    return (''), 204

@app.route('/pan_zero')
def pan_zero():
    pan(0)
    return (''), 204

@app.route('/tilt_down')
def tilt_down():
    cur = get_tilt()
    tilt(cur+10)
    return (''), 204

@app.route('/tilt_up')
def tilt_up():
    cur = get_tilt()
    tilt(cur-10)
    return (''), 204

@app.route('/tilt_zero')
def tilt_zero():
    tilt(0)
    return (''), 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True, threaded=True)

