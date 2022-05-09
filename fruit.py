"""
Ripe Fruit Values
Thomas Billington
5/9/22
"""
import numpy as np  

class Fruit:

    def __init__(self):
        self.upper = np.zeros(3)
        self.lower = np.zeros(3)
        self.name = 'Default'

    #sets the fruit object to be a banana with specific color range
    def set_banana(self):
        self.lower = np.array([69,49,76])
        self.upper = np.array([52,71,76])
        self.name = "Banana"

    #sets the fruit object to be an orange with specific color range
    def set_orange(self):
        self.lower = np.array([47,87,76])
        self.upper = np.array([33,86,76])
        self.name = "Orange"

    #sets the fruit object to be an apple with specific color range
    def set_apple(self):
        self.lower = np.array([7,65,76])
        self.upper = np.array([14,98,76])
        self.name = "Apple"

    #sets the fruit object to be a strawberry with specific color range
    def set_strawberry(self):
        self.lower = np.array([15,53,76])
        self.upper = np.array([14,98,76])
        self.name = "Strawberry"

    #processing the user input to determine the fruit and set fruit information
    def process_input(self, input):
        if (input == "Strawberry"):
            self.set_strawberry()
            print("Fruit is: ", self.name)

        elif (input == "Banana"):
            self.set_banana()
            print("Fruit is: ", self.name)

        elif (input == "Apple"):
            self.set_apple()
            print("Fruit is: ", self.name)

        elif (input == "Orange"):
            self.set_orange()
            print("Fruit is: ", self.name)

    #gets the upper array for the HSV values
    def get_upper(self):
        return self.upper

    #gets the upper array for the HSV values
    def get_lower(self):
        return self.lower
    
    #gets the name of the fruit being monitored
    def get_name(self):
        return self.name