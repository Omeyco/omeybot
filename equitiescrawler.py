#-*- coding: utf8 -*-
import urllib2
import json
import time
from bs4 import BeautifulSoup
import sys





if len(sys.argv) == 3:
	request = urllib2.Request('http://investing.com/equities/' + sys.argv[2])
else:
	request = urllib2.Request('http://investing.com/equities/')




request.add_header('User-Agent','elbenas')
opener = urllib2.build_opener()
page =  opener.open(request).read()    
soup = BeautifulSoup(page, 'html.parser')
eqs = soup.find_all(attrs={"class": "bold left noWrap elp"})




for x in eqs:
	# print 'http://mx.investing.com'+x.a['href']+'-balance-sheet'
	try:
		if(sys.argv[1] in x.a.text):
			#print  'http://mx.investing.com'+x.a['href']+'-balance-sheet'
			#print "<h1>"+ x.a.text +"</h1>"
			request = urllib2.Request('http://mx.investing.com'+x.a['href']+'-balance-sheet')
			request.add_header('User-Agent','elbenas')
			opener = urllib2.build_opener()
			page =  opener.open(request).read() 
			s1 = BeautifulSoup(page, 'html.parser')
			li = s1.find('table', {'class': 'genTbl reportTbl'})

			page = page.split('"rrtable"',1)[1]
			page = page.split("</tr>            </tbody>",1)[0]

			info = {}
			print x.a.text

			page = page.split('" bold">',1)[1]
			titulo = page.split('<span',1)[0]
			page = page.split('<td>',1)[1]
			info[titulo] = page.split('</',1)[0]

			for i in range(0,40):
				page = page.split('"">',1)[1]
				titulo = page.split('</',1)[0]
				page = page.split('<td>',1)[1]
				info[titulo] = page.split('</',1)[0]

			for i in range (0,3):
 				page = page.split('" bold">',1)[1]
				titulo = page.split('</',1)[0]
				page = page.split('<td>',1)[1]
				info[titulo] = page.split('</',1)[0]

			for x in info:
				print x + " = " + info[x]



			######



			break


		

			#print soup.find_all(id='rrtable')[1]
			# for y in soup.find_all(id='rrtable'):
			# 	print y.tbody

	except Exception, e:
		pass
	
