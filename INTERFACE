from tkinter import *
import os
import threading

from PIL import ImageTk



root = Tk()
root.title("CHAT BUCKET")
root.eval('tk::PlaceWindow . center')


b_blue = "#89CFF0"
blue = "#00FFFF"
text_color = "#EAECEE"
font = "Helvetica"




def send():

    enter = Entry(root, bg="#2C3E50", fg=text_color, font=font, width=55)
    enter.grid(row=2, column=0)
    send_button = "You:  " + enter.get()
    



def main():

    top_page = Label(root, bg=b_blue, fg="black", text="Welcome to Chat Bucket!", pady=10, width=20, height=1).grid(row=0) # my top page


    send = Button(root, text="Send", bg=b_blue, command=main).grid(row=2, column=1) # send button

    rectangle = Frame(root, width=600, height=500, bg=b_blue) # rectangle 

    rectangle.grid(row=1, column=0, columnspan=2) # grid

    
    chat_box = Entry(root, bg=b_blue, fg="white",width=55) # chat box
    chat_box.grid(row=2, column=0)


    scrollbar = Scrollbar(rectangle)
    scrollbar.place(relheight=1, relx=0.974)

    root.mainloop()
'''
    logo_image = ImageTk.PhotoImage(file="bucket.png")
    widget_image = Label(rectangle,image=logo_image)
    widget_image.image = logo_image
    widget_image.pack()
'''

    




main()
