from tkinter import *
import random

root = Tk()
root.config(bg = "#ffffff")
root.geometry("400x400")

ran_name = Label(root, font = ("Corbel Light", 50), bg = "white")
ran_name.place(relx = 0.5, rely = 0.35,anchor = CENTER)
schore = Label(root, text = "Score : 0", font = ("Lucida Handwriting", 10))
schore.place(relx =0.05, rely = 0.05, anchor = W)
anser = Entry(root)
anser.place(relx = 0.5, rely = 40, anchor = CENTER)

class game:
    def __init__(self):
        self.__score = 0
        self.color = ["white","Yellow","Blue","Red","Green","Black","Brown","Silver","Purple","green","Gray","Orange","Maroon","Aquamarine","Wheat","Lime","Crimson", "pink","Magenta","Plum","Olive","Cyan"]
        self.text = self.color
    def updateGame(self):
        self.rand = random.randint(0, 22)
        ran_name["text"] = self.text[self.rand]
        ran_name["fg"] = self.color[self.rand]
        
obj = game()


btn = Button(root, text = "Start", command = obj.updateGame, bg = "Dark olive green", fg = "white", relief = FLAT, padx = 10, pady = 1, font = ("Arial", 15))
btn.pack()

root.mainloop()