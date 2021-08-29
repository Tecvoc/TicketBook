 * Copyright (C) Nilanjan Bala - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 * Written by Nilanjan Bala, <nilanjan1@tutanota.com>, August 2021


## A sample app for bookig movie tickets

* For simplicity it is assumed that each cinema hall has only one auditorium


## Running the application

```sh
# Activate the virtual environment
pip install -r requirements.txt

# Set the db with custom values
export POSTGRES_DB="dbname"
export POSTGRES_USER="username"
export POSTGRES_PASSWORD="password"

# Setup the data
cd src/

python3 manage.py migrate
python3 manage.py loaddata ../fixtures/movie_app_data.json

# Run the application
python3 manage.py runserver

# Can hit the public api's now as
http://localhost:8000/api/city/

# To run with docker-compose
docker-compose up -d

# Wait for 10 seconds and now can hit the public api's now as
http://0.0.0.0:8080/api/city/

# To stop it, do
docker-compose stop
```
