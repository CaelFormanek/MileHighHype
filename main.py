import requests
from news_scraper import scrapeDenverPostNews
import re

# Define the API URL
api_url = "http://127.0.0.1:8000/api/news/"

# Define the team URLs you want to scrape
team_urls = {
    "Broncos": "https://www.denverpost.com/sports/nfl/denver-broncos/",
    "Nuggets": "https://www.denverpost.com/sports/nba/denver-nuggets/",
    "Avalanche": "https://www.denverpost.com/sports/nhl/colorado-avalanche/",
    "Rockies": "https://www.denverpost.com/sports/mlb/colorado-rockies/"
}

# Function to post news article to the database
def post_to_api(news_data):
    response = requests.post(api_url, json=news_data)
    if response.status_code == 201:
        print(f"News posted successfully: {news_data['title']}")
    else:
        print(f"Failed to post news: {response.status_code}")

# Main method to scrape and post news for each team
def main():
    # Loop through each team and scrape one article
    for team, url in team_urls.items():
        print(f"Scraping {team} news...")
        
        # Scrape one article for the team
        articles = scrapeDenverPostNews(2, url)  # Scrape one article
        if articles:
            # Clean the article content by removing unwanted text
            clean_content = articles[1]

            # Remove specific unwanted phrases
            unwanted_phrases = [
                "Digital Replica Edition",
                "Sign up for Newsletters and Alerts",
            ]
            for phrase in unwanted_phrases:
                print("removed " + phrase)
                clean_content = clean_content.replace(phrase, '')


            # Prepare the data to post to the API
            news_data = {
                'title': f"{team} News",  # Customize based on the article
                'date': '2024-11-21',  # You could extract the date if available
                'content': clean_content,  # The scraped article text
                'team': team
            }
            
            # Post the article to the API
            post_to_api(news_data)
        else:
            print(f"No articles found for {team}")

# Run the main function
if __name__ == "__main__":
    main()
