from time import time
from sys import platform, exit

if platform == 'linux' or platform == 'linux2':
    filepath = '/tmp/py_simple_healthcheck'
else:
    filepath = 'py_simple_healthcheck'

def health_check(timeout):
    with open(filepath, 'w+') as file:
        file.write(f'{str(int(time()))},{str(timeout)}')

def is_healthy():
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            timestamp, timeout = content.split(',')
            if time() > int(timestamp) + int(timeout):
                exit(1)
    
    except FileNotFoundError as e:
        print('Healthcheck file not found', flush=True)
