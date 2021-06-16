import pyb, sensor, image, time, math

enable_lens_corr = False # turn on for straighter lines...
sensor.reset()
sensor.set_pixformat(sensor.RGB565) # grayscale is faster
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()

# All lines also have `x1()`, `y1()`, `x2()`, and `y2()` methods to get their end-points
# and a `line()` method to get all the above as one 4 value tuple for `draw_line()`.

car_stop=0
initial_flag=1

while(True):


   clock.tick()
   img = sensor.snapshot()
   if enable_lens_corr: img.lens_corr(1.8) # for 2.8mm lens...

   # `merge_distance` controls the merging of nearby lines. At 0 (the default), no
   # merging is done. At 1, any line 1 pixel away from another is merged... and so
   # on as you increase this value. You may wish to merge lines as line segment
   # detection produces a lot of line segment results.

   # `max_theta_diff` controls the maximum amount of rotation difference between
   # any two lines about to be merged. The default setting allows for 15 degrees.


   uart = pyb.UART(3,9600,timeout_char=1000)
   uart.init(9600,bits=8,parity = None, stop=1, timeout_char=1000)


   for l in img.find_line_segments(merge_distance = 5, max_theta_diff = 5):
     img.draw_line(l.line(), color = (255, 0, 0))
     if(l.y2()==0 and initial_flag==1 ):
        initial_x2=l.x2()
        initial_flag=0


     elif(l.y1()>2 and l.y1()<20 and l.length()>45 and l.length()<56):
        print("car stop!")
        car_stop=1

        time.sleep(2.5)

        uart.write("/stop/run \n")

        #uart.write("/turn/run 50 0.51\n")
        #time.sleep(0.8)
        #uart.write("/stop/run \n")
     if(l.y2()==0 and car_stop==0):
        print(l)
        diff=(l.x2()-initial_x2)/1000
        if(diff < 0):
          factor=str(-0.47+diff)
        else :
          factor=str(0.47+diff)
        print(factor)

        command="/turn/run 35 " + factor +"\n"

        uart.write(command)
        time.sleep(0.5)

        uart.write("/goStraight/run 35\n")



   print("FPS %f" % clock.fps())

