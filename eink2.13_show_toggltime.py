import time
from Epaper import *
from PIL import Image #Pillow
import toggl_python
import os 

# Demo Configuration
X_PIXEL = 128
Y_PIXEL = 250
RED_CH = True # If the module has only two colors(B&W), please set it to False.

toggl_python.get_total_time_per_day_and_create_image() #making image

print("Flash Image")
f = Image.open(os.path.dirname(os.path.abspath(__file__)) + '/test.png')
f = f.convert('RGB') # conversion to RGB
data = f.load()

rBuf = [0] * 4000
bBuf = [0] * 4000

for y in range(250):
    for x in range(128):
       # Red CH
       #rが122より大きくてg,bが122より小さい時、画像は赤に近い色を持っていると判断して赤を表示するようにする
       if data[x,y][0] >= 120 and data[x,y][1] <= 200 and data[x,y][2] <= 200 and RED_CH is True:
           # This algorithm has bugs if ported according to C, the solution is referred to:https://www.taterli.com/7450/
           index = int(16 * y + (15 - (x - 7) / 8))
           tmp = rBuf[index]
           rBuf[index] = tmp | (1 << (x % 8))
       # Black CH
       elif data[x,y] == (255,255,255):
            index = int(16 * y + (15 - (x - 7) / 8))
            tmp = bBuf[index]
            bBuf[index] = tmp | (1 << (x % 8))

e = Epaper(X_PIXEL,Y_PIXEL)
if RED_CH is True:
    e.flash_red(buf=rBuf)
e.flash_black(buf=bBuf)
e.update()
