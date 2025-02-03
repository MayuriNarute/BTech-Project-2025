'''
This CNN model is for feature extraction from the images like shape,
color, texture,etc.
NOTE : Both h5 & keras formats store the model structure, weights, and training configurations.
'''

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# Image size & number of classes (Leukemia, Lymphoma, Myeloma)
img_size = (128, 128, 3)  # 3 channels (RGB)
num_classes = 3  # Three types of blood cancers

# CNN Model Architecture
model = Sequential([
    # First Convolutional Block
    Conv2D(32, (3, 3), activation='relu', input_shape=img_size),
    MaxPooling2D(pool_size=(2, 2)),

    # Second Convolutional Block
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),

    # Third Convolutional Block
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),

    # Flattening and Fully Connected Layers
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),  # Regularization to prevent overfitting
    Dense(num_classes, activation='softmax')  # Output layer for classification
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Display model summary
model.summary()

# Save model architecture
# model.save("cnn_model.h5")  # ❌ Legacy format

model.save("cnn_model.keras")  # ✅ Recommended format

print("✅ CNN Model created and saved successfully!")
