import sys
from dotenv import load_dotenv, find_dotenv
from django.core.management import execute_from_command_line


if __name__ == "__main__":
    load_dotenv(dotenv_path=find_dotenv(), verbose=True)
    execute_from_command_line(sys.argv)
