from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import os
import shutil
import subprocess

app = Flask(__name__)
CORS(app)

# Load trained CNN model
model = tf.keras.models.load_model("cnn_model_best.keras")

# Class labels used during training
class_labels = ['Leukemia', 'Lymphoma', 'Myeloma', 'Acute Lymphoblastic Leukemia',
                'Acute Myeloid Leukemia', 'Chronic Myeloid Leukemia',
                'Hodgkin Lymphoma', 'Non-Hodgkin Lymphoma']


def preprocess_image(image_path, target_size=(128, 128)):
    img = load_img(image_path, target_size=target_size)
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']

    # Step 1: Save to uploads/
    uploaded_path = 'static/uploads/uploaded_image.jpg'
    file.save(uploaded_path)

    # Step 2: Copy to ESRGAN input folder (LR/)
    esrgan_input = 'ESRGAN_Model/LR/temp.jpg'
    shutil.copy(uploaded_path, esrgan_input)

    # Step 3: Run ESRGAN enhancement via subprocess
    subprocess.run(["python", "ESRGAN_Model/test.py"], check=True)

    # Step 4: Move output image to static/enhanced/
    enhanced_image_path = 'static/enhanced/enhanced_image.jpg'

    # Step 5: Preprocess enhanced image for prediction
    preprocessed_image = preprocess_image(enhanced_image_path)
    predictions = model.predict(preprocessed_image)[0]

    predicted_index = np.argmax(predictions)
    predicted_class = class_labels[predicted_index]

    result = {
        "predicted_class": predicted_class,
        "probability_scores": {label: float(f"{score * 100:.2f}") for label, score in zip(class_labels, predictions)},
        "original_image": uploaded_path,
        "enhanced_image": enhanced_image_path
    }

    return jsonify(result)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
