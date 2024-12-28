import requests
from bs4 import BeautifulSoup

BASE_URL = "https://agmarknet.gov.in"

def scrape_crop_price(crop_name):
    search_url = f"{BASE_URL}/SearchCmmMkt.aspx?cname={crop_name}"
    response = requests.get(search_url)
    
    if response.status_code != 200:
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'tablePrice'})
    
    if not table:
        return None
    
    rows = table.find_all('tr')[1:]  # Skip header row
    if rows:
        first_row = rows[0]
        columns = first_row.find_all('td')
        price = float(columns[3].text.strip())  # Extract price column
        return price
    
    return None
