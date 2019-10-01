# MyMenu

## Setup
- Clone this repo
- This project uses [pipenv](https://github.com/pypa/pipenv)
    - Install dependencies and create virtual environment: `pipenv install --dev`
- Run migrations: `python manage.py migrate`
- Create superuser: `python manage.py createsuperuser`
- Start server: `python manage.py runserver 0.0.0.0:8000`


## Info

- The admin page can be fount at [0.0.0.0:8000/admin](http://0.0.0.0:8000/admin)
- You can get the urls with: `python manage.py show_urls`
