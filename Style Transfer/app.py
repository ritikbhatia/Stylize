from __future__ import print_function
import os
from flask import Flask, render_template, request, redirect, url_for
from artify import run_model
from detect import run_detect

############### Uploading and Rendering #######################
app = Flask(__name__)
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# static_folder='', static_url_path=''


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/artify')
def upload_file():
    return render_template('upload.html')


# style, content and output overwritten after every model call
# Add upload again button in display_images.html!!
# Account for different image types (png)
# Change epochs back to 300(more?)
@app.route('/artify_perform', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        content = request.files['content']
        style = request.files['style']
        content_img_name = 'content_img.jpg'
        style_img_name = 'style_img.jpg'
        content.save(os.path.join(
            app.config['UPLOAD_FOLDER'], content_img_name))
        style.save(os.path.join(app.config['UPLOAD_FOLDER'], style_img_name))
        run_model()
        # run_detect(content_img_name)
        return render_template('display_images.html', content_image=content_img_name, style_image=style_img_name, output_image="output.jpg")

# JavaScript and CSS not rendering from static folder
# JS and CSS written in script and style tag for now
# That seems to be working
# HOW DO I GET LINK THE FREAKING STATIC FILE?!


@app.route('/detect_perform', methods=['GET', 'POST'])
def detection():
    if request.method == 'POST':
        image = request.files['detect_image']
        image_name = 'detection_image.jpg'
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
        run_detect(image_name)
    return redirect(url_for('detector'))


@app.route('/edit', methods=['GET', 'POST'])
def editor():
    return render_template('image_editing.html')


@app.route('/detect', methods=['GET', 'POST'])
def detector():
    return render_template('detect.html')


if __name__ == '__main__':
    app.run(debug=True)
