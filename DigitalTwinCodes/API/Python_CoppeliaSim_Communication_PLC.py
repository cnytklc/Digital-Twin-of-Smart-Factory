import sim
import serial
# import random
# from firebase import firebase
from HslCommunication import MelsecMcNet
from HslCommunication import SoftBasic
import time


# firebase = firebase.FirebaseApplication("https://coppelia-112e5-default-rtdb.firebaseio.com/", None)
arduino = serial.Serial(port='COM8', baudrate=9600, timeout=.1)

if __name__ == "__main__":
    print(SoftBasic.GetUniqueStringByGuidAndRandom())
    melsecNet = MelsecMcNet("192.168.1.10", 4001)


def printReadResult(result):
    if result.IsSuccess:
        print(f"{int((result.Content - 300) / 50)} C")
def printReadResult2(result2):
    if result2.IsSuccess:
        print(f"{((result2.Content))}")


clientID = sim.simxStart('127.0.0.1', 19999, True, True, 500, 5)  # Connect to CoppeliaSim


def printTemp3(temp3, temp2):
    print(f"{int(((temp3.Content - 300) / 50) + ((temp2.Content - 300) / 50)) / 2} C")


def send_command(command):
    arduino.write(f"{command:.0f}".encode())
    

while True:
    a=sim.simxGetFloatSignal(clientID,"velocity_data1",sim.simx_opmode_oneshot)

    send_command(a[1])
    x1 = melsecNet.ReadInt32("D0")  ##to content
    x2 = melsecNet.ReadInt32('D5')
    Ps_x0=melsecNet.ReadBool("X0")
    Ps_x1=melsecNet.ReadBool("X1")
    Ps_x2=melsecNet.ReadBool("X2")
    Ps_x3=melsecNet.ReadBool("X3")
    print('Temperature 1 :')
    printReadResult(x1)
    print('Temperature 2 :')
    printReadResult(x2)
    print('Proximity0,1,2,3 :')
    printReadResult2(Ps_x0)
    printReadResult2(Ps_x1)
    printReadResult2(Ps_x2)
    printReadResult2(Ps_x3)
    print('Temperature 3 :')
    printTemp3(x1, x2)
    
    

    
        # Read a line from the serial port
   
    line = arduino.readline().decode('utf-8').strip()
    if line:
        print("Received data:", line)
    
        time.sleep(1)  # Adjust the delay as needed
    #---------------------------------------------------------------------------------------------
        
    
    # _, signal = sim.simxGetFloatSignal(clientID, 'data', sim.simx_opmode_oneshot)

    # print(signal)

    # result = firebase.get('https://coppelia-112e5-default-rtdb.firebaseio.com/1', '')

    # value = result
    
    # print(value)
    # Sending signal from Firebase to CoppeliaSim
    # Random = random.randint(5,85)
    #----------------------------------------------------------------------------------------------    

    #temperature
    temp3 = float(((((x1.Content - 300) / 50) + ((x1.Content - 299) / 50))) / 2)
    temp_3_1= "{:.2f}".format(temp3)
    sim.simxSetStringSignal(clientID, "data_signal1", str((x1.Content - 300) / 50), sim.simx_opmode_blocking)
    sim.simxSetStringSignal(clientID, "data_signal2", str((x1.Content - 299) / 50), sim.simx_opmode_blocking)
    sim.simxSetStringSignal(clientID, "data_signal3",str(temp_3_1),sim.simx_opmode_blocking)
    
    #Proximity
    sim.simxSetStringSignal(clientID, "Ps_signal0", str(Ps_x0.Content), sim.simx_opmode_blocking)
    sim.simxSetStringSignal(clientID, "Ps_signal1", str(Ps_x1.Content ), sim.simx_opmode_blocking)
    sim.simxSetStringSignal(clientID, "Ps_signal2", str(Ps_x2.Content ), sim.simx_opmode_blocking)
    sim.simxSetStringSignal(clientID, "Ps_signal3", str(Ps_x3.Content ), sim.simx_opmode_blocking)
    #velocity
    if arduino.readline().decode('utf-8').strip():
      sim.simxSetStringSignal(clientID, "velocity_data", str(line), sim.simx_opmode_blocking)
      
    time.sleep(1)

    # firebase.post("Conveyor Velocity in CoppeliaSim: ", Random)



