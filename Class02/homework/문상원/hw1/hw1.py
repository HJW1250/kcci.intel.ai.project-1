from iotdemo import FactoryController
import time




with FactoryController("/dev/ttyACM0") as ctrl:
    input=int(input())

    if input==1:
        ctrl.system_start()


    elif input==2:
        ctrl.system_stop()
    
    elif input==3:
        ctrl.__led(2,True)



    elif input==4:
        ctrl.__led(3,True)



    elif input==5:
        ctrl.__led(4,True)

ctrl.close()
