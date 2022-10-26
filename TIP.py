import time
import requests
from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller
proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}
print("Created by drgreentumb93")
print("Changing IP Address in every 30 seconds....\n\n")
while True:
    headers = { 'User-Agent': UserAgent().random }
    time.sleep(30)
    with Controller.from_port(port = 9051) as c:
        c.authenticate()
        c.signal(Signal.NEWNYM)
        print(f"Your IP is : {requests.get('https://ident.me', proxies=proxies, headers=headers).text}  ||  User Agent is : {headers['User-Agent']}")
