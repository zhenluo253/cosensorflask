from smbus import SMBus
from time import sleep
import _thread
#import time
from flask_cors import CORS, cross_origin
from flask import Flask

bus  = SMBus(1)
app = Flask("__main__")
cors = CORS(app, resources={r"/": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/', methods=['GET','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])

#def safe_exit(signum, frame):
	#exit(1)
#ads7830_commands = [0x84, 0xc4, 0x94, 0xd4, 0xa4, 0xe4, 0xb4,0xf4]
def read_ads7830():
	bus.write_byte(0x4b, 0x84)
	return bus.read_byte(0x4b)
X = ""
def getValue_t(delay):
    global X
    while True:
        value =read_ads7830()
        print(value)
        sleep(delay)
        X = value
_thread.start_new_thread(getValue_t,(1,))
def home():
    global X
    strs = X
    return "{value:" +str(strs)+"}"
CORS(app)
if __name__ == "__main__":
    app.run()
