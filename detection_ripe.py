"""
Object Detection Software for ripe fruit:
Thomas Billington 5/08/21
"""
import cv2
import numpy as np  
import PySimpleGUI as sg
from fruit import Fruit

"""
Creates a color mask that uses HSV values for object detection
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
    return mask

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
            [sg.Button('Banana'), sg.Button('Apple'), sg.Button('Orange')] 
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

    #creates fruit object and passes the upper and lower limits of the color range
    fruit = Fruit()
    fruit.process_input(gui_val)
    upper_lim = fruit.get_upper()
    lower_lim = fruit.get_lower()

    #creates a window with the webcam feed
    cv2.namedWindow('Ripeness Tester:')
    cap = cv2.VideoCapture(0)

    while True:
        #reads the camera feed and creates a mask for the color entered
        ret, frame = cap.read()
        cmask = colorMask(frame, lower_lim, upper_lim)

        #finds the contours of the image using the mask
        conts = cv2.findContours(cmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]

        # find the biggest countour
        c_max = max(conts, key = cv2.contourArea)
        x,y,width,height = cv2.boundingRect(c_max)

        # creates a rectangle around the biggest contour
        cv2.rectangle(frame, (x,y), (x+width, y+height), (0,255,0), 2)

        #draws image on main screen
        cv2.imshow(f'Frame: {fruit.get_name()}', frame)
        #shows mask 
        cv2.imshow(f'Mask Frame: {fruit.get_name()}', cmask)

        if cv2.waitKey(1) == ord('q'):
            break

    #close vid stream
    cap.release()
    cv2.destroyAllWindows()
