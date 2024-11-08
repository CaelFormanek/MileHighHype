import requests
from bs4 import BeautifulSoup

# Making a GET request to the page
r = requests.get('https://www.milehighreport.com/2024/11/7/24290075/broncos-vs-chiefs-3-keys-to-game')

# Parsing the HTML, this is the raw content
soup = BeautifulSoup(r.content, 'html.parser')

# Find the main content div with class 'c-entry-content'
main_content = soup.find('div', class_='c-entry-content')

# If the div is found, extract and print the text from paragraphs and headings
if main_content:
    # Find all paragraphs and headings inside the div
    content = main_content.find_all(['p', 'h2', 'h3', 'h4'])  # Add more tags if needed
    
    # Loop through and print the text of each element
    for element in content:
        print(element.text.strip())  # Strip any extra whitespace
else:
    print("Content not found")
