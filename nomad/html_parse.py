from bs4 import BeautifulSoup
import requests

url = "https://repository.nomad-coe.eu/uploads/api/repo/?page=1&per_page=100&order_by=basis_set&order=1&owner=all&atoms=Fr&metrics=total_energies"


headers = {
    "Referer": "https://repository.nomad-coe.eu/uploads/gui/search",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36"
}


html_content = requests.get(url, headers=headers).text
# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
print(soup.prettify()) # print the parsed data of html