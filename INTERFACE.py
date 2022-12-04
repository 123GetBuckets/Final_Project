import tkinter as tk

# from PIL import ImageTk


root = tk.Tk()
root.title("CHAT BUCKET")
root.eval('tk::PlaceWindow . center')


b_blue = "#89CFF0"
blue = "#00FFFF"
text_color = "#EAECEE"
font = "Helvetica"

root.resizable(width=tk.FALSE, height=tk.FALSE)


def creation():

    top_page = tk.Label(root, bg=b_blue, fg="black",
                        text="Welcome to Chat Bucket!",
                        pady=1, padx=1, height=1).grid(row=0)  # my top page


send = tk.Button(root, text="Send", bg=b_blue, command=lambda: onclick(1))
send.grid(row=2, column=1)

root.bind('<Return>', lambda event: onclick(1))

rectangle = tk.Text(root, width=60, height=50, bg=b_blue)  # rectangle
rectangle.config(state=tk.DISABLED)
rectangle.grid(row=1, column=0, columnspan=2)  # grid


chat_box = tk.Entry(root, bg=b_blue, fg="white", width=55)  # chat box
chat_box.grid(row=2, column=0)


scrollbar = tk.Scrollbar(rectangle)
scrollbar.place(relheight=1, relx=0.974)


def onclick(args):
    text = chat_box.get()
    if len(text) != 0:
        if args == 1:
            rectangle.config(state=tk.NORMAL)
            rectangle.insert(tk.END, "\n" + "YOU:" + str(text))
            rectangle.config(state=tk.DISABLED)
        chat_box.delete(0, tk.END)


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
