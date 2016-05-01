#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
import random
import datetime
import telepot
import db
import urllib2
import json
def handle(msg):
    chat_id = msg['chat']['id']
    command  = msg['text'].split(' ')[0]
    if command=='/start':
        message = """
                <b>Bienvenido a Omeybot</b>
                /listar - Despliega una lista de las empresas disponibles
                /buscar - Busca entre todas las empresas disponibles
                /info - Información detallada sobre cierta empresa
                /razones - Razones financieras de la empresa
                /comp - Compara a dos empresas

        """
        bot.sendMessage(chat_id, message, parse_mode='html')
    if command=='/listar':
        message = ''
        for comp in db.getAllCompanies():
            message += '%s - %s \n' % (comp[3], comp[1])
        bot.sendMessage(chat_id, message)
    if command=='/buscar':
        message = ''
        for comp in db.searchCompany(msg['text'].split(' ')[1]):
            message += '%s - %s \n' % (comp[3], comp[1])
        bot.sendMessage(chat_id, message)
    if command=='/info':
        message = ''
        res = db.getLatestDataSheet(msg['text'].split(' ')[1].upper())
        message += '<b>%s</b> \n' % res['nombre']
        message += '<b>Activos:</b> %s\n' % res['activos']
        message += '<b>Pasivos:</b> %s\n' % res['pasivos']
        message += '<b>Ventas:</b> %s\n' % res['ventas']
        message += '<b>Capital:</b> %s\n' % res['cap']
        bot.sendMessage(chat_id, message, parse_mode='html')
    if command=='/razones':
        message = ''
        res = db.getRatios(msg['text'].split(' ')[1].upper())
        message += '<b>%s</b> \n' % res['nombre']
        message += '<b>Circulante:</b> %s\n' % res['circulante']
        message += u'<b>Rápida:</b> %s\n' % res['rapida']
        message += u'<b>Rotación:</b> %s\n' % res['rotacion']
        message += u'<b>Ingreso:</b> %s\n' % res['ingreso']
        message += u'<b>Margen:</b> %s\n' % res['margen']
        bot.sendMessage(chat_id, message, parse_mode='html')
    if command=='/comp':
        message = ''
        emp = db.comp(msg['text'].split(' ')[1].upper(), msg['text'].split(' ')[2].upper())
        message += u'<b>%s | %s</b> \n' % (emp[0]['nombre'], emp[1]['nombre'])
        message += u'<b>Circulante:</b>  %s  %s\n' % (emp[0]['circulante'], emp[1]['circulante'])
        message += u'<b>Rápida:</b>     %s  %s\n' % (emp[0]['rapida'], emp[1]['rapida'])
        message += u'<b>Rotación:</b>   %s  %s\n' % (emp[0]['rotacion'], emp[1]['rotacion'])
        message += u'<b>Ingreso:</b>    %s  %s\n' % (emp[0]['ingreso'], emp[1]['ingreso'])
        message += u'<b>Margen:</b>     %s  %s\n' % (emp[0]['margen'], emp[1]['margen'])

        bot.sendMessage(chat_id, message, parse_mode='html')
    if command=='/quote':
        request = urllib2.Request('http://www.google.com/finance/info?q='+msg['text'].split(' ')[1])
        opener = urllib2.build_opener()
        data =  opener.open(request).read()    
        obj = json.JSONDecoder().decode(data.replace('\n', '')[3:])
        request = urllib2.Request('https://www.google.com/finance/getchart?q='+msg['text'].split(' ')[1])
        opener = urllib2.build_opener()
        img =  opener.open(request).read()    
        message = """ Emisor: %s\nPrice: %s""" % (str(obj[0]['e']), str(obj[0]['l_cur']))
        bot.sendMessage(chat_id, message)
        bot.sendPhoto(chat_id, ('command.jpg',img))

bot = telepot.Bot('185136018:AAElZ047OZtBvA_ktrtqEl-QXGYYbPjC_ew')
bot.message_loop(handle)
print '.......'

while 1:
    time.sleep(10)