from django.core.management import execute_from_command_line
from dotenv import load_dotenv, find_dotenv
from huey import RedisHuey

import sys
import os


load_dotenv(dotenv_path=find_dotenv(), verbose=True)
huey = RedisHuey('webcred', host=os.getenv('REDIS_URL'))
execute_from_command_line(sys.argv)
