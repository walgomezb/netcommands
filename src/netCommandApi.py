from flask import Flask
import docker
from docker.types import LogConfig
import json
import binascii
import os

app = Flask(__name__)


@app.route('/executeNetDeviceCommands',methods=['GET'])
def executeNetDeviceCommands():
    jobId = binascii.b2a_hex(os.urandom(10))
    jobId = jobId.decode('utf-8')

    IMAGE_NAME = "netcommand"
    #client = docker.from_env()
    #client = docker.DockerClient(base_url='unix:///Users/wagomez/.docker/run/docker.sock')
    #client = docker.DockerClient(base_url='ssh://centosDocker')
    client = docker.from_env()
    lc = LogConfig(type=LogConfig.types.JSON, config={
    'max-size': '1g',
    })
    instanceName = "netcommand"+str(jobId)

    jobInfo = {
        "id": jobId,
        "routers": [ {"ip": "ip1", "cta": "cta1", "password": "pass1", 
                    "commands":["show run", "show int bri"]
                    }

        ]
    }

    jobInfo = json.dumps(jobInfo)


    containerNetcommand = client.containers.run(image=IMAGE_NAME, detach=False,
                                                                name=instanceName,
                                                                auto_remove=True,
                                                                #volumes_from='webstreamLive',
                                                                #command="streamlink -l info --http-header streamtype=live --http-proxy http://proxyDevOps:8881/ hls://"+urlClient+" best -f -o /webstore/cont"+instance+".ts"
                                                                log_config = lc,
                                                                stderr = True,
                                                                stdout = True,
                                                                command = "'"+jobInfo+"'",
                                                                volumes_from='voljobsoutput'
                                                                )


    #containerNetcommand.wait()
    #print ("termino")
    #print(containerNetcommand)
    return containerNetcommand


if __name__ == '__main__':

    app.run(host="0.0.0.0", port=8051)