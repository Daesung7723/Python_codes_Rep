import ws2812b
import utime

ring_pin = 17 # Mdoule connect pin
numpix   = 8  # Number of RGB lights
# Initialize RGB light halo
strip = ws2812b.ws2812b(numpix, 0, ring_pin)
strip.fill(0,0,0) # Clear RGB buffer
strip.show()      # Refresh display

while True:
    for i in range(numpix): 
        for j in range(5):
            strip.set_pixel(i, 10, 10, 10)
            strip.show()
            utime.sleep(.03)
            strip.set_pixel(i, 0, 0, 0)
            strip.show()
            utime.sleep(.03)

    
    for i in range(numpix): 
        strip.set_pixel(7-i, 10, 10, 10)
        strip.show()
        utime.sleep(.03)
        strip.set_pixel(7-i, 0, 0, 0)
        strip.show()
