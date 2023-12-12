# Cinema API

This API, developed using Django REST Framework (DRF), offers a comprehensive solution for cinema management. It allows developers to seamlessly integrate and automate various cinema-related functions such as accessing movie showtimes, processing bookings, and handling customer data.

## Setup manualy:
First, install PostgreSQL and set up a database. Then, follow these steps:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Configure your environment variables:
```
POSTGRES_HOST={POSTGRES_HOST}
POSTGRES_NAME={POSTGRES_NAME}
POSTGRES_USER={POSTGRES_USER}
POSTGRES_PASSWORD={POSTGRES_PASSWORD}
SECRET_KEY={SECRET_KEY}
```
On Linux run:
```
source .env
sh start.sh
```
On Windows run:
```
env.bat
bash start.sh
```


## Run with Docker:
```
docker-compose build
docker-compose up
```