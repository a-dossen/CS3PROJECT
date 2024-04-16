import requests

if __name__ == '__main__':
    API_KEY = 'AIzaSyAqKk6xDQcFVV5eGU-luM3Q_vEBoobyflk' 
    SEARCH_ENGINE_ID = '40b30577200994fb3'

    # API_KEY = open('API_KEY').read()
    # SEARCH_ENGINE_ID = open('SEARCH_ENGINE_ID').read()

search_query = input("Search: ")

url = 'https://www.googleapis.com/customsearch/v1'
params = {
    'key': API_KEY,
    'q' : search_query,
    'cx': SEARCH_ENGINE_ID
}

response = requests.get(url, params=params)
results = response.json()['items']

counter=1
for item in results:
    if counter <= 10:
        print(f"{counter}. ", end="")
        counter+=1
        print(item['link'])