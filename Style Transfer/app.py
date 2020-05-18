import os
from flask import Flask, render_template, request
app = Flask(__name__, static_folder='/')


@app.route('/')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        content = request.files['content']
        style = request.files['style']
        content_img_name = content.filename
        style_img_name = style.filename
        content.save(content_img_name)
        style.save(style_img_name)
        return render_template('display_images.html', content_image=content_img_name, style_image=style_img_name)


if __name__ == '__main__':
    app.run(debug=True)
