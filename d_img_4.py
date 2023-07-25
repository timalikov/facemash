import os
import requests
from bs4 import BeautifulSoup

# Set the path to the text file containing the HTML content
filename = 'links.txt'

# Set the path to the folder where you want to save the images
folder_path = 'images'

# Create the folder if it does not exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Read the HTML content from the text file
with open(filename, 'rb') as f:
    html_content = f.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the <img> tags
img_tags = soup.find_all('img')

# Loop through each <img> tag and download the image
for i, img_tag in enumerate(img_tags):
    # Extract the value of the 'src' attribute
    src = img_tag.get('src')

    # Make a request to download the image
    response = requests.get(src, verify=False)

    # Generate a unique file name for the image
    file_name = f'image_{i+1}.jpg'

    # Set the path to save the image
    file_path = os.path.join(folder_path, file_name)

    # Save the image to the specified location
    with open(file_path, 'wb') as f:
        f.write(response.content)

    print(f'{src} downloaded successfully.')

print('All images downloaded successfully.')
