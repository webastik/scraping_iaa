import requests
import lxml
from bs4 import BeautifulSoup
from time import sleep


url_start = "https://www.iaai.com/Search?url=lAuF7d4zu%2fDaMTtOHzDbUXqb%2fEhijt7Vs0tYOM1OHbY%3d"
response = requests.get(url_start)
soup = BeautifulSoup(response.text, "lxml")
link = "https://www.iaai.com" + soup.find("h4", class_="heading-7 rtl-disabled").find("a").get("href") # get lot full URL
print(link)
sleep(2)


# get vehicle's attributes

response_lot = requests.get(link)

soup_lot = BeautifulSoup(response_lot.text, "lxml")

soup_lot.findAll( class_="data-list__value").text

#lot_id = soup_lot.find("ul", class_="data-list data-list--details").text
print(soup_lot)



print("Lot id: " + lot_id, "Link: " + link)