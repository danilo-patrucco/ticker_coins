from tkinter import Tk, Label, Button

class gui:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")



'''
class gui:

    def __init__(self, data):
        self.data = data

    def print_data_test(self):
        print(self.data['data'][0]['name'], ' USD ', self.data['data'][0]['quote']['USD']['price'])

'''