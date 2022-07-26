import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

res = requests.get(URL)
webpage = res.text
soup = BeautifulSoup(webpage, 'html.parser')
# print(soup)
mvlist = []
article_tag = soup.find_all(name = 'h3', class_ = "title")

## want to scrape the h3 class = "title"
movielist = [x.text for x in article_tag]
text = ', '.join(movielist)
# print(movielist)
for i in reversed(movielist):
    print(i)
    mvlist.append(i)

with open('movielist.txt', 'w', encoding="utf-8") as file:
    for item in mvlist:
        file.write(f"{item}\n")