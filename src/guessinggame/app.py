"""
A simple guessing game built with beeware
"""
from random import randint
from functools import partial
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER


class GuessingGame(toga.App):

    def startup(self):
        
        main_box = toga.Box(style=Pack(direction=COLUMN,alignment=CENTER))

        box1 = toga.Box(style=Pack(padding=5))
        self.lab1 = toga.Label("Welcome to the guessing game with Jesse 😎",style=Pack(alignment=CENTER))

        box1.add(self.lab1)

        range_box = toga.Box(style=Pack(direction=COLUMN,padding=10))
        self.start_range = toga.Label("Enter the first digit: ", style=Pack(width=0.25))
        self.start_in = toga.TextInput(style=Pack(width=0.25, padding_top=7))
        #self.start_in.value = int(self.start_in.value)
        self.end_range = toga.Label("Enter the limit of our guess: ", style=Pack(width=0.25, padding_top=7))
        self.end_on = toga.TextInput(style=Pack(width=0.25, padding_top=7))
        #self.end_on.value = int(self.end_on.value)

        self.textin = toga.Label("Enter your guess: ", style=Pack(padding_top=15))
        self.ask = toga.TextInput(style=Pack(width=0.25,padding_top=7))


        sub_num = toga.Button("Submit", style=Pack(padding_top=30),on_press=partial(self.display_results))

        range_box.add(self.start_range,self.start_in,self.end_range,self.end_on,self.textin,self.ask,sub_num)





        #box2 = toga.Box(style=Pack(padding=5, direction=COLUMN,alignment=CENTER))
        #self.lab2 = toga.Label("Guess a number from 1 to 10", style=Pack(alignment=CENTER))
        #self.textin1 = toga.TextInput(style=Pack(padding=(5,0,0,5),alignment=CENTER))
        
        

        #box2.add(self.lab2,self.textin1,sub_num)

        box3 = toga.Box(style=Pack(direction=COLUMN,padding=5, alignment=CENTER))
        self.lab3 = toga.Label("",style=Pack(alignment=CENTER, padding=5))
        self.lab4 = toga.Label("", style=Pack(alignment=CENTER, padding=5))
        self.lab5 = toga.Label("", style=Pack(alignment=CENTER, padding=5))

        box3.add(self.lab3,self.lab4,self.lab5)



        main_box.add(box1,range_box,box3)


        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def display_results(self, widget):
        """Function to display the numbers"""
        

        try:
            number = randint(int(self.start_in.value),int(self.end_on.value))
            number = int(number)

            self.lab3.text = f"Your number is {self.ask.value}"
            self.lab4.text = f"And the correct number is {number}"
            if int(self.ask.value) == number:
                self.lab5.text = f"Congrats, you got the right number 🎊🎊"
            elif int(self.ask.value) != number:
                self.lab5.text = f"Sorry, you got the wrong number...Try again"
            else:
                self.lab5.text = f"Please make sure you typed an integer"
        except:
            ValueError
            self.lab3.text = f"Please enter a number 🙄"
            self.lab4.text = ""
            self.lab5.text = ""
        
        

        


def main():
    return GuessingGame()
