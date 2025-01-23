import os
import shutil
from sklearn.model_selection import train_test_split

# Define paths
dataset_dir = 'C:/Users/B-TECH Project/archive (7)/PBC_dataset_normal_DIB_224'
output_dir = 'C:/Users/Administrator/PycharmProjects/Final Year/dataset'
splits = ['train', 'val', 'test']

# Create output folders
for split in splits:
    os.makedirs(os.path.join(output_dir, split), exist_ok=True)

# Process each class folder
for class_folder in os.listdir(dataset_dir):
    class_path = os.path.join(dataset_dir, class_folder)
    if not os.path.isdir(class_path):
        continue

    images = os.listdir(class_path)
    train, temp = train_test_split(images, test_size=0.3, random_state=42)
    val, test = train_test_split(temp, test_size=0.5, random_state=42)

    for split, split_images in zip(splits, [train, val, test]):
        split_dir = os.path.join(output_dir, split, class_folder)
        os.makedirs(split_dir, exist_ok=True)
        for img in split_images:
            shutil.copy(os.path.join(class_path, img), os.path.join(split_dir, img))
