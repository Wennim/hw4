import time
import serial
import sys,tty,termios


serdev = '/dev/ttyUSB1'
s = serial.Serial(serdev, 9600)


while(1):
    input_position=str(input("Enter your position: ")).split(",")
    

    if input_position[2]=="west" :
        print("Start!\n")
        input_d2=str((float(input_position[1])+16)*3.35)
        
        command = "/goStraight/run -" + input_d2 + " \n"
        s.write(command.encode())
        time.sleep(2)

        s.write("/stop/run \n".encode())

        s.write("/turn/run 100 0.1 \n".encode())
        time.sleep(1.65)

        s.write("/stop/run \n".encode())

        input_d1=str((float(input_position[0])+19)*3.35)
        command = "/goStraight/run -" + input_d1 + " \n"
        s.write(command.encode())
        time.sleep(2)
        s.write("/stop/run \n".encode())
        print("Done!\n")
    
    elif input_position[2]=="east" :
        print("Start!")
        input_d2=str((float(input_position[1])+6)*3.35)
       
        command = "/goStraight/run -" + input_d2 + " \n"
        s.write(command.encode())
        time.sleep(2)
        s.write("/stop/run \n".encode())

        s.write("/turn/run -100 0.1 \n".encode())
        time.sleep(1.3)
        s.write("/stop/run \n".encode())

        input_d1=str((float(input_position[0]))*3.35)
        command = "/goStraight/run -" + input_d1 + " \n"
        s.write(command.encode())
        time.sleep(2)
        s.write("/stop/run \n".encode())
        print("Done!")


    else :
        print("Start!")
        input_d2=str((float(input_position[1]))*3.35)

        command = "/goStraight/run -" + input_d2 + " \n"
        s.write(command.encode())
        time.sleep(2)
        s.write("/stop/run \n".encode())
        print("Done!")
    
