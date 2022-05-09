"""
Object Detection Software for ripe fruit:
Thomas Billington 5/08/21
"""
import cv2
import numpy as np  
from matplotlib import pyplot as plt
import PySimpleGUI as sg
from fruit import Fruit

"""
Creates a color mask that uses HSV files for object detection
uses postprocessing to clean up the image and allow for more
accurate detections
"""
def colorMask(img, lower_lim, upper_lim):
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #coverts BGR values to HSV
    
    mask = cv2.inRange(hsv, lower_lim, upper_lim) 
    
    #kernel used for postprocessing
    kernel = np.ones((5, 5), np.uint8)

    #postprocessing
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.dilate(mask, kernel, iterations=1)

    #returns mask
    return cv2.bitwise_and(img, img, mask=mask)

"""
Creates a GUI that allows the "farmer" to decide which crops he want
to check for ripeness. Future versions will include more fruit. 
"""
def fruit_gui():

    flag = True
    fruit = "Default"

    while(flag == True):

        sg.theme('Kayak') #theme
        #Window view
        layout = [  
            [sg.Text('Choose the ripe fruit you want to find: ')],
            [sg.Button('Banana'), sg.Button('Strawberry'), sg.Button('Apple'), sg.Button('Orange')] 
            ]

        window = sg.Window('Fruit', layout)
        #Events
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED: #closes is x is pressed
                flag = False
                break
            elif event == 'Apple':
                fruit = "Apple"
                flag = False
                break
            elif event == 'Orange':
                fruit = "Orange"
                flag = False
                break
            elif event == 'Strawberry':
                fruit = "Strawberry"
                flag = False
                break
            elif event == 'Banana':
                fruit = "Banana"
                flag = False
                break
        
        window.close()
        return fruit


"""
Main function where video is taken and mask is applied
"""
if __name__ == "__main__": 

    #makes the GUI and gets type of fruit
    gui_val = fruit_gui()

    fruit = Fruit()
    fruit.process_input(gui_val)
    upper_lim = fruit.get_upper()
    lower_lim = fruit.get_lower()

    print("Upper lim: ", upper_lim)
    print("Lower lim: ", lower_lim)

    cv2.namedWindow('Ripeness Tester:')
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv2.imshow('frame', colorMask(frame, lower_lim, upper_lim))

        if cv2.waitKey(1) == ord('q'):
            break
