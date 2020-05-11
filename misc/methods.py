import requests
import json

def changeCol(id, colour, saturation, brigthness, ip, user):
    payload = {"on":True, "sat":saturation, "bri":brigthness, "xy":colour}
    r = requests.put(f"http://{ip}/api/{user}/lights/{id}/state", data=json.dumps(payload, separators=(',', ':')))
    return print(f"Completing colour change for light {id}")

def changeBrightness(id, var, ip, user):
    payload = {"on":True, "bri":var}
    r = requests.put(f"http://{ip}/api/{user}/lights/{id}/state", data=json.dumps(payload, separators=(',', ':')))
    return print(f"Completing brightness change for light {id}")

from misc.converter import ColorHelper, GamutB

convert = ColorHelper(GamutB)

def getColImage(r, g, b):
    link = f"http://singlecolorimage.com/get/{convert.rgb_to_hex(r, g, b)}/200x200"
    return link

def getColNameByRGB(r, g, b):
    r = requests.get(f"http://www.thecolorapi.com/id?rgb={r},{g},{b}")
    return r.json()['name']['value']

def rgbToHex(r, g, b):
    return convert.rgb_to_hex(r,g,b)

def turnOn(ip, user, id):
    payload = {"on":True}
    r = requests.put(f"http://{ip}/api/{user}/lights/{id}/state", data=json.dumps(payload, separators=(',', ':')))
    return print(f"Turned light on!")

def turnOff(ip, user, id):
    payload = {"on":False}
    r = requests.put(f"http://{ip}/api/{user}/lights/{id}/state", data=json.dumps(payload, separators=(',', ':')))
    return print(f"[Light Controller] Light {id} turned off!")
