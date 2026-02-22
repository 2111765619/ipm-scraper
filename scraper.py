import requests
from bs4 import BeautifulSoup

# URL of the IPM trademark announcements page
url = 'http://ipm.ssaa.ir/'

# Function to extract trademark announcements
def scrape_trademark_announcements():
    response = requests.get(url)
    page_content = response.content

    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(page_content, 'html.parser')

    # Find the section containing announcements
    announcements = soup.find_all('div', class_='announcement')  # Adjust the selector based on the actual HTML structure

    # Extract and print each announcement
    for announcement in announcements:
        title = announcement.find('h2').get_text()  # Adjust as necessary
        date = announcement.find('span', class_='date').get_text()  # Adjust as necessary
        print(f'Title: {title}, Date: {date}')

if __name__ == '__main__':
    scrape_trademark_announcements()