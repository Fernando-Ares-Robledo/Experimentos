import serial
import time
from datetime import date ,datetime
import requests
import json
url = 'https://api.openweathermap.org/data/2.5/weather?q=Barajas,es&APPID=45e966dd06a788f47a582116cdc79905&units=metric'

ser = serial.Serial('COM3', 9800, timeout=1)
c=0
path = r"C:\Users\Moha\Documents\geiger\datos"
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
    try:
    
    #start = time.time()

        conteos = ser.readline()
        now = datetime.now()
        fecha_hora = now.strftime("%H:%M:%S")  

        
    #time.sleep(0.1)
        if conteos != b"":
        #print("a")
            #Response = requests.get(url)
            #res = response.json()
            print((conteos.decode()))
            file2write=open(filename(),'a') #a append
            file2write.write(conteos.decode()+';'+fecha_hora+";\n")
            file2write.close()

    except:
        print('error')
    #end = time.time()
    #print('tiempo = {}s'.format((end - start)))
