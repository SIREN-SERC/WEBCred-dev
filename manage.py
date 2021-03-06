import sys
from dotenv import load_dotenv, find_dotenv
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line

load_dotenv(dotenv_path=find_dotenv(), verbose=True)
wsgi = get_wsgi_application()

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
