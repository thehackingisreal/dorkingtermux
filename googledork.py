import requests, re, os, base64;
from urlparse import urlparse, parse_qs

def scan(dork, tld, log):
	url = []
	result = open(log,"a")
	page = 0
	print("[+] Scanned  Dork : "+dork)
	print("[+] Scan 200 aja : "+dork)
	while page <= 200:
		urll = "http://www.google."+tld+"/search?q="+dork+"&start="+str(page)+"&inurl=https"
		htmll = requests.get(urll).text
		if re.findall('<script src="(.*?)" async defer></script>', htmll):
			print("[-] ups Captcha Detect! You're Requests Blocked please reset to hp")
			print("[-[  You're Connection For Change New IP Addres")
			pass
		else:
			pass
		link = re.findall(r'<h3 class="r"><a href="(.*?)"',htmll)
		for i in link:
			i=i.strip()
			o = urlparse(i, 'http')
			if i.startswith('/url?'):
				link = parse_qs(o.query)['q'][0]
				url.append(link)
				result.write(str(link+"\n"))
		page+=10
		print("["+str(len(url))+"]  SCANNED SITE")
	print("["+str(len(url))+"] Success scanned")
	print("["+str(len(url))+"] good job")
	print("["+str(len(url))+"] tinggal lihat wordlist dah ")
print '''
 ____________________
|                    |
| google auto dorker |
|_________BOT___________|
'''
print
print("[*] author the dark night's Dorker\n[*] INDONESIA SECURITY LITE AND ALL GROUP CYBER\n\n")

dork = raw_input("[dorking-bot] masukan dorknya : ")
if ' ' in dork:
	dork = dork.replace(' ', '+')
else:
	pass
dom = "com"
out = raw_input("[dorking-bot] masukin txt buat ngumpulin dorknya : ")
scan(dork,dom,out,)