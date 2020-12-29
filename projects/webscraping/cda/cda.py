import asyncio

from bs4 import BeautifulSoup

from typing import List, Awaitable
from video import Video
import aiohttp

NEW_VIDEOS_URL = "https://www.cda.pl/video/najnowsze/"

async def get_page_source(uri):
    async with aiohttp.ClientSession() as session:
        async with session.get(uri) as r:
            content = await r.read()
            return content


async def get_new_videos_urls(pages: int) -> Awaitable[List[str]]:
    tasks = [get_page_source(NEW_VIDEOS_URL + str(i)) for i in range(1, pages + 1)]
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

            videos.append(link)
    return videos

if __name__ == "__main__":
    videos_urls = asyncio.run(get_new_videos_urls(20))
    for video_url in videos_urls:
        print(video_url)
