import requests 
from threading import Thread

def scrape(start,stop,txt_file):
	link_list = []	

	print 'Started Scraping'
	
	while start <= stop :
		url = 'http://www.pacsun.com/%s.html'%start
		r = requests.get(url)
		if str(r.url) != url:
			prod_url = str(start)+' : '+r.url
			print prod_url
			link_list.append(prod_url)
		else :
			print start
		start +=1
	
	txt = open(txt_file, 'w')
	
	for link in link_list:
		txt.write(link+'\n')
	
	txt.close()

	print 'Stoped scraping'

def main():
	t1 = Thread(target = scrape, args = (5886106, 5886120, 'pacsun1.txt'))

	t1.start()

main()