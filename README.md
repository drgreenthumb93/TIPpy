## TIPpy or TOR IP-Changer (for Python)

In case you have to do a wide scan and don't want to get blocked, this is the right tool for you.


Check if TOR is installed and right configured:

```
curl --socks5 localhost:9050 --socks5-hostname localhost:9050 -s https://check.torproject.org/ | cat | grep -m 1 Congratulations | xargs
```
If you see "Congratulations. This browser is configured to use Tor.", then you can proceed. Otherwise you should reconfigure you TOR settings.

You need to install the following Python modules:

- sudo pip3 install requests
- sudo pip3 install requests[socks]
- sudo pip3 install requests[security]
- sudo pip3 install cryptography
- sudo pip3 install stem
- sudo pip3 install fake_useragent


Add the following to /etc/tor/torrc

```
ControlPort 9051
CookieAuthentication 1
```

After that restart the TOR service

```
sudo systemctl restart tor.service 
```

or

```
sudo service restart tor
```

You can change the time at time.sleep(5) to eg time.sleep(50) to change you IP every 50s.

Then start the script with:

```
sudo python3 TIP.py 
```

![TOR changes IP after 5s](https://raw.githubusercontent.com/drgreenthumb93/tor_ip_changer/main/ip_changer1.png)
