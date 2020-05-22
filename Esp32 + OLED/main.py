# notify
print('RUN: main.py')

import os,time
from machine import Pin, SPI
import sdcard
import ssd1306

##############################
### sd card init
##############################

# IOMUX pins for SPI controllers
# Note: Port 1 for 80Mhz (otherwise 40 max)
# Note: Only the first device attaching to the bus can use CS0 pin.
#          HSPI  VSPI
# Pin Name GPIO Number
# CS0*     15     5
# SCLK     14    18
# MISO     12    19
# MOSI     13    23
# QUADWP    2    22
# QUADHD    4    21

# this is for the TTGO-style ESP32 Dev Board
# this is the pinout used for setup
#                     ----
#                    |    | RST
#                    |    | 3V
#                    |    | NC
#                    |    | GND
#                BAT |    | A00 DAC2
#                 EN |    | A01 DAC1 
#                USB |    | A02  G34 IN
#            G13 A12 |    | A03  G39 IN
#            G12 A11 |    | A04  G36 IN
#            G27 A10 |    | A05  G04 
#            G33 A09 |    | SCK  G05 --> CS
#            G15 A08 |    | MOSI G18 --> SCK
#            G32 A07 |    | MISO G19 --> MISO 
#            G14 A06 |    | RX   G16 
#            G22 SCL |    | TX   G17 
#   MOSI <-- G23 DSA |    |      G21 
#                     ----


# spi pins (including cs)
mosi = 23
miso = 19
sck  = 18
cs   =  5

# port
sd = sdcard.SDCard(SPI(2,
                       sck=Pin(sck),
                       mosi=Pin(mosi),
                       miso=Pin(miso)
                       ),
                   Pin(cs,mode=Pin.OUT))

# mount
os.mount(sd,'/sd')
print(os.listdir())

############################
# oled init
############################

oled = ssd1306.SSD1306_128X64_GRID()
oled.port = 1
oled.baudrate *= 8
oled.port_open(test=False)
oled.contrast(0)
oled.flip()

oled.randomflash(1028,0)

oled.frame_clear()
for n in range(4,0,-1):
    for a in range(0,361,45):
        oled.frame_clear()
        oled.ray(64,32,32,a)
        oled.poly(64,32,32,sides=16,start=0,end=a)
        oled.place_text(n,64,32,scale=3,center=True,middle=True,value=1)
        oled.frame_show()
        #time.sleep(0.125)

oled.blank()
time.sleep(1)

oled.frame_clear()
oled.place_text('The',64,32-14,scale=1,center=True,middle=True,value=1)
oled.place_text('Matrix',64,32+7,scale=2,center=True,middle=True,value=1)
oled.frame_show()
oled.fadeinout()

oled.frame_clear()
time.sleep(1)

############################
# play frames
############################

try:

    ftime  = 23.976 # fps
    ftime = int(1000000/ftime)
    t1 = time.ticks_us()

    infile = open('sd/the_matrix.dat',mode='rb')

    fc = 0

    while 1:

        frame = infile.read(1024)

        if not frame:
            break

        fc += 1

        while time.ticks_us() < t1 + (ftime*fc):
            pass

        oled.write(frame)

    infile.close()

except:
    print('STOP VIDEO')

secs = time.ticks_diff(time.ticks_us(),t1)/1000000
print('RATE:',fc,secs,fc/secs)

oled.fadeout()

############################
# done
############################

oled.frame_clear()
oled.place_text('Meanwhile,',64,32-14,scale=1,center=True,middle=True,value=1)
oled.place_text('back at the',64,32,scale=1,center=True,middle=True,value=1)
oled.place_text('batcave ...',64,32+14,scale=1,center=True,middle=True,value=1)
oled.frame_show()
oled.fadeinout()

oled.frame_clear()
oled.place_text('Trouble is',64,32-7,scale=1,center=True,middle=True,value=1)
oled.place_text('brewing!',64,32+7,scale=1,center=True,middle=True,value=1)
oled.frame_show()
oled.fadeinout()

oled.blank()






















