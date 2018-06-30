#!/usr/bin/python

import cgi,cgitb
import  commands,os
cgitb.enable()

print  "Content-Type:text/html"
print  ""

data=cgi.FieldStorage()
x=data.getvalue('num')

if  x  ==  '1' :
	print  "Get Python prompt"
	commands.getoutput('sudo docker start pycont')
	os.system('sudo docker exec -it pycont   bash -c  "service shellinaboxd status"')
	print  "<a href='https://192.168.10.108:4200'>"
	print   "Get Python Prompt with user name google and password 1"
	print   "</a>"


else :
	print  "nothing"


