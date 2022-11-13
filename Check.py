import requests 
import venv
import json
import asynch 

def check_connection():
    for url in ['https://api.github.com', 'https://api.github.com/invalid']:
        try:
            responce = requests.get(url)
        except requests.exceptions.HTTPError as http_err:
            print(print(f'HTTP error occurred: {http_err}')  
        except Exception as err:
            print(f'Other error occurred: {err}') 
        else:
            print('Success!'))
def login_setter(login, password, url):
    
