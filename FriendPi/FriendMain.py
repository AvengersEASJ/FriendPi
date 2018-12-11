import socket
import time
from time import sleep
from sense_hat import SenseHat


def getDataBroadcast ():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    client.bind(("", 4000))
    data  = client.recvfrom(1024) 
    return str(data)



def apple():

    apple = SenseHat()
  
    r = (255, 0, 0)
    g = (0, 255, 0)

    apple.clear
    apple1 = [
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, r, r, r, r, g, g,
        g, g, r, r, r, r, g, g,
        g, g, r, r, r, r, g, g,
        g, g, r, r, r, r, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g
    ]
    
    for event in apple.stick.get_events():
        if event.action == "pressed":
            apple.set_pixels(apple1)
            if event.direction == "up":
                apple.set_pixel(4, 3, g)
                apple.set_pixel(4, 2, g)
                apple.set_pixel(5, 3, g)
                apple.set_pixel(5, 2, g)
        
                sleep(0.8)
        
            if event.direction == "up":
                apple.set_pixel(3, 3, g)
                apple.set_pixel(3, 2, g)
                apple.set_pixel(2, 3, g)
                apple.set_pixel(2, 2, g)
          
                sleep(0.8)
          
            if event.direction == "up":
                apple.set_pixel(2, 4, g)
                apple.set_pixel(2, 5, g)
                apple.set_pixel(3, 4, g)
                apple.set_pixel(3, 5, g)
            
                sleep(0.8)
          
            if event.direction == "up":
                apple.set_pixel(4, 4, g)
                apple.set_pixel(4, 5, g)
                apple.set_pixel(5, 4, g)
                apple.set_pixel(5, 5, g)

def mainmenu ():
   
    _friendsID, friendName, gender, thirst, hunger, task, fun, degrees, _dress, notused1, notused2 = getDataBroadcast().split()
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
      s, s, s, s, s, s, s, s,
    ]
 
    f_tama = [
        b, b, b, b, b, b, y, y,
        b, b, b, s, s, b, y, y,
        b, b, b, s, s, b,  b, b,
        b, p, s, s, s, s, p, b,
        b, b, b, s, s, b, b, b,
        b, b, b, s, s, b, b, b,
        b, b, p, p, p, p, b, b,
        s, s, s, s, s, s, s, s,
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

    if  int(degrees) > 20:
        sense.set_pixel(0, 7, green)
        sense.set_pixel(0, 7, green)
        sense.set_pixel(0, 7, green)
        sense.set_pixel(0, 7, green)
        sense.set_pixel(0, 7, green)
        sense.set_pixel(0, 7, green)
        sense.set_pixel(0, 7, green)
        sense.set_pixel(0, 7, green)
    elif int(degrees) > 10 and degrees < 20:   
        sense.set_pixel(1, 8, b)
        sense.set_pixel(2, 8, b)
        sense.set_pixel(3, 8, b)
        sense.set_pixel(4, 8, b)
        sense.set_pixel(5, 8, b)
        sense.set_pixel(6, 8, b)
        sense.set_pixel(7, 8, b)
        sense.set_pixel(8, 8, b)

    else:
        sense.set_pixel(0, 7, p)
        sense.set_pixel(1, 7, p)
        sense.set_pixel(2, 7, p)
        sense.set_pixel(3, 7, p)
        sense.set_pixel(4, 7, p)
        sense.set_pixel(5, 7, p)
        sense.set_pixel(6, 7, p)
        sense.set_pixel(7, 7, p)

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    server.settimeout(0.2)
    server.bind(("", 5000))
    message = friendsID + " " + thirst + " " + hunger + " " + task + " " + fun + " " + dress
    server.sendto(message.encode(), ('<broadcast>', 5000))
    
    apple()
    hunger + 20



while True: 
    mainmenu()
    
    



