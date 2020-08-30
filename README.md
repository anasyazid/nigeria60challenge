# nigeria60challenge
Setting up guide for development server

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
python3 -m venv venv
echo in_production=0 > .env
source venv/bin/activate
pip3 install -r requirements-dev.txt
```

## Running locally
```sh
source venv/bin/activate
python3 manage.py runserver
```

## Make database migrations
```sh
source venv/bin/activate
python3 manage.py make migrations
python3 manage.py migrate
```

## Consideration
If your default python runs python3, you can simply use `python` command in place of `python3`. And `pip` command in place of `pip3`
