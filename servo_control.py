from gpiozero import Servo
from time import sleep
class servo_control(object):
    def __init__(self,ser_h_z):
        self.ser_h_z=ser_h_z
    def move_max(self):
        self.ser_h_z.max()

    def move_mid(self):
        self.ser_h_z.mid()

    def move_min(self):
        self.ser_h_z.mid()

if __name__=='__main__':
    ser_h_z=Servo(27)
    a=servo_control(ser_h_z)#gpio 27,22
    a.move_max()


