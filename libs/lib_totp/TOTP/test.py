from utils.qrcoder import QRCoder
import pyotp
from utils.hasher import Hasher
import webbrowser
import uuid

for i in range(20):
    myid = uuid.uuid4()
    print(myid)