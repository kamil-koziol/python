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

            if (len(scrape) == 0):
                return videos
            else:
                for vid in scrape:
                    url = vid.a.get("href")
                    if url:
                        if not url.startswith("https://www.cda.pl"):
                            url = "https://www.cda.pl" + url
                    videos.append(url)
            i += 1

    def download(self, download_path: str = "downloads"):
        # TODO: Add creating folders if not exist
        videos = [
            "https://www.cda.pl/video/2486267d4",
            "https://www.cda.pl/video/248630943",
            "https://www.cda.pl/video/250105452",
            "https://www.cda.pl/video/2518128a9",
            "https://www.cda.pl/video/2531640cb",
            "https://www.cda.pl/video/2546847e8",
            "https://www.cda.pl/video/256809044",
            "https://www.cda.pl/video/2583666bd",
            "https://www.cda.pl/video/25999076f",
            "https://www.cda.pl/video/261542952",
            "https://www.cda.pl/video/2652516eb",
            "https://www.cda.pl/video/2671470a4",
            "https://www.cda.pl/video/3424375c3",
            "https://www.cda.pl/video/3443971c3",
            "https://www.cda.pl/video/3463282e8",
            "https://www.cda.pl/video/3485605e6",
            "https://www.cda.pl/video/351312746",
            "https://www.cda.pl/video/35377301f",
            "https://www.cda.pl/video/35612772a",
            "https://www.cda.pl/video/358452193",
            "https://www.cda.pl/video/360697930",
            "https://www.cda.pl/video/362523795"
        ]
        for url in videos:
            video = Video(url)
            print(url)
            video.download(download_path)


if __name__ == "__main__":
    folder = Folder("https://www.cda.pl/Zoxks/folder/29570831")

    folder.download()
