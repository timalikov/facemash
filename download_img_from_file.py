from bs4 import BeautifulSoup
from selenium import webdriver

# Set the path to the text file containing the HTML script
filename = "links.txt"

# Read the HTML script from the text file
with open(filename, 'r') as f:
    html = f.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all the image tags
img_tags = soup.find_all('img')

# Set up a selenium webdriver
driver = webdriver.Chrome()

# Loop through each image tag
for img_tag in img_tags:
    # Get the image source URL
    img_src = img_tag.get('src')

    # Navigate to the image source URL using selenium
    driver.get(img_src)
    print(f"Clicked image at {img_src}")

# Close the selenium webdriver
driver.quit()
