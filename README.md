# nigeria60challenge
Clone repository
```sh
git clone git@github.com:N-60/nigeria60challenge.git
```

Enter directory and install dependencies
```sh
cd nigeria60challenge
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run server
```sh
source venv/bin/activate
python manage.py runserver
```

Make database migrations
```sh
source venv/bin/activate
python manage.py make migrations
python manage.py migrate
```
