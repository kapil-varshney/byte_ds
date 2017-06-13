#!/usr/bin/env python3

from flask import Flask, render_template


app = Flask(__name__)

#
@app.router('/')
def index():
    return render_template('index.html')

#
@app.route('/movies/bahubali-part-<int:i>')
def movies(i):
    return render_template('bahubali-part-2.html')


if __name__=='__main__':
