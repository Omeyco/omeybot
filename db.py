#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as lite

def searchCompany(query):
	con = lite.connect('empdb.db')
	res = [] 
	with con:
	    con.row_factory = lite.Row
	    cur = con.cursor() 
	    cur.execute("SELECT * FROM empresa")
	    rows = cur.fetchall()
	    
	    for row in rows:
	        if query in  row["nombre"] or query in row["symbol"]: 
	        	res.append(row)
	return res
	con.close()
def getAllCompanies():
	con = lite.connect('empdb.db')
	res = [] 
	with con:
	    con.row_factory = lite.Row
	    cur = con.cursor() 
	    cur.execute("SELECT * FROM empresa")
	    rows = cur.fetchall()
	    for row in rows:
	        res.append(row)
	return res
	con.close()
def getLatestDataSheet(symbol):
	con = lite.connect('empdb.db')
	res = {}
	with con:
	    con.row_factory = lite.Row
	    cur = con.cursor() 
	    cur.execute("SELECT * FROM empresa NATURAL JOIN reporte WHERE empresa.symbol = '%s'"%symbol)
	    rows = cur.fetchall()
	    for row in rows:
	    	res['nombre'] = row['nombre']
	        res['activos'] = row['act_cir']+row['act_fij']+row['act_dif']
	        res['pasivos'] = row['pas_cir']+row['pas_lp']
	        res['ventas'] = row['ventas']
	        res['cap'] = row['cap']
	return res
	con.close()

def getRatios(symbol):
	con = lite.connect('empdb.db')
	res = {}
	with con:
	    con.row_factory = lite.Row
	    cur = con.cursor() 
	    cur.execute("SELECT * FROM empresa NATURAL JOIN reporte WHERE empresa.symbol = '%s'"%symbol)
	    rows = cur.fetchall()
	    for row in rows:
	    	res['nombre'] = row['nombre']
	        res['circulante'] = round(row['act_cir']/row['pas_cir'], 2)
	        res['rapida'] = round((row['act_cir']-row['inv'])/row['pas_cir'], 2)
	        res['ingreso'] = round(row['uti_net']/row['cap'], 2)
	        res['margen'] = round(row['uti_net']/row['ventas'], 2)
	        res['rotacion'] = round(row['ventas']/row['act_fij'], 2)
	return res
	con.close()


def comp(symbol1, symbol2):
	con = lite.connect('empdb.db')
	emp = []
	res = {}
	res2 = {}
	with con:
	    con.row_factory = lite.Row
	    cur = con.cursor() 
	    cur.execute("SELECT * FROM empresa NATURAL JOIN reporte WHERE empresa.symbol = '%s'"%(symbol1))
	    rows = cur.fetchall()
	    for row in rows:
	    	res['nombre'] = row['nombre']
	        res['circulante'] = round(row['act_cir']/row['pas_cir'], 2)
	        res['rapida'] = round((row['act_cir']-row['inv'])/row['pas_cir'], 2)
	        res['ingreso'] = round(row['uti_net']/row['cap'], 2)
	        res['margen'] = round(row['uti_net']/row['ventas'], 2)
	        res['rotacion'] = round(row['ventas']/row['act_fij'], 2)
	        emp.append(res)
	    cur.execute("SELECT * FROM empresa NATURAL JOIN reporte WHERE empresa.symbol = '%s'"%(symbol2))
	    rows = cur.fetchall()
	    for row in rows:
	    	res2['nombre'] = row['nombre']
	        res2['circulante'] = round(row['act_cir']/row['pas_cir'], 2)
	        res2['rapida'] = round((row['act_cir']-row['inv'])/row['pas_cir'], 2)
	        res2['ingreso'] = round(row['uti_net']/row['cap'], 2)
	        res2['margen'] = round(row['uti_net']/row['ventas'], 2)
	        res2['rotacion'] = round(row['ventas']/row['act_fij'], 2)
	        emp.append(res2)
	return emp
	con.close()

