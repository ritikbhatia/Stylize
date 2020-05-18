from __future__ import print_function
import os
import copy
import torchvision.models as models
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
from PIL import Image
import torch.optim as optim
import torch.nn.functional as F
import torch.nn as nn
import torch
from flask import Flask, render_template, request, redirect, url_for
from model import run_model

############### Uploading and Rendering #######################
app = Flask(__name__, static_folder='')


@app.route('/')
def upload_file():
    return render_template('upload.html')

# url to redirect back to home
# @app.route('/home')
# def redirect_home():
#     return redirect(url_for('/'))


# style, content and output overwritten after every model call
# Add upload again button in display_images.html
# Account for different image types (png)
# Change epochs back to 300
@app.route('/uploader', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        content = request.files['content']
        style = request.files['style']
        content_img_name = 'content_img.jpg'
        style_img_name = 'style_img.jpg'
        content.save(content_img_name)
        style.save(style_img_name)
        run_model()
        return render_template('display_images.html', content_image=content_img_name, style_image=style_img_name, output_image="output.jpg")


if __name__ == '__main__':
    app.run(debug=True)
