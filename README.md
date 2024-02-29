# log-watcher
A simple log watcher

Note: We assume that you have installed docker on your computer. If docker not installed you can get help from [here ](https://docs.docker.com/engine/install/) 

1. Clone the project
2. Now you can find `docker-compose.yml.example` you have to copy and rename it to `docker-compose.yml` file. Command `docker-compose.yml.example docker-compose.yml`
3. Now edit the compose file and set mount the volumn which you want to watch logs
```
    volumes:
    - ./src/:/app
    - ~/domain.com/log/:/domain.com.log
    - ~/another-directory/:/another-directory
    - ~/database/db_logs/:/database.logs
    - /var/log/:/local.logs
```
Note: The first is your physical directory where your logs are located or top folder whichi is mounted to the docker path which will use as alisase 
4.  Now locate `src/` 
5. copy .env.example to env file `cp env.example .env`, you can open `.env` file and update your secreet key, username and password. You can change your username, password and secreet key by your own.  
6. copy config.example.py to config.py `cp config.example.py config.py`
7. You can find a section LOG_FILES in config.py where you can put all the files, now you have to map your all log files which you want to watch
```
# Current file 
LOG_FILES = [
    {"path": "/domain.com.log/access.log", "name": "domain.com-access.log"},
    {"path": "/another-directory/logs/error.log", "name": "Internal-error.log"},
    {"path": "/database.logs/", "name": "Database error.log"},
    {"path": "/local.logs/nginx/error.log", "name": "Local Nginx error.log"},
    {"path": "/local.logs/nginx/access.log", "name": "Local Nginx access.log"},
]
```
8. you can find `requirements.txt` which use for python module installation in docker. 

## Docker Build 
```
docker-compose build
docker-compose up -d 
```

You can access it from http://localhost:5050



## The output after login
<img align="right" src="./screenshot.png" style="width:100%">
