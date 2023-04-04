import requests

api_key = "9cd64cf6"

def get_one_film(id):
    url = f"http://www.omdbapi.com/?i={id}&apikey={api_key}"
    response = requests.get(url)
    if response.ok:
        return response.text
    print(response)
    return None
