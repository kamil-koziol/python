from urllib.parse import unquote
from bs4 import BeautifulSoup
import requests
import json
from tqdm import tqdm
import os

class Video:
    def __init__(self, url: str):

        b_quality = self.best_quality(url)
        if b_quality:
            self.url = self.add_quality(url, b_quality)
        else:
            self.url = url

        response = requests.get(self.url)
        self.soup = BeautifulSoup(response.content, "html.parser")
    
    @staticmethod
    def decrypt(a: str):
        a = unquote(a.replace("_XDDD", ""))
        a = unquote(a.replace("_CDA", ""))
        a = unquote(a.replace("_ADC", ""))
        a = unquote(a.replace("_CXD", ""))
        a = unquote(a.replace("_QWE", ""))
        a = unquote(a.replace("_Q5", ""))
        a = unquote(a.replace("_IKSDE", ""))
        b = []

        for e in range(len(a)):
            f = ord(a[e])
            b.append(chr(33 + (f + 14) % 94) if 33 <= f and 126 >= f else chr(f))

        a = "".join(b)
        
        a = a.replace(".cda.mp4", "")
        a = a.replace(".2cda.pl", ".cda.pl")
        a = a.replace(".3cda.pl", ".cda.pl")
        
        return a
    
    @property
    def title(self):
        title_tag = self.soup.find("span", class_="title-name")
        return title_tag.text.strip()

    def download(self, download_path: str = 'downloads'):

        FILE_PATH = os.path.join(download_path, self.title) + ".mp4"
        CHUNK_SIZE = 1024*1024

        r = requests.get(self.mp4_url, stream=True) 
        headers = r.headers

        contentLength = int(headers.get("content-length", None)) // CHUNK_SIZE

        with open(FILE_PATH, 'wb') as f: 
            progressBar = tqdm(total=contentLength+1, unit="MB")
            for chunk in r.iter_content(chunk_size = CHUNK_SIZE):
                if chunk: 
                    f.write(chunk)
                    progressBar.update(1)
            progressBar.close()

    @property
    def mp4_url(self):
        tags = self.soup.findAll("div")

        for tag in tags:
            if tag.has_attr("player_data"):
                player_data = json.loads(tag["player_data"])
                break

        file = player_data["video"]["file"]
        
        decrypted_file = "https://" + self.decrypt(file)+ ".mp4"
        return decrypted_file
    
    @staticmethod
    def get_qualities(url: str):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        div = soup.find("div", class_='wrapqualitybtn')
        if div:
            links = div.find_all("a")
            return [link.text for link in links]
    
    def best_quality(self, url):
        qualities = self.get_qualities(url)
        if qualities:   
            return qualities[-1]
    
    @staticmethod
    def add_quality(url: str, quality: str):

        if "?wersja=" in url:
            return url
        else:
            return url + "?wersja=" + quality
    

if __name__ == "__main__":
    video = Video("https://www.cda.pl/video/575921609/vfilm?wersja=720p")
    video.download()