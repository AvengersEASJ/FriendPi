import socket
import time
from sense_hat import SenseHat
import re

friendsID = ""
friendName = ""
gender = ""
thirst = ""
hunger =" "
task = ""
fun = ""
dress = ""

def getDataBroadcast ():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    client.bind(("", 4000))
    data  = client.recvfrom(1024) 
    return str(data)

def sendDataBroadcast():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    server.settimeout(0.2)
    server.bind(("", 4999))
    message = friendsID + thirst + hunger + task + fun + dress
    bmessage = str.encode(message)
    server.sendto(bmessage, ('<broadcast>', 5000))


def mainmenu ():
   
    _friendsID, friendName, gender, thirst, hunger, task, fun, _dress, notused1, notused2 = getDataBroadcast().split()
    friendsID = _friendsID.replace("b'", "")
    dress = _dress.replace("\'", "")
    sense = SenseHat()

    g = (0, 255, 0) #green
    s = (0, 0, 0)  #sort
    b = (0, 0, 255) #blue
    y = (255, 255, 0) #yellow
    p = (87, 109, 88) #pigefarve
    

    m_tama = [
      b, b, b, b, b, b, y, y,
      b, b, b, s, s, b, y, y,
      b, b, b, s, s, b, b, b,
      b, s, s, s, s, s, s, b,
      b, b, b, s, s, b, b, b,
      b, b, b, s, s, b, b, b,
      b, b, s, s, s, s, b, b,
      g, g, g, g, g, g, g, g
    ]
 
    f_tama = [
        b, b, b, b, b, b, y, y,
        b, b, b, s, s, b, y, y,
        b, b, b, s, s, b,  b, b,
        b, p, s, s, s, s, p, b,
        b, b, b, s, s, b, b, b,
        b, b, b, s, s, b, b, b,
        b, b, p, p, p, p, b, b,
        g, g, g, g, g, g, g, g
    ]

    num = gender
    if num == False:
        sense.set_pixels(m_tama)
    else:
        sense.set_pixels(f_tama)
  
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    #thirst
    num2 = int(thirst)
    if num2 > 40 and num2 > 70:
        sense.set_pixel(0, 0, green)
    elif num2 > 40:   
        sense.set_pixel(0, 0, yellow)
    else:
        sense.set_pixel(0, 0, red)  
  
  
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    #hunger
    num3 = int(hunger)
    if num3 > 40 and num3 > 70:
        sense.set_pixel(1, 0, green)
    elif num3 > 40:   
        sense.set_pixel(1, 0, yellow)
    else:
        sense.set_pixel(1, 0, red)  

    red = (255, 0, 0)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    #mood
    num4 = int(hunger) + int(thirst) + int(fun)
    if num4 > 120 and num4 > 210:
        sense.set_pixel(3, 1, green)
        sense.set_pixel(4, 1, green)
        sense.set_pixel(3, 2, green)
        sense.set_pixel(4, 2, green)
    elif num4 > 120:   
        sense.set_pixel(3, 1, yellow)
        sense.set_pixel(4, 1, yellow)
        sense.set_pixel(3, 2, yellow)
        sense.set_pixel(4, 2, yellow)
    else:
        sense.set_pixel(3, 1, red)
        sense.set_pixel(4, 1, red)
        sense.set_pixel(3, 2, red)
        sense.set_pixel(4, 2, red)
    sendDataBroadcast()

while True: 
    mainmenu()
    



