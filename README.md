# nigeria60challenge

## Requirements
git bash
python 3.7+


## Setting up

Clone repository
```sh
git clone git@github.com:N-60/nigeria60challenge.git
```

Enter directory and install dependencies
```sh
cd nigeria60challenge
python -m venv venv
echo in_production=0 > .env
source venv/bin/activate
pip install -r requirements.txt
```

## Running locally
```sh
source venv/bin/activate
python manage.py runserver
```

## Make database migrations
```sh
source venv/bin/activate
python manage.py make migrations
python manage.py migrate
```
