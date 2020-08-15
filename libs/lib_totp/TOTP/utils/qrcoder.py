from typing import Tuple
import urllib.parse


class QRCoder:

    URL = "https://chart.googleapis.com/chart?cht=qr&"

    @staticmethod
    def generate(content: str, size: Tuple[int,int] = (400,400), encoded=True):
        uri = QRCoder.URL + f"chs={size[0]}x{size[1]}&" + "chl="
        if encoded:
            return uri + urllib.parse.quote_plus(content)
        else:
            return uri + content
