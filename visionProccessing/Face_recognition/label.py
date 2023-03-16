from PIL import Image
import os

# Path to the folder containing the images
folder_path = 'Me\Joey'

# Get a list of all the image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]

# Loop through each image file
for i, image_file in enumerate(image_files):
    # Open the image file using Pillow
    image_path = os.path.join(folder_path, image_file)
    image = Image.open(image_path)

    # Create a new file name with the label and extension
    new_file_name = '1_{:03d}.{}'.format(i, image.format.lower())

    # Save the image with the new file name in the same folder
    new_file_path = os.path.join(folder_path, new_file_name)
    image.save(new_file_path)

    # Print the original and new file names for verification
    print('Renamed {} to {}'.format(image_file, new_file_name))