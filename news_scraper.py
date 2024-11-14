import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import time

# function for scraping Broncos news
def scrapeDenverPostNews(numberOfArticles, url):
    # Step 1: Initial request to get the list of articles
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)
    # return
    # Step 2: Extract article URLs from the main page
    article_links = []
    for article in soup.find_all("article", class_="headline-only",):
        link_tag = article.find("a", class_="article-title")
        if link_tag and link_tag['href']:
            article_links.append(link_tag['href'])

    # determines number of scrapes
    scrape_counter = 0

    # holds all article content
    soups = []
    # Step 3: Scrape each individual article page for the full content
    for article_url in article_links:
        article_response = requests.get(article_url)
        article_soup = BeautifulSoup(article_response.text, "html.parser")
  
        # Adjust the selector based on the structure of the article page
        paragraphs = article_soup.find_all("p")
        article_text = " ".join([p.get_text() for p in paragraphs])
        soups.append(article_text)
        # print("======================================================================")
        # print("Article URL:", article_url)
        # print("Content:", article_text)

        # Stop at the desired number of articles
        scrape_counter += 1
        if scrape_counter == numberOfArticles:
            break
        
        # Add a delay to avoid overwhelming the server
        time.sleep(1)
    return soups

# function to add news to the database
def addNewsToDatabase(news, databaseURL):
    # Connect to the MongoDB database
    client = MongoClient(databaseURL)

    # Select the database
    db = client['sportsnews']

    # Select the collection within the database (replace 'news' with your collection name)
    collection = db['news']

    # Insert the news data into the collection
    result = collection.insert_one(news)

    return result.inserted_id  # Return the ID of the inserted document

# function to clear all data from a database collection
def clearCollection(databaseURL, collectionName):
    # Connect to the MongoDB database
    client = MongoClient(databaseURL)

    # Select the database
    db = client['sportsnews']

    # Select the collection
    collection = db[collectionName]

    # Delete all documents in the collection
    result = collection.delete_many({})

    print(f"Deleted {result.deleted_count} documents from the {collectionName} collection.")

# main block
if __name__ == "__main__":
    # scrapeDenverPostNews(2, "https://www.denverpost.com/sports/nfl/denver-broncos/")
    # scrapeDenverPostNews(2, "https://www.denverpost.com/sports/nba/denver-nuggets/")
    # scrapeDenverPostNews(2, "https://www.denverpost.com/sports/nhl/colorado-avalanche/")
    # scrapeDenverPostNews(2, "https://www.denverpost.com/sports/mlb/colorado-rockies/")
    # news_data = {
    # 'title': 'Broncos Win Game',
    # 'date': '2024-11-13',
    # 'content': 'The Denver Broncos won their latest game...',
    # 'team': 'Broncos'
    # }

    # databaseURL = 'mongodb://localhost:27017'

    # news_id = addNewsToDatabase(news_data, databaseURL)

    # print(f"News inserted with ID: {news_id}")
    databaseURL = 'mongodb://localhost:27017'
    clearCollection(databaseURL, 'news')
