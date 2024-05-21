## This is a FastAPI base app for services/microservices

### Create and activate virtual enviroment

python3 -m venv venv

source venv/bin/activate

export PYTHONPATH=$PWD

### Install the requirements
pip install -r requirements.txt

    ├── app
    │   ├── __init__.py
    │   ├── service.ini # service config file
    │   ├── main.py # main entry file
    │   ├── dependencies.py # dependencies file (auth, etc)
    │   └── routes
    │       ├── api.py # main routes
    │       ├── dummy.py # dummy routes
    │       ├── admin.py # admin routes    
    │       ├── items.py # items routes
    │       ├── mongo.py # mongo routes
    │   └── models/ # pydantic models
    │   └── server
    │       ├── exception_handler.py # custom class to handle exceptions (if need it)
    │       ├── database.py # database connection
    └── tests # tests folder
    └── requirements.txt # dependencies (pip)


### run locally

uvicorn app.main:app --reload

### compile as a docker image

docker build -t fastapi-mongo .

docker run -d --name fastapi-mongo -p 8888:80 fastapi-mongo


### Resouces 

FastAPI Sample.postman_collection.json