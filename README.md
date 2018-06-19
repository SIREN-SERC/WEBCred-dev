# Installation
- Install the python dependencies using [pipenv](https://github.com/pypa/pipenv)
```
    $ pipenv install
```

- Create a Postgres database and populate the variables listed in `env.sample` into `.env`
- Apply database migrations
```
    $ python manage.py migrate
```
- Start the webserver
```
    $ python manage.py runserver
``` 

Based on the original WEBCred application [here](https://github.com/Shriyanshagro/WEBCred)

![WEBCred](static/screenshot.png)
