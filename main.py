import requests
from news_scraper import scrapeDenverPostNews

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
        articles = scrapeDenverPostNews(1, url)  # Scrape one article
        if articles:
            # Prepare the data to post to the API
            news_data = {
                'title': f"{team} Victory",  # Customize based on the article
                'date': '2024-11-13',  # You could extract the date if available
                'content': articles[0],  # The scraped article text
                'team': team
            }
            
            # Post the article to the API
            post_to_api(news_data)
        else:
            print(f"No articles found for {team}")

# Run the main function
if __name__ == "__main__":
    main()
