import netmiko
import sys
import json
import os


jobInfo = json.loads(sys.argv[1])
print("JobId received: ", jobInfo["id"])
print("Job Information", sys.argv[1])

print("App started failed", file=sys.stderr)


outPath = "/jobsoutput/"+jobInfo["id"]
if not os.path.exists(outPath):
      
    print("directorio creado")
    os.makedirs(outPath)

outFile = outPath + "/out.txt"
f = open(outFile, "w")
f.write("Resultados de comandos")
f.close()

