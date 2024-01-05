# ByteQuest Assignment

## Local Setup

- Git clone: `https://github.com/bharatswamy/bytequest.git`
- Go to the project directory: `cd bytequest`
- Setup virtual environment: `python3 -m venv env .` (do not forget to add the dot(.) in the end)
- Activate virtual environment: `source env/bin/activate`
- Add following variales in `local_settings.py` file parallel to the `settings.py` file.
TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
FACEBOOK_APP_ID, FACEBOOK_APP_SECRET
- Install requirements: `pip install -r requirements.txt`
- Run migrations: `python manage.py makemigrations`, `python manage.py migrate`
- Run server using local settings: `python manage.py runserver`
- See it running on [localhost](http://127.0.0.1:8000/)