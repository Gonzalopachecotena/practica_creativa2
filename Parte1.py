#! /usr/bin/python

#GONZALO PACHECO TENA
#MIGUEL ESTEBAN GUTIÉRREZ
#SERGIO CALDERÓN CÁMARA

#Importamos las librerias necesarias
from subprocess import call
import sys
import subprocess
import json
import os

GROUP_NUMBER = os.environ['GROUP_NUMBER']

call(["sudo apt-get update"], shell=True)
call(["sudo apt-get install python3-pip"], shell=True)
call(["sudo git clone https://github.com/CDPS-ETSIT/practica_creativa2.git"], shell=True)
call(["pip install -r practica_creativa2/bookinfo/src/productpage/requirements.txt"], shell=True)
f1=open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html",'r')
f2=open("productpage.html",'w')
for line in f1:
    if"Simple Bookstore App" in line:
        f2.write(line.replace("Simple Bookstore App", "Simple Bookstore App" + GROUP_NUMBER))
    else: 
        f2.write(line)
f2.close()
f1.close()
call(["sudo cp -r productpage.html practica_creativa2/bookinfo/src/productpage/templates"], shell=True)
call(["python3 practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 1500"], shell=True)


