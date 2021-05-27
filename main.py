from tkinter import *

class MainScreen:
    def __init__ (self, master):
        background_color = "black"

        self.main_frame = Frame(master, bg = background_color, padx=100, pady=100)
        self.main_frame.grid()

        self.Heading_label = Label(self.main_frame, )


if __name__ == "__main__":
    root = Tk()
    root.title("Quiz on Global Pollution")
    root.mainloop()