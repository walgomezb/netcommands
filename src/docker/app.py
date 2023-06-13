import netmiko
import sys
import json
import os
import time
import random
from datetime import datetime


jobInfo = json.loads(sys.argv[1])
inicio = datetime.now()
print("Inicio Request=  " + str(inicio))
print("JobId received: ", jobInfo["id"])
print("Job Information ", sys.argv[1])
espera = random.randint(0, 10)
time.sleep(espera)
print("TiempoEspera Segs= "+ str(espera))

outPath = "/jobsoutput/"+jobInfo["id"]
if not os.path.exists(outPath):
      
    print("directorio creado")
    os.makedirs(outPath)

outFile = outPath + "/out.txt"
f = open(outFile, "w")
f.write("Resultados de comandos")
f.close()
final = datetime.now()
print("Final Request  " + str(final))
