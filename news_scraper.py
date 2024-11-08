import requests
from bs4 import BeautifulSoup
import time

# Step 1: Initial request to get the list of articles
url = "https://www.denverpost.com/sports/denver-broncos/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Extract article URLs from the main page
article_links = []
for article in soup.find_all("article", class_="headline-only"):
    link_tag = article.find("a", class_="article-title")
    if link_tag and link_tag['href']:
        article_links.append(link_tag['href'])


max_scrapes = 2
scrape_counter = 0
# Step 3: Scrape each individual article page for the full content
for article_url in article_links:
    article_response = requests.get(article_url)
    article_soup = BeautifulSoup(article_response.text, "html.parser")

    # Adjust the selector based on the structure of the article page
    paragraphs = article_soup.find_all("p")
    article_text = " ".join([p.get_text() for p in paragraphs])

    print("================================================")
    print("Article URL:", article_url)
    print("Content:", article_text)
    scrape_counter += 1
    if scrape_counter == 2:
        break
   
    
    # Add a delay to avoid overwhelming the server
    time.sleep(1)
