from flask import Flask
from flask import render_template
from flask import request
from random import sample
import json
import os

app = Flask(__name__)
app.n_image = 5  # Images to display for liking /disliking
app.img_root = 'static/images'
app.image_names = map(lambda img_name: os.path.join(app.img_root, img_name),
                      os.listdir(app.img_root))


def image_draw(n=app.n_image):
    return sample(app.image_names, n)

@app.route('/')
def index():
    sample_image_names = image_draw()
    return render_template('index.html', sample_image_names=sample_image_names)

@app.route('/process_images', methods=['POST'])
def process_images():
    data = request.json
    like_lst, dislike_lst = data

    ####  random model  ###
    random_images = image_draw(10)
    #####################

    return json.dumps(random_images)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
