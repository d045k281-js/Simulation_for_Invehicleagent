from genericpath import exists
import cv2
import requests
import time as sleep
import numpy as np

def play_video(num):
    cap = cv2.VideoCapture('vid'+str(num)+'.mp4')
    window_name = "window"
    # frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps =  cap.get(cv2.CAP_PROP_FPS)
    duration = frame_count/fps
    frame_no =0

    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    while(cap.isOpened()):
        ret,frame = cap.read()
        if ret ==True:

            width = cap.get(cv2.CAP_PROP_FRAME_WIDTH )
            height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT )

            # print(frame_no)
            # if(frame_no==364):
            #     send_request(num)
            # cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)          
            # cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.CV_WINDOW_FULLSCREEN)
            # winname = "Test"
            # cv2.namedWindow(winname)        # Create a named window
            frame = cv2.imshow(window_name, frame)
            cv2.moveWindow(window_name, 1920, 0)
        
            if(cv2.waitKey(10) & 0xFF == ord('q')):
                break
            frame_no += 1
    cap.release()
    cv2.destroyAllWindows

def send_request(num):
    if num==1:
        print("detouring")
        requests.post('https://192.168.1.9:5000/health')
        # print("detouring")
    elif num==2:
        requests.post('http://192.168.1.9:5000/low_alertness')
        print("sending sleepy signal")
    elif num==3:
        requests.post('https://192.168.1.9:5000/anixety')
    elif num==4:
        requests.post('http://192.168.1.9:5000/detournow')
    elif num==3:
        requests.post('https://192.168.1.9:5000/breakdown')

def run_sim(num):
    play_video(num)
    sleep(10)
    print("sending signal")
   

while(1):
    print("\nWelcome to the Simulation!\n\n")
    print("1. Health Emergency\n2. Low Alertness\n3. Experiencing Anxiety/Stress\n4. Detour\n5. Breakdown or Accident\n")
    choice = input('Enter a number to run the corresponding simulation: ')

    if(choice == "1"):
        run_sim(1)
    elif(choice == "2"):
        run_sim(2)
    elif(choice == "3"):
        run_sim(3)
    elif(choice == "4"):
        run_sim(4)
    elif(choice == "5"):
        run_sim(5)
    else:
        print("Invalid input. Try again\n")
