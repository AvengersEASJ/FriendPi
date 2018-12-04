
from sense_hat import SenseHat

tama = SenseHat()

g = (0, 255, 0) #green
s = (0, 0, 0)  #sort
b = (0, 0, 255) #blue
y = (255, 255, 0) #yellow
p = (87, 109, 88) #pigefarve
d = (132, 210, 255) #drengfarve

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

num = 1
if num == 0:
 tama.set_pixels(m_tama)
else:
  tama.set_pixels(f_tama)
  
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
#thirst
num2 = 75
if num2 > 40 and num2 > 70:
   tama.set_pixel(0, 0, red)
elif num2 > 40:   
    tama.set_pixel(0, 0, yellow)
else:
  tama.set_pixel(0, 0, green)  
  
  
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
#hunger
num3 = 45
if num3 > 40 and num3 > 70:
   tama.set_pixel(1, 0, red)
elif num3 > 40:   
    tama.set_pixel(1, 0, yellow)
else:
  tama.set_pixel(1, 0, green)  

red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
#mood
num4 = 5
if num4 > 40 and num4 > 70:
   tama.set_pixel(3, 1, red)
   tama.set_pixel(4, 1, red)
   tama.set_pixel(3, 2, red)
   tama.set_pixel(4, 2, red)
elif num4 > 40:   
     tama.set_pixel(3, 1, yellow)
     tama.set_pixel(4, 1, yellow)
     tama.set_pixel(3, 2, yellow)
     tama.set_pixel(4, 2, yellow)
else:
  tama.set_pixel(3, 1, green)
  tama.set_pixel(4, 1, green)
  tama.set_pixel(3, 2, green)
  tama.set_pixel(4, 2, green)