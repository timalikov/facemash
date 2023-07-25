import requests
from bs4 import BeautifulSoup

# Set the path to the text file containing the links
filename = 'links.txt'

# Read the links from the text file
with open(filename, 'r') as f:
    links = f.readlines()

# Loop through each link and make a request
for link in links:
    # Clean up the link by removing any whitespace and newline characters
    link = link.strip()

    # Make a GET request to the URL
    response = requests.get(link, verify=False)
    

    # Parse the content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Do something with the parsed content, e.g. extract text, images, etc.
    # ...

    # Print a message to indicate that the link has been visited
    print(f'{link} visited successfully.')
