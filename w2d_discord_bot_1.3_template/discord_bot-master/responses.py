import ssl
import urllib.error
import urllib.parse
import urllib.request

import requests
from bs4 import BeautifulSoup



#
def get_all_articles():
    return get_latest_nature_article(), get_latest_eng_tech_article()


def get_response(message):
    u_msg = message[1:].lower()
    if u_msg == "art1":
        return get_latest_eng_tech_article()
    elif u_msg == "art2":
        return get_latest_nature_article()


def get_latest_nature_article():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = "https://www.nature.com/"
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    article = soup.find('a', class_="c-hero__link")
    link = article.get('href')
    return link


def get_latest_eng_tech_article():
    # Make a request to the URL
    url = "https://eandt.theiet.org/"
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the first article on the page
    article = soup.find("div", class_="article-link")

    # print(article)
    # # Extract the link of the article
    link = article.find("a")["href"]

    link = f"https://eandt.theiet.org/{link}"

    return link
