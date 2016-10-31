import microbit
from microbit import uart

while(True):
    if(uart.any()):
        input = uart.read(1)
        print("Got " + str(input))#was for debugging
        #if first character from input(message) is '1' set light to 9 brightest
        #otherwise if anything else (including '0') set lite to 0 - effectively off
        if(chr(input[0]) == '1'): light = 9
        else: light = 0
        #turn on microbit display
        microbit.display.on()
        #Displays Heart when recieving message ON - using variable light in place of manual setting
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
    
        #for all LEDs on
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

