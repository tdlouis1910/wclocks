from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import glob
import os
import cv2
import numpy as np
import pandas as pd
import detect_object
from shutil import copyfile
import shutil
from distutils.dir_util import copy_tree

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

from flask_cors import CORS, cross_origin

import requests

from urllib.request import urlopen

# Define a flask app
app = Flask(__name__)

# for f in os.listdir("static\\similar_images\\"):
#   os.remove("static\\similar_images\\"+f)

print('Model loaded. Check http://127.0.0.1:5000/')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        f = request.files['image']
        filename = secure_filename(f.filename)


        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, '/static/uploads', filename)
        f.save(file_path)

        get_detected_object = detect_object.ts_detector(file_path)

    return get_detected_object[1]


@app.route('/api/v1/prediction', methods= ['POST'])
@cross_origin()
def test():

    if request.method == 'POST':
      f = request.files['file']
      # file = f.get('image')
      basepath = os.path.dirname(__file__)

      file_path = os.path.join(basepath, 'static\\uploads', secure_filename(f.filename))

      print(file_path)
      f.save(file_path)   
      get_detected_object = detect_object.ts_detector(file_path)


      return get_detected_object[1]

    return "Unconfirmed Request"


# @app.route('/uploader', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['file']
#         # create a secure filename
#         filename = secure_filename(f.filename)
#         print(filename)
#         # save file to /static/uploads
# #      filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         basepath = os.path.dirname(__file__)

#         file_path = os.path.join(
#             basepath, './static/uploads', secure_filename(f.filename))

#         print(file_path)
#         f.save(file_path)

#         get_detected_object = detect_object.ts_detector(file_path)

#         return render_template("uploaded.html", fname=filename, display_detection=get_detected_object[1])


# @app.route('/predict', methods=['POST'])
# def upload():
#    if request.method == 'POST':
#        # Get the file from post request
#        f = request.files['file']
#
        # Save the file to ./uploads
#        basepath = os.path.dirname(__file__)
#        file_path = os.path.join(
#            basepath, 'uploads', secure_filename(f.filename))
#        f.save(file_path)

        # Make prediction
#       get_detected_object=detect_object(file_path)
#        return get_detected_object
#    return None


if __name__ == '__main__':
    app.run(debug=True)
