import requests
from bs4 import BeautifulSoup

def get_h3_headings(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        h3_headings = [heading.text.strip() for heading in soup.find_all('h3')]
        
        return h3_headings
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return []

url = 'http://www.columbia.edu/~fdc/sample.html'
headings = get_h3_headings(url)

if headings:
    print(headings)
else:
    print("No <h3> headings found on the page.")
