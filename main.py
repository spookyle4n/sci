import requests
from bs4 import BeautifulSoup
import re

# Define the target URL of academia.edu where science researchers' profiles can be found
target_url = 'https://www.academia.edu/'

# Send an HTTP request to fetch the content of the academia.edu homepage
response = requests.get(target_url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find and extract email addresses from the academia.edu homepage using regular expressions
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
emails = re.findall(email_pattern, soup.text)

# Print the extracted email addresses
for email in emails:
    print(email)
