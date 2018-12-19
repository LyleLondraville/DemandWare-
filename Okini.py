import requests 
from threading import Thread 

def scrape(start,stop,txt_file):
	
	info_list = []

	while start <= stop :

		get = requests.get('http://www.oki-ni.com/en/%s.html' % start)
		if get.status_code == 200:
			if len(get.url) <= 37:
				info = str(start)+ ' : ' + get.history[1].url
				info_list.append(str(info))
			else :
				info = str(start)+ ' : ' + get.url
				info_list.append(str(info))	
		else :
			info = str(start)+ ' : ' + 'Not found!'
			info_list.append(str(info))	

		start += 1
	txt = open(txt_file, 'w')

	for link in info_list:
		txt.write(link + '\n')

	txt.close()

scrape(403001,404000,'ok4.txt')
