import os
from googleapiclient.discovery import build

API_KEY = os.environ["YT_API"]
youtube = build('youtube', 'v3', developerKey=API_KEY)

request = youtube.playlistItems().list(
    part="contentDetails",
    playlistId="PLRqwX-V7Uu6ZV4yEcW3uDwOgGXKUUsPOM"
)

response = request.execute()

for item in response["items"]:
    print(item)