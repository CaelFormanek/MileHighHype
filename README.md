# Mile High Hype™

## Purpose
This app is a passion project built by Cael Formanek (me) to bring Colorado sports into one place. Using web scraping and APIs, the app is able to grab information from top Colorado sports news outlets and present them to the user. This is not meant for use by other customers, but is a way for me to get my news on my favorite teams conveniently.

### TODO:
1. Make it so main.py will replace current news entries with ones being scraped
2. Create frontend
3. Make script to replace news every 3 hours

### To get started
1st time: source setup.sh <br>
nth time: source venv/bin/activate <br>
to deactivate venv: deactivate <br>

### Running the MongoDB Database
create a mongo image with Docker: docker pull mongo <br>
run a database called sportsnews: docker run --name sportsnews -d -p 27017:27017 mongo <br>

### Managing the API
Before running 1st time/ On Changes: 
python manage.py makemigrations <br>
python manage.py migrate <br>

To run: python manage.py runserver <br>
To quit: control+c

### Testing the API
curl http://127.0.0.1:8000/api/news/ <br>
curl -X DELETE http://127.0.0.1:8000/api/news/ <br>
curl -X POST -H "Content-Type: application/json" -d '{
    "title": "Broncos Victory",
    "date": "2024-11-13",
    "content": "The Broncos secured a historic win...",
    "team": "Broncos"
}' http://127.0.0.1:8000/api/news/ <br>
curl -X PUT -H "Content-Type: application/json" -d '{
    "title": "Broncos Big Victory",
    "date": "2024-11-14",
    "content": "The Broncos secured a big win against rivals...",
    "team": "Broncos"
}' http://127.0.0.1:8000/api/news/1/ <br>
curl -X DELETE http://127.0.0.1:8000/api/news/1/ <br>
curl http://127.0.0.1:8000/api/news/1/ <br>





### Web news sources
Broncos: https://www.denverpost.com/sports/nfl/denver-broncos/ <br>
Nuggets: https://www.denverpost.com/sports/nba/denver-nuggets/ <br>
Avalanche: https://www.denverpost.com/sports/nhl/colorado-avalanche/ <br> 
Rockies: https://www.denverpost.com/sports/mlb/colorado-rockies/ <br>

