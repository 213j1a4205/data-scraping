import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://www.merchantgenius.io/"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the section for "BROWSE SHOPIFY STORES BY LAUNCH DATE"
    section = soup.find('section', {'id': 'shopify-stores-by-launch-date'})  # Replace with the actual id or class if different

    # Find the specific date section (for example, January 2023)
    date_section = section.find('div', {'data-date': 'January 2023'})  # Replace with the actual tag and attributes

    # Extract the list of websites
    websites = date_section.find_all('a', href=True)

    # Print the extracted websites
    for website in websites:
        print(website['href'])
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
