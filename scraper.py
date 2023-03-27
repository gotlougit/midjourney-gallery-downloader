import requests, json, os
from datetime import datetime
from bs4 import BeautifulSoup

def get_image_urls(url):

    urllist = []

    headers = {'User-Agent': 'curl/7.84.0'}
    page = requests.get(url, headers=headers, allow_redirects=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    body = soup.find("body")
    sc = list(body.find_all("script"))[-1].string
    sc = str(sc)
    # parse JSON
    sc = json.loads(sc).get("props").get("pageProps").get("jobs")
    for i in sc:
        urllist.append(i.get("event").get("seedImageURL"))
    return urllist

def download_image(urllist):
    curdate = datetime.now().strftime("%Y%m%d")
    os.makedirs(curdate, exist_ok=True)
    os.chdir(curdate)

    headers = {'User-Agent': 'curl/7.84.0'}
    i = 1
    for url in urllist:
        page = requests.get(url, headers=headers, allow_redirects=True)
        with open(str(i) + ".webp", 'wb') as f:
            f.write(page.content)
        i+=1
        print(f"Downloaded {i}.webp")

url = 'https://www.midjourney.com/showcase/recents'
url2 = 'https://www.midjourney.com/showcase/top'
urllist1 = get_image_urls(url)
urllist2 = get_image_urls(url2)

unique = set()
for i in urllist1:
    unique.add(i)
for i in urllist2:
    unique.add(i)
download_image(unique)
