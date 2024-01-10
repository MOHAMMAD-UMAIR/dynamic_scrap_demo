import requests
from bs4 import BeautifulSoup

def get_website_content(url):
    # Send an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text content from the HTML body
        page_content = soup.find('main', class_= "page--body")
        page_text = page_content.text()

        return page_text
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")
        return None

# Example usage
url = 'https://www.fortinet.com/products'
website_content = get_website_content(url)

if website_content:
    print(f"Text content of the HTML body of {url}:\n{website_content}")
