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
root.resizable(width=FALSE, height=FALSE)


def creation():

    top_page = Label(root, bg=b_blue, fg="black", text="Welcome to Chat Bucket!", pady=1, padx=1, height=1).grid(row=0) # my top page

send = Button(root, text="Send", bg=b_blue, command=lambda:onclick(1)) # send button
send.grid(row=2, column=1)

rectangle = Text(root, width=60, height=50, bg=b_blue) # rectangle 
rectangle.config(state=DISABLED)
rectangle.grid(row=1, column=0, columnspan=2) # grid


chat_box = Entry(root, bg=b_blue, fg="white",width=55) # chat box
chat_box.grid(row=2, column=0)


scrollbar = Scrollbar(rectangle)
scrollbar.place(relheight=1, relx=0.974)

def onclick(args): 
    text = chat_box.get()
    if args  == 1:
        rectangle.config(state=NORMAL)
        rectangle.insert(END, "\n" + "YOU:" + str(text))
        rectangle.config(state=DISABLED)
    chat_box.delete()



def main():
    creation()
    onclick(args=1)

main()




root.mainloop()

    
# what to do left: Make "you" on right and "Connector" on left
# Make it type out on each side, 
# make 

'''
    logo_image = ImageTk.PhotoImage(file="bucket.png")
    widget_image = Label(rectangle,image=logo_image)
    widget_image.image = logo_image
    widget_image.pack()
'''




    
