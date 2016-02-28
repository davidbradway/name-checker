# README

This is a tool to identify if an entered name has any bad initials or email patterns
or if that name could become a problem upon a marriage name change.

## Get name-checker

Download a snapshot: https://gitlab.oit.duke.edu/dpb6/name-checker/repository/archive.zip

Or:

    git clone git@gitlab.oit.duke.edu:dpb6/name-checker.git
    cd name-checker/

## Setup

### Local test

```bash
pip install virtualenv
virtualenv flask
.\flask\Scripts\pip install flask
.\flask\Scripts\pip install flask-wtf
.\flask\Scripts\python .\app.py
```

#### Go to the webpage:

http://localhost:5000

### Deployment to Heroku

```bash
history | grep heroku
heroku login
heroku create
#heroku create babynamechecker-flask1 -s cedar
git push heroku master
heroku ps:scale web=1 
heroku ps
```

## Reference

[Learn Python the Hard Way tutorials](http://learnpythonthehardway.org/book/ex51.html)
