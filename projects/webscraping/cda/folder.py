import requests
from bs4 import BeautifulSoup
from video import Video
from typing import List

class Folder:
    def __init__(self, url: str):
        self.url = url

    def get_videos_urls(self) -> List[Video]:
        videos: str = []

        i = 1
        while True:
            resp = requests.get(self.url + "/" + str(i))
            soup = BeautifulSoup(resp.text, "html.parser")
            scrape = soup.find_all("span", class_='wrapper-thumb-link')

            if(len(scrape) == 0):
                return videos
            else:
                for vid in scrape:
                    url = vid.a.get("href")
                    if url:
                        if not url.startswith("https://www.cda.pl"):
                            url = "https://www.cda.pl" + url
                    videos.append(url)
            i+= 1
    
    def download(self, download_path: str = "downloads"):
        # TODO: Add creating folders if not exist
        for url in self.get_videos_urls():
            video = Video(url)
            video.download(download_path)


if __name__ == "__main__":
    folder = Folder("https://www.cda.pl/TheTadelaX/folder/20948491")
    folder.download("/Users/kamil-koziol/Downloads/OPM")

