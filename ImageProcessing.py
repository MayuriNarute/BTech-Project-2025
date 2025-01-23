import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Paths to the dataset folders
train_dir = 'C:/Users/Administrator/PycharmProjects/Final Year/dataset/train'
val_dir = 'C:/Users/Administrator/PycharmProjects/Final Year/dataset/val'
test_dir = 'C:/Users/Administrator/PycharmProjects/Final Year/dataset/test'

# Image parameters
img_size = (128, 128)  # Resize all images to 128x128
batch_size = 32

# Data augmentation for training and normalization for all sets
train_datagen = ImageDataGenerator(
    rescale=1./255,  # Normalize pixel values between 0 and 1
    rotation_range=20,  # Random rotation
    width_shift_range=0.2,  # Random width shift
    height_shift_range=0.2,  # Random height shift
    shear_range=0.2,  # Shear transformation - different perception angle
    zoom_range=0.2,  # Random zoom
    horizontal_flip=True  # Random horizontal flip
)

val_test_datagen = ImageDataGenerator(rescale=1./255)  # Only normalization

# Loading datasets
train_data = train_datagen.flow_from_directory(
    train_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=True  # Shuffle the data for better training
)

val_data = val_test_datagen.flow_from_directory(
    val_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=False
)

test_data = val_test_datagen.flow_from_directory(
    test_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=False
)
#Leukemia: Basophils, lymphocytes, erythroblasts.
#Lymphoma: Lymphocytes, monocytes.
#Myeloma: Platelets, plasma cells ig- immature granulocytes (lymphocyte-related).

# Print class indices for verification
print("Classes in Training Data:", train_data.class_indices)
print("Classes in Validation Data:", val_data.class_indices)
print("Classes in Test Data:", test_data.class_indices)
