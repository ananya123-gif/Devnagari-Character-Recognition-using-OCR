import os
import numpy as np
import cv2
import tensorflow as tf
# Flask utils
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

# Define a flask app
app = Flask(__name__, template_folder='templates')

# Model saved with Keras model.save()
Model_Path = 'HindiModel1.h5'

# Load your trained model
model = tf.keras.models.load_model(Model_Path, custom_objects={'tf': tf})


def model_predict(img_path, model):
    image = cv2.imread(img_path, 0)/255
    image = np.asarray(image)
    img = cv2.resize(image, (32, 32))
    img = np.asarray(img)
    # Preprocessing the image
    x = np.expand_dims(img, axis=0)
    preds = model.predict(x)
    output = np.argmax(preds, axis=1)
    if output == 0:
        return "character is ञ"
    elif output == 1:
        return "character is ट"
    elif output == 2:
        return "character is ठ"
    elif output == 3:
        return "character is ड"
    elif output == 4:
        return "character is ढ"
    elif output == 5:
        return "character is ण"
    elif output == 6:
        return "character is त"
    elif output == 7:
        return "character is थ"
    elif output == 8:
        return "character is द"
    elif output == 9:
        return "character is ध"
    elif output == 10:
        return "character is क"
    elif output == 11:
        return "character is न"
    elif output == 12:
        return "character is प"
    elif output == 13:
        return "character is फ"
    elif output == 14:
        return "character is ब"
    elif output == 15:
        return "character is भ"
    elif output == 16:
        return "character is म"
    elif output == 17:
        return "character is य"
    elif output == 18:
        return "character is र"
    elif output == 19:
        return "character is ल"
    elif output == 20:
        return "character is व"
    elif output == 21:
        return "character is ख"
    elif output == 22:
        return "character is श"
    elif output == 23:
        return "character is ष"
    elif output == 24:
        return "character is स"
    elif output == 25:
        return "character is ह"
    elif output == 26:
        return "character is क्ष"
    elif output == 27:
        return "character is त्र"
    elif output == 28:
        return "character is ज्ञ"
    elif output == 29:
        return "character is ग"
    elif output == 30:
        return "character is घ"
    elif output == 31:
        return "character is ङ"
    elif output == 32:
        return "character is च"
    elif output == 33:
        return "character is छ"
    elif output == 34:
        return "character is ज"
    elif output == 35:
        return "character is झ"
    elif output == 36:
        return "character is 0"
    elif output == 37:
        return "character is १"
    elif output == 38:
        return "character is २"
    elif output == 39:
        return "character is ३"
    elif output == 40:
        return "character is ४"
    elif output == 41:
        return "character is ५"
    elif output == 42:
        return "character is ६"
    elif output == 43:
        return "character is ७"
    elif output == 44:
        return "character is ८"
    elif output == 45:
        return "character is ९"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/working')
def working():
    return render_template('working.html')

@app.route('/process_image', methods=['GET','POST'])
def process_image():
    if request.method=='POST':
    # get the uploaded file
        file = request.files['image']
        # save the file to a temporary location
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(file.filename))
        file.save(file_path)
        processed_img = model_predict(file_path, model)
        # return the processed image
        return render_template('home.html', processed_img=processed_img)


if __name__ == '__main__':
    p = model_predict(r'C:\FLASK\9.png', model)
    app.run(debug=True)
