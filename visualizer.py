import serial
import binascii
import matplotlib.pyplot as plt
import math

class LidarData:
    def __init__(self,FSA,LSA,CS,Speed,TimeStamp,Confidence_i,Angle_i,Distance_i):
        self.FSA = FSA
        self.LSA = LSA
        self.CS = CS
        self.Speed = Speed
        self.TimeStamp = TimeStamp
        self.Confidence_i = Confidence_i
        self.Angle_i = Angle_i
        self.Distance_i = Distance_i

def CalcLidarData(str):
    str = str.replace(' ','')
    Speed = int(str[2:4]+str[0:2],16)/100
    FSA = float(int(str[6:8]+str[4:6],16))/100
    LSA = float(int(str[-8:-6]+str[-10:-8],16))/100
    TimeStamp = int(str[-4:-2]+str[-6:-4],16)
    CS = int(str[-2:],16)
    Confidence_i = list()
    Angle_i = list()
    Distance_i = list()
    count = 0
    if(LSA-FSA > 0):
        angleStep = float(LSA-FSA)/(12)
    else:
        angleStep = float((LSA+360)-FSA)/(12)
    counter = 0
    circle = lambda deg : deg - 360 if deg >= 360 else deg
    for i in range(0,6*12,6): 
        Distance_i.append(int(str[8+i+2:8+i+4] + str[8+i:8+i+2],16)/100)
        Confidence_i.append(int(str[8+i+4:8+i+6],16))
        Angle_i.append(circle(angleStep*counter+FSA)*math.pi/180.0)
        counter += 1
    lidarData = LidarData(FSA,LSA,CS,Speed,TimeStamp,Confidence_i,Angle_i,Distance_i)
    #print (" Distance_i=" ,Distance_i)
    #print (" Confidence_i=" ,Confidence_i)
    return lidarData

def assign_color(value):
    if value < 50 or value > 255:
        return "White"
    elif value <= 85:
        return "Red"
    elif value <= 120:
        return "Orange"
    elif value <= 155:
        return "Yellow"
    elif value <= 190:
        return "Green"
    elif value <= 225:
        return "Blue"
    elif value <= 240:
        return "Indigo"
    else:
        return "White"

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='polar')
ax.set_title('lidar (exit: Key E)',fontsize=18)
plt.connect('key_press_event', lambda event: exit(1) if event.key == 'e' else None)
ser = serial.Serial(port='/dev/ttyUSB0',baudrate=230400,timeout=5.0,bytesize=8,parity='N',stopbits=1)
tmpString = ""
lines = list()
angles = list()
distances = list()
confidences = list()
colors = list()
i = 0
while True:
    loopFlag = True
    flag2c = False
    if(i % 40 == 39):
        if('line' in locals()):
            line.remove()
        colors = [assign_color(confidence) for confidence in confidences]
        line = ax.scatter(angles, distances, c=colors, s=5)
        ax.set_theta_offset(math.pi / 2)
        plt.pause(0.01)
        angles.clear()
        distances.clear()
        confidences.clear()
        colors.clear()
        i = 0
        
    while loopFlag:
        b = ser.read()
        tmpInt = int.from_bytes(b, 'big')
        if (tmpInt == 0x54):
            tmpString +=  b.hex()+" "
            flag2c = True
            continue
        elif(tmpInt == 0x2c and flag2c):
            tmpString += b.hex()
            if(not len(tmpString[0:-5].replace(' ','')) == 90 ):
                tmpString = ""
                loopFlag = False
                flag2c = False
                continue
            lidarData = CalcLidarData(tmpString[0:-5])
            angles.extend(lidarData.Angle_i)
            distances.extend(lidarData.Distance_i)
            confidences.extend(lidarData.Confidence_i)
            tmpString = ""
            loopFlag = False
        else:
            tmpString += b.hex()+" "
        flag2c = False
    i +=1

ser.close()
