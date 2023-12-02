import requests
from requests.auth import HTTPBasicAuth
import json

class Auth:
    def __init__(self, link):
        self.link = link
        
    def __init__(self, link, username, password):
        self.link = link
        self.username = username
        self.password = password
    
    def connect(self):
        user = HTTPBasicAuth(self.username, self.password)
        try:
            response = requests.get(self.link, auth=user)
            print(response.status_code)
            response.raise_for_status()  # Solleva un'eccezione se la risposta ha uno status code non 2xx
        except requests.exceptions.RequestException as e:
            print(f"Errore durante la connessione: {e}")
            return None
        
        return response.status_code