import cv2
import os
import numpy as np

# Path to the dataset of face images
path = 'Me\Joey'

# Function to read the face images and labels
def read_images(path):
    face_images = []
    labels = []

    for filename in os.listdir(path):
        if filename.startswith('.'):
            continue
        img = cv2.imread(os.path.join(path, filename), cv2.IMREAD_GRAYSCALE)
        face_images.append(img)
        label = int(filename.split('_')[0]) # Assumes label is in the format "label_number"
        labels.append(label)

    return face_images, np.array(labels)

# Load the face images and labels
face_images, labels = read_images(path)

# Create the LBPH recognizer object
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Train the recognizer on the face images and labels
recognizer.train(face_images, labels)

# Save the trained model to disk
recognizer.save('face_recognizer.yml')