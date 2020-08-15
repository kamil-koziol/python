import time
from main import ScrapeCDA
from contextlib import contextmanager

@contextmanager
def timer(desc: str, f):
    start = time.time()
    try:
        yield start
    finally:
        with open(f, "a") as f:
            f.write(desc+': '+str(time.time()-start)+"\n")

filename = "results.txt"
with timer("Time to initialize", filename):
    cda = ScrapeCDA()

with timer("Time to get 1 video page", filename):
    vids = cda.get_new_videos(1)

with timer("Time to get 10 video pages", filename):
    cda.get_new_videos(10)

with timer("Time to get 1 video download link", filename):
    cda.get_video_download("https://www.cda.pl/video/4809632a9")

with timer("Time to get 30 video download links", filename):
    for vid in vids:
        cda.get_video_download(vid.link)