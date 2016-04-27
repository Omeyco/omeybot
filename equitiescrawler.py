import urllib2
import json
from bs4 import BeautifulSoup

request = urllib2.Request('http://mx.investing.com/equities/mexico')
request.add_header('User-Agent','elbenas')
opener = urllib2.build_opener()
page =  opener.open(request).read()    
soup = BeautifulSoup(page)
eqs = soup.find_all(attrs={"class": "bold left noWrap elp"})
empresas = []
for x in eqs:
	# print 'http://mx.investing.com'+x.a['href']+'-balance-sheet'
	try:
		print '<h1>'+x.a.text+'</h1>'
		request = urllib2.Request('http://mx.investing.com'+x.a['href']+'-balance-sheet')
		request.add_header('User-Agent','elbenas')
		opener = urllib2.build_opener()
		page =  opener.open(request).read()    
		soup = BeautifulSoup(page)
		for y in soup.find_all(id='rrtable'):
			print y.tbody
	except Exception, e:
		pass
	
