from bs4 import BeautifulSoup

# Set the path to the text file containing the HTML content
filename = 'links.txt'

# Read the HTML content from the text file
with open(filename, 'rb') as f:
    html_content = f.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the <img> tags and extract their 'src' attribute values
img_links = [img_tag['src'] for img_tag in soup.find_all('img')]

# Print the list of image links)
for i in img_links:
    print(i)
