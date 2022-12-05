import tkinter as tk
import socket
import threading


'''
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


# , command=lambda: onchange())  # chat box
chat_box = tk.Entry(root, bg=b_blue, fg="white", width=55)
chat_box.grid(row=2, column=0)


scrollbar = tk.Scrollbar(rectangle)
scrollbar.place(relheight=1, relx=0.974)


# what to do left: Make "you" on right and "Connector" on left
# Make it type out on each side,
# make
'''
'''
    logo_image = ImageTk.PhotoImage(file="bucket.png")
    widget_image = Label(rectangle,image=logo_image)
    widget_image.image = logo_image
    widget_image.pack()
'''


class client:
    def __init__(self):
        self.msg = ''
        self.user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clicks = False
        self.root = tk.Tk()
        self.b_blue = "#89CFF0"
        self.blue = "#00FFFF"
        self.text_color = "#EAECEE"
        self.font = "Helvetica"
        self.send = tk.Button(self.root, text="Send", bg=self.b_blue, command=lambda: self.send())
        self.rectangle = tk.Text(self.root, width=60, height=50, bg=self.b_blue)  # rectangle
        self.chat_box = tk.Entry(self.root, bg=self.b_blue, fg="black", width=55)
        self.scrollbar = tk.Scrollbar(self.rectangle)
        self.Switch = False

    def creation(self):
        self.top_page = tk.Label(self.root, bg=self.b_blue, fg="black",
                                 text="Welcome to Chat Bucket!", pady=1, padx=1, height=1).grid(row=0)
        self.root.title("CHAT BUCKET")
        self.root.eval('tk::PlaceWindow . center')
        self.root.resizable(width=tk.FALSE, height=tk.FALSE)
        self.send.grid(row=2, column=1)
        self.root.bind('<Return>', lambda event: self.onclick(1))
        self.rectangle.config(state=tk.DISABLED)
        self.rectangle.grid(row=1, column=0, columnspan=2)  # grid
        self.chat_box.grid(row=2, column=0)
        self.scrollbar.place(relheight=1, relx=0.974)

    def send(self):
        self.Switch = True

    def onclick(self, args):  # send button
        self.msg = self.chat_box.get()
        print(self.msg)
        while True:
            if self.msg.lower() == "terminate":
                self.user.close()
            if len(self.msg) > 0:
                break
            if len(self.msg) == 0:
                return False
        self.rectangle.config(state=tk.NORMAL)
        self.rectangle.insert(tk.END, "\n" + "YOU:" + str(self.msg))
        self.rectangle.config(state=tk.DISABLED)
        self.chat_box.delete(0, tk.END)

    def Nsending(self):
        while True:
            if self.Switch is True:
                if self.onclick(1) != False:
                    try:
                        self.user.send(bytes(self.msg, encoding='ascii'))
                        self.Switch = False
                    except:
                        print("SEND ERROR")
                        self.user.close()
                        return False

    def Nrec(self):
        while True:
            try:
                rmsg = self.user.recv(1024)
                if len(rmsg) == 0:
                    return
                self.rectangle.config(state=tk.NORMAL)
                self.rectangle.insert(tk.end, '\n' + str(rmsg, encoding='utf-8'))
                self.rectangle.config(state=tk.DISABLED)
            except:
                print("RECIEVE ERROR")
                self.user.close()
                return False

    def start(self, IP, PORT):
        self.creation()
        addr = (IP, PORT)
        try:
            self.user.connect(addr)
        except:
            print("Unable to reach HOST")
            return
        # print('connect')
        self.thread = threading.Thread(target=self.Nrec)
        self.thread2 = threading.Thread(target=self.Nsending)
        self.creation()
        self.thread.start()
        self.thread2.start()


gui = client()
gui.start('10.109.82.235', 444)

gui.root.mainloop()
