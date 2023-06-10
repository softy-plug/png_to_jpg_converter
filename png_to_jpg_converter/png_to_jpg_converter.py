import os
from PIL import Image

# Prompt user for folders
png_folder = input('Enter the folder with png images: ')
jpg_folder = input('Enter folder to save converted jpg images: ')

# Check if folders exists, else create them
if not os.path.exists(jpg_folder):
    os.makedirs(jpg_folder)

# Loop through all files in the png folder
for file_name in os.listdir(png_folder):
    if file_name.endswith('.png'):
        # Open png image and convert to RGB
        png_image = Image.open(os.path.join(png_folder, file_name))
        png_image = png_image.convert('RGB')

        # Create new jpg file name
        jpg_file_name = os.path.splitext(file_name)[0] + '.jpg'
        jpg_file_path = os.path.join(jpg_folder, jpg_file_name)

        # Save jpg image with maximum quality
        jpg_image = png_image.save(jpg_file_path, 'JPEG', quality=100)

print('All png images in {} converted to jpg and saved in {}.'.format(png_folder, jpg_folder))

# softy_plug