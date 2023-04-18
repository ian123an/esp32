import esp32
import time

while True:
    hall = esp32.hell_sensor()
    print(hall)
    
    if(hall<100 and hall>0):
        print("收藏盒已開啟")
    time.sleep(0.1)
