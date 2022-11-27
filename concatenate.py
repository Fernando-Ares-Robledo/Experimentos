#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
#   Python version-3.9.1
#   November 27, 2020 23:16:59 PM CET  platform: Windows NT
#   Author: Fernando Ares Robledo
#           
#   Mail: fernandoaresrobledo@gmail.com

import serial
import time
from datetime import date ,datetime
import requests
import json
key =""
url = 'https://api.openweathermap.org/data/2.5/weather?q=Barajas,es&APPID={}'.format(key)

ser = serial.Serial('COM4', 9800, timeout=1)
c=0
path = r"C:\Users\yo\Documents\geiger\datos"
now = datetime.now()
fecha_dia = now.strftime("%d/%m/%Y")
# %H:%M:%S
filename = str("datos_dia_")+fecha_dia
print(filename)
print()
print(now.strftime("%d"))
print('*****---*****')

dia =  now.strftime("%d")
time.sleep(1)

def filename():
    now = datetime.now()
    fecha_dia = now.strftime("%d/%m/%Y")
    filename = path+'/' + str("datos_dia_")+fecha_dia.replace("/","-")+".txt"
    return filename

while True:
    
    #start = time.time()

    conteos = ser.readline()
    now = datetime.now()
    fecha_hora = now.strftime("%H:%M:%S")  

        
    #time.sleep(0.1)
    if conteos != b"":
        #print("a")
        response = requests.get(url)
        res = response.json()
        print((conteos.decode()))
        file2write=open(filename(),'a') #a append
        file2write.write(conteos.decode()+fecha_hora+";"+ response+";\n")
        file2write.close()

        
    #end = time.time()
    #print('tiempo = {}s'.format((end - start)))
