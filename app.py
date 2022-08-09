from concurrent.futures import thread
from flask import Flask, render_template, request, Response, redirect, send_file
import os
from os import remove
import pafy
import moviepy.editor as mp
from pytube import YouTube

app = Flask(__name__)
path = os.getcwd() + "/output/"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/envia', methods=['GET', 'POST'])
def envia():
    if request.method == 'POST':
        url = request.form['url']
        yt = YouTube(url)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(path)
    return 'Download Complete...'
    

@app.route('/envia2', methods=['GET', 'POST'])
def envia2():
    if request.method == 'POST':
        url = request.form['url']
        yt = YouTube(url)
        yt.streams.filter(progressive=True, file_extension='mp3').order_by('resolution').desc().first().download(path)
    
    # send_file(p, as_attachment=True)
    return 'Download Complete...'

if __name__ == '__main__':
    app.run(port=1234, threaded=True)