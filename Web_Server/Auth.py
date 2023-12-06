import requests
from requests.auth import HTTPBasicAuth

class Auth:
    
    #link api with authentication
    def __init__(self, link, username = None, password = None):
        self.link = link
        self.username = username
        self.password = password
        self.lista = None
    
    #connection to api
    def connect(self):
        auth = None
        if self.username and self.password:
            auth = HTTPBasicAuth(self.username, self.password)
            
        try:
            response = requests.get(self.link, auth = auth)
            response.raise_for_status()  # Raises an exception if the response has a status code other than 2xx.
        except requests.exceptions.RequestException as e:
            print(f"Error during the connection: {e}")
            return None
        
        if(response.status_code == 200):
            self.lista = response.json()
            return True
        else:
            print(f"Error during connection: Status Code {response.status_code}")
            return False
    
    #return api value
    def getDate(self):
        return self.lista
    
    def search(self, *indici):
        try:
            valore = self.lista
            for indice in indici:
                valore = valore[indice]
            return valore
        except KeyError:
            return None
