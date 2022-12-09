import tkinter as tk
import pygame

#VERSION WITH MUSIC!!!! *CREATED BUGS*

root = tk.Tk()
root.title("CHAT BUCKET")
root.eval('tk::PlaceWindow . center')


b_blue = "#89CFF0"
blue = "#00FFFF"
text_color = "#EAECEE"
font = "Helvetica"

root.resizable(width=tk.FALSE, height=tk.FALSE)

root.geometry("300x500")


pygame.mixer.init()


def creation():

    top_page = tk.Label(root, bg=b_blue, fg="black",
                        text="Welcome to Chat Bucket!",
                        pady=0, padx=1, height=1).place(x=80, y=0)  # my top page

send = tk.Button(root, text="Send", bg=b_blue, command=lambda: onclick(1))
send.place(x=260, y=475)

root.bind('<Return>', lambda event: onclick(1))

rectangle = tk.Text(root, width=50, height=35, bg=b_blue)  # rectangle
rectangle.config(state=tk.DISABLED)
rectangle.place(x=0, y=10)  # grid

chat_box = tk.Entry(root, bg=b_blue, fg="black", width=28)  # chat box
chat_box.place(x=0, y=470)

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


def play():
    pygame.mixer.music.load("song_for_game.mp3")
    pygame.mixer.music.play(loops=0)


def main():
    play()
    creation()
    onclick(args=1)

    
    


main()


root.mainloop()


# what to do left: Make "you" on right and "Connector" on left
# Make it type out on each side,
# make

