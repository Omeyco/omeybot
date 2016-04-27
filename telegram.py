import sys
import time
import random
import datetime
import telepot
import urllib2
import json
def handle(msg):
    chat_id = msg['chat']['id']
    command  = msg['text']
    request = urllib2.Request('http://www.google.com/finance/info?q='+command)
    opener = urllib2.build_opener()
    data =  opener.open(request).read()    
    obj = json.JSONDecoder().decode(data.replace('\n', '')[3:])
    request = urllib2.Request('https://www.google.com/finance/getchart?q='+command)
    opener = urllib2.build_opener()
    img =  opener.open(request).read()    
    message = """ Emisor: %s\nPrice: %s""" % (str(obj[0]['e']), str(obj[0]['l_cur']))
    bot.sendMessage(chat_id, message)
    bot.sendPhoto(chat_id, ('command.jpg',img))

bot = telepot.Bot('')
bot.notifyOnMessage(handle)
print '.......'

while 1:
    time.sleep(10)