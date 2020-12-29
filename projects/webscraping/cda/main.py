import requests
from bs4 import BeautifulSoup
import csv
from collections import namedtuple

from typing import List, Optional
import asyncio
import aiohttp
import time

class ScrapeCDA:
    Video = namedtuple("Video", ["title", "link", "author"])

    def __init__(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)
    
    def get_video_download(self, video_uri: str) -> Optional[str]:
        self.driver.get(video_uri)
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        video = soup.find("video")
        if not video:
            return "premium"

        download_uri = video.get("src")
        return download_uri
    
    # POCZEKALNIA
        
    async def get_new_videos(self, pages: int) -> List[namedtuple("Video", ["title", "link", "author"])]:
        URI = "https://www.cda.pl/video/najnowsze/"
        tasks = [self.__get_page_source(URI + str(i)) for i in range(1,pages+1)]
        sources = await asyncio.gather(*tasks)

        videos = []
        for source in sources:
            soup = BeautifulSoup(source, "html.parser")

            for text in soup.find_all("div", class_="poczekalnia-left-col"):
                title = text.a.text
                if text.a["href"].startswith('https://www.cda.pl'):
                    link = text.a["href"]
                else:
                    link = "https://www.cda.pl" + text.a["href"]

                if text.div.div.a:
                    author = text.div.div.a.text[7:]
                else:
                    author = "anonim"

                myVideo = ScrapeCDA.Video(title, link, author)
                videos.append(myVideo)
        return videos

    # FOLDERY
    async def __get_folder_pages_amount(self, uri:str):
        i = 1
        while True:
            resp = await self.__get_page_source(uri + "/" + str(i))
            soup = BeautifulSoup(resp, "html.parser")
            scrape = soup.find_all("span", class_='wrapper-thumb-link')
            if(len(scrape) == 0):
                return i-1
            i+=1

    async def __get_page_source(self, uri):
        async with aiohttp.ClientSession() as session:
            async with session.get(uri) as r:
                content = await r.read()
                return content

    async def __get_folder_sources(self, folder_uri: str):
        pages = await self.__get_folder_pages_amount(folder_uri)
        tasks = []
        for page in range(1,pages+1):
            tasks.append(self.__get_page_source(folder_uri + "/" +str(page))) 
        return await asyncio.gather(*tasks)
    
    async def get_folder(self, folder_uri: str):
        videos = []
        sources = await self.__get_folder_sources(folder_uri)
        for page_source in sources:
            soup = BeautifulSoup(page_source, "html.parser")
            scrape = soup.find_all("span", class_='wrapper-thumb-link')
            for vid in scrape:
                link = vid.a.get("href")
                if link:
                    if not link.startswith("https://www.cda.pl"):
                        link = "https://www.cda.pl" + link
                        
                title = vid.img.get("alt")
                thumbnail_uri = vid.img.get("src")
                time = vid.span.text
                videos.append((title,link,thumbnail_uri,time))
        return videos


cda = ScrapeCDA()
# URI = "https://www.cda.pl/Snikibiki1337/folder/23386979"

folder = asyncio.run(cda.get_folder("https://www.cda.pl/TheTadelaX/folder/20948491"))
# download_links = []
# for vid in folder:
#     d_link = cda.get_video_download(vid[1])
#     print(d_link)
#     download_links.append(d_link)

with open("TEST.csv", 'w') as f:
    writer = csv.writer(f)
    for vid in folder:
        writer.writerow(vid)


# i = asyncio.run(cda.get_new_videos(34))
# print(i)

# with open("pliki.txt", "w") as f:
#     for video in asyncio.run(cda.get_new_videos(1)):
#         link = cda.get_video_download(video.link)
#         print(link)
#         f.write(link+ "\n")


# print(cda.get_video_download("https://www.cda.pl/video/556194077"))