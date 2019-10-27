# assignment-Flask-API
API using flask in virtual environment with CORS enabled

some useful tips:

if pip3 not found, use `python3 -m pip` instead

install virtualenv `pip install virtualenv`

initialize virtual env by `virtualenv env`

change source `source env/bin/activate`

install flask and flask-sqlalchemy `pip3 install flask flask-sqlalchemy`

subl app.py

to create db, in `python3` cli enter 
* from app import db
* db.create_all()

install gunicorn `pip3 install gunicorn`

install heroku & login `heroku login`

before deploying to heroku
* `pip3 freeze > requirements.txt`
* `touch Procfile`
* `git init`
* `git add -A`
* `git commit -m "first"`
* `heroku create myapp`
* `git remote -v`
* `git push heroku master`

It must have been deployed now



Code inspiration: 
