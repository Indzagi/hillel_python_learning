import requests
from bs4 import BeautifulSoup

with requests.get('https://www.google.com/') as my_site:
    data = BeautifulSoup(my_site.text, "html.parser")
    with open("my_site.html", "w", encoding="utf-8") as file:
        file.write(str(data))
        print(data.prettify())
