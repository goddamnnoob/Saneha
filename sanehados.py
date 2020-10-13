#!/usr/bin/env python3

import requests
import random
import re
import threading
def get_proxies():
	proxies = []
	res = requests.get('https://free-proxy-list.net').text
	p = re.findall('(\d+\.\d+\.\d+\.\d+):(\d+)',res)
	for proxy in p:
        	proxies.append(proxy[0]+':'+proxy[1])
	return proxies
def attack(proxies):
	s= requests.Session()
	proxy = random.choice(proxies)
	s.proxies = {"http":proxy,"https":proxy}
	for i in range(10):
		try:
			res = s.get('http://www.icanhazip.com',timeout = 6)
			print(res.text)
		except Exception as e:
			try:
				s.proxies = {"http":"socks5://"+proxy,"https":"socks5://"+proxy}
				res = s.get('http://www.icanhazip.com',timeout = 1.5)
				print(res.text)
			except Exception as e:
				try:
					s.proxies = {"http":"socks4://"+proxy,"https":"socks4://"+proxy}
					res = s.get('http://www.icanhazip.com',timeout =1.5)
					print(res.text)
				except Exception as e:
					print("failed")
					return 0

if __name__ == "__main__":
	print("START!")
	proxies = get_proxies()
	for i in range(10):
		t = threading.Thread(target=attack, args=(proxies,))
		t.start()
