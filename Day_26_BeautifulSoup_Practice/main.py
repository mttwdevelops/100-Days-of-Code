# Created 7/26/2022

from bs4 import BeautifulSoup
import requests # needed for live urls

# with open("website.html", encoding="utf8") as file: # needed to add encoding="utf8" since it gives error otherwise..
#     contents = file.read()
#     # print(file)

# soup = BeautifulSoup(contents, 'html.parser') # parses website into object

# print(soup.title)

# gets all Titles (or "Anchors") from website
# all_anchor_tags = soup.find_all(name = "a")
# for tag in all_anchor_tags:
#     print(tag.getText())

# gets all website links from website
# all_anchor_tags = soup.find_all(name = "a")
# for tag in all_anchor_tags:
#     print(tag.get("href"))

## Now we will be scraping Hacker News, which was done already in PracticeFile's Scrape.py
res = requests.get('https://news.ycombinator.com/news')
yc_webpage = res.text
soup = BeautifulSoup(yc_webpage, 'html.parser')

# what about getting the text?
# print(soup.select(".titlelink"))
# article_tag = soup.find(name = 'a', class_ = "titlelink")
# article_text = article_tag.getText()
# article_link = article_tag.get('href')
# article_upvote = soup.find('span', class_="score").getText()
# print(article_link)
# print(article_upvote)

# in order to get all tags and upvotes, set soup.find in lines 31 and 34 to find_all
article_tag = soup.find_all(name = 'a', class_ = "titlelink")
article_texts = []
article_links = []
for articles in article_tag:
    article_text = articles.getText()
    article_link = articles.get('href')
    article_texts.append(article_text)
    article_links.append(article_link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all('span', class_="score")] # got rid of .gettext since cannot run on list

# print(article_texts)
# print(article_links)
# print(article_upvotes)

# want to get the article link and text with the article with most upvotes
import numpy
# max_index = max(article_upvotes)
# print(max_index)
ind = numpy.argmax(article_upvotes)
print(ind)
print(article_texts[ind])
print(article_links[ind])
print(article_upvotes[ind])