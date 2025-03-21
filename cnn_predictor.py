import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load trained CNN model
model = tf.keras.models.load_model("cnn_model_best.keras")

# Class labels used during training
class_labels = ['Leukemia', 'Lymphoma', 'Myeloma','Acute Lymphoblastic Leukemia','Acute Myeloid Leukemia','Chronic Myeloid Leukemia','Hodgkin Lymphoma','Non-Hodgkin Lymphoma']

# Function to preprocess input image
def preprocess_image(image_path, target_size=(128, 128)):
    img = load_img(image_path, target_size=target_size)
    img_array = img_to_array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Function to predict cancer type with probabilities
def predict_with_probabilities(image_path):
    preprocessed_image = preprocess_image(image_path)
    predictions = model.predict(preprocessed_image)[0]  # Get softmax output

    # Get the highest probability class
    predicted_index = np.argmax(predictions)
    predicted_class = class_labels[predicted_index]

    # Print probability scores
    print("Probability Scores:")
    for label, score in zip(class_labels, predictions):
        print(f"{label}: {score * 100:.2f}%")

    return predicted_class, predictions

# Example usage
if __name__ == "__main__":
    test_image_path = "C:/Users/Administrator/PycharmProjects/Final Year/dataset/test/basophil/BA_77980.jpg"
    predicted_class, probability_scores = predict_with_probabilities(test_image_path)

    print(f"Predicted Cancer Type: {predicted_class}")
