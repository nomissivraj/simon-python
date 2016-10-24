import microbit
from microbit import uart

while(True):
    if(uart.any()):
        input = uart.read(1)
        print("Got " + str(input))
        if(chr(input[0]) == '1'): light = 9
        else: light = 0
        microbit.display.on()
        #this lot flashes a heart
        microbit.display.set_pixel(1,0,light)
        microbit.display.set_pixel(3,0,light)
        microbit.display.set_pixel(0,1,light)
        microbit.display.set_pixel(2,1,light)
        microbit.display.set_pixel(4,1,light)
        microbit.display.set_pixel(0,2,light)
        microbit.display.set_pixel(4,2,light)
        microbit.display.set_pixel(1,3,light)
        microbit.display.set_pixel(3,3,light)
        microbit.display.set_pixel(2,4,light)
    
        #this lot flashes all LEDs
        #microbit.display.set_pixel(0,0,light)
        #microbit.display.set_pixel(0,1,light)
        #microbit.display.set_pixel(0,2,light)
        #microbit.display.set_pixel(0,3,light)
        #microbit.display.set_pixel(0,4,light)
        #microbit.display.set_pixel(1,0,light)
        #microbit.display.set_pixel(1,1,light)
        #microbit.display.set_pixel(1,2,light)
        #microbit.display.set_pixel(1,3,light)
        #microbit.display.set_pixel(1,4,light)
        #microbit.display.set_pixel(2,0,light)
        #microbit.display.set_pixel(2,1,light)
        #microbit.display.set_pixel(2,2,light)
        #microbit.display.set_pixel(2,3,light)
        #microbit.display.set_pixel(2,4,light)
        #microbit.display.set_pixel(3,0,light)
        #microbit.display.set_pixel(3,1,light)
        #microbit.display.set_pixel(3,2,light)
        #microbit.display.set_pixel(3,3,light)
        #microbit.display.set_pixel(3,4,light)
        #microbit.display.set_pixel(4,0,light)
        #microbit.display.set_pixel(4,1,light)
        #microbit.display.set_pixel(4,2,light)
        #microbit.display.set_pixel(4,3,light)
        #microbit.display.set_pixel(4,4,light)

