import requests
from bs4 import BeautifulSoup
import os

# Set the URL of the website you want to download images from
url = "https://wsp.kbtu.kz/ScheduleTeacherStudent#!ScheduleView/RoomScheduleView/StudentsScheduleView/StudentsScheduleView/"

# Make a request to the website
response = requests.get(url, verify=False)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the image tags
img_tags = soup.find_all('img')

# Create a directory to save the downloaded images
if not os.path.exists('images'):
    os.makedirs('images')

# Download each image and save it to the images directory
for img in img_tags:
    img_url = img.get('src')
    if img_url.startswith('http'):
        response = requests.get(img_url)
        filename = os.path.join('images', img_url.split('/')[-1])
        with open(filename, 'wb') as f:
            f.write(response.content)
            print(f"{filename} downloaded successfully!")
