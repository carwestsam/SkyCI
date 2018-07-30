## Backend Service

```bash
# create new migration file
FLASK_APP=main.py flask db migrate

# apply migrations
FLASK_APP=main.py flask db upgrade

# start application
FLASK_APP=main.py flask run

```