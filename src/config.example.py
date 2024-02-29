import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Now use os.environ to fetch the values
SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')  # Provide a default value just in case
USERS = {
    os.environ.get('USERNAME', 'your_username'): os.environ.get('PASSWORD', 'your_password')  # Default values provided as fallback
}

LOG_FILES = [
    {"path": "/logs/logs-app/access.log", "name": "access.log"},
    {"path": "/logs/logs-app/error.log", "name": "error.log"},
    {"path": "/logs/logs-api/access.log", "name": "access.log"},
    {"path": "/logs/logs-api/error.log", "name": "error.log"},
    {"path": "/logs/logs/error.log", "name": "error.log"},
    {"path": "/logs/logs/debug.log", "name": "debug.log"},
]
