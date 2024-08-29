#TIPpy_docker.py
import time
from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller

proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

while True:
    headers = {'User-Agent': UserAgent().random}
    time.sleep(30)
    with Controller.from_port(port=9051) as c:
        c.authenticate()
        c.signal(Signal.NEWNYM)
