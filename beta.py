#!/usr/bin/env python3
import sys
import urllib.parse
import urllib.request
from flask import request
import requests 
from flask import Flask, render_template, request, redirect
import bs4 as bs

#https://www.youtube.com/watch?v=aIPqt-OdmS0 Web scraping and parsing with BeautifulSoup

sauce = urllib.request.urlopen('https://registrar.vt.edu/dates-deadlines-accordion/Drop-Add.html').read()
soup = bs.BeautifulSoup(sauce, 'html.parser')
table = soup.table
table_rows = table.find_all('tr')
dates = ()
crF = soup.find(string="Fall 2018: March 20-27, 2018")
crS = soup.find(string = "Spring 2019: October 16-23, 2018")
print ("\n\n_Upcoming course request deadlines_\n")
print ("> {}".format(crF))
print ("> {} \n".format(crS))

for tr in table_rows:
	td = tr.find_all('td')
	for i in td:
		for j in i:
			dates = dates + (j,)

print ("____Web Drop/Add Availability____\n")
print ("* Term:      	{}".format(dates[0]))
print ("> Add Period:	{}".format(dates[1]))
print ("> Drop Period:	{}\n".format(dates[2]))

print ("* Term:      	{}".format(dates[4]))
print ("> Add Period:	{}".format(dates[5]))
print ("> Drop Period:	{}\n".format(dates[6]))

print ("* Term:      	{}".format(dates[8]))
print ("> Add Period:	{}".format(dates[9]))
print ("> Drop Period:	{}\n".format(dates[10]))

print ("* Term:      	{}".format(dates[12]))
print ("> Add Period:	{}".format(dates[13]))
print ("> Drop Period:	{}\n".format(dates[14]))

print ("* Term:      	{}".format(dates[16]))
print ("> Add Period:	{}".format(dates[17]))
print ("> Drop Period:	{}\n".format(dates[18]))	

