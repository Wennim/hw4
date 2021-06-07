import time
import serial
import sys,tty,termios


serdev = '/dev/ttyUSB0'
s = serial.Serial(serdev, 9600)


while(1):
    input_position=str(input("Enter your position: ")).split(",")
    print(input_position)

    

    if input_position[2]=="west" :
        input_d2=str((float(input_position[1])+22)*3.35)
        print(input_d2)
        command = "/goStraight/run -" + input_d2 + " \n"
        print(command)
        s.write(command.encode())
        time.sleep(2)
        s.write("/stop/run \n".encode())

        s.write("/turn/run 100 0.1 \n".encode())
        time.sleep(1.5)
        s.write("/stop/run \n".encode())

        input_d1=str((float(input_position[0])+19)*3.35)
        command = "/goStraight/run -" + input_d1 + " \n"
        s.write(command.encode())
        time.sleep(2)
        s.write("/stop/run \n".encode())
    
    else :
        input_d2=str((float(input_position[1])+6)*3.35)
        print(input_d2)
        command = "/goStraight/run -" + input_d2 + " \n"
        print(command)
        s.write(command.encode())
        time.sleep(2)
        s.write("/stop/run \n".encode())

        s.write("/turn/run -100 0.1 \n".encode())
        time.sleep(1.5)
        s.write("/stop/run \n".encode())

        input_d1=str((float(input_position[0]))*3.35)
        command = "/goStraight/run -" + input_d1 + " \n"
        s.write(command.encode())
        time.sleep(2)
        s.write("/stop/run \n".encode())
    
