#!/usr/bin/env python2.7
#-*- coding:utf-8 -*-

from flask import Flask, request, url_for, redirect, make_response
app = Flask(__name__)


@app.route('/')
def index():
    return "<h1 style='text-align:center;'>Dev À Toc !</h1>"


if __name__ == '__main__':
    app.run(debug=True)
