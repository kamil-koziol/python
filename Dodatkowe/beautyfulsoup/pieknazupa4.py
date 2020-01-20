from bs4 import BeautifulSoup
import requests

with open('example.html') as html_file:
    soup = BeautifulSoup(html_file, "lxml")

# print(soup.prettify())

# match = soup.title.text
# print(match)

article = soup.find("div", class_="article")
print(article)

# footer = soup.find("div", class_="footer")
# print(footer)

# article_headline = article.h2.a.text
# print(article_headline)

# summary = article.p.text
# print(summary)

for artic in soup.find_all("div", class_="article"):
    artic_headline = artic.h2.a.text
    print(artic_headline)

    summary = artic.p.text
    print(summary)