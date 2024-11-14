# Mile High Hype™

## Purpose
This app is a passion project built by Cael Formanek (me) to bring Colorado sports into one place. Using web scraping and AI interpretation, the app is able to grab information from top Colorado sports news outlets and present them to the user. This is not meant for use by other customers, but is a way for me to get my news on my favorite teams conveniently.

### To get started
1st time: source setup.sh <br>
nth time: source venv/bin/activate <br>
to deactivate venv: deactivate <br>

### Running the MongoDB Database
create a mongo image with Docker: docker pull mongo <br>
run a database called sportsnews: docker run --name sportsnews -d -p 27017:27017 mongo <br>


### Web news sources
Broncos: https://www.denverpost.com/sports/nfl/denver-broncos/ <br>
Nuggets: https://www.denverpost.com/sports/nba/denver-nuggets/ <br>
Avalanche: https://www.denverpost.com/sports/nhl/colorado-avalanche/ <br> 
Rockies: https://www.denverpost.com/sports/mlb/colorado-rockies/ <br>

