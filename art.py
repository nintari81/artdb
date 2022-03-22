from tkinter import *
from turtle import width

from pip import main
from dbconnect import *
from add_modules import *
from search_modules import *


# SHOW ALL ARTISTS IN DB
def show_artists():

    show = Tk()
    show.geometry("800x500")
    show.title("artists")

    show_artists = Listbox(show)
    show_artists.place(x=10, y=10, width=780, height=480)

    cursor.execute("SELECT * FROM artists")
    for i in cursor.fetchall():
        artist = f"{i[0]}, {i[1]}, {i[2]}, {i[3]}, {i[4]}, {i[5]}"
        show_artists.insert(END, artist)

    show.mainloop()


# SHOW ALL ARTWORK
def show_pieces():

    show_art = Tk()
    show_art.geometry("800x500")
    show_art.title("art work")

    show_art = Listbox(show_art)
    show_art.place(x=10, y=10, width=780, height=480)

    cursor.execute("SELECT * FROM pieces")
    for i in cursor.fetchall():
        piece = f"{i[0]}, {i[1]}, {i[2]}, {i[3]}, {i[4]}"
        show_art.insert(END, piece)

    show_art.mainloop()


# CLOSE ALL WINDOWS
def close_win():
    db.close()
    win.destroy()


"""======================================================================
||                             MAIN WINDOW                              ||
======================================================================="""

win = Tk()
win.geometry("310x450")
win.title("art db")
win.resizable(False, False)

# IMAGE
img = PhotoImage(file="./images/img.png")
art_img = Label(image=img)
art_img.place(x=30, y=30)

# BUTTONS
add_artist_btn = Button(win, text="add artist", command=add_artist)
add_artist_btn.place(x=30, y=260, width=120, height=40)

add_art_btn = Button(win, text="add artwork", command=add_art)
add_art_btn.place(x=160, y=260, width=120, height=40)

search_artist_btn = Button(win, text="search artist", command=search_artist)
search_artist_btn.place(x=30, y=300, width=120, height=40)

search_medium_btn = Button(win, text="search medium", command=search_medium)
search_medium_btn.place(x=160, y=300, width=120, height=40)

search_price_btn = Button(win, text="search price", command=search_price)
search_price_btn.place(x=30, y=340, width=120, height=40)

show_artists_btn = Button(win, text="view artists", command=show_artists)
show_artists_btn.place(x=160, y=340, width=120, height=40)

show_art_btn = Button(win, text="view art info", command=show_pieces)
show_art_btn.place(x=30, y=380, width=120, height=40)

close_btn = Button(win, text="close", command=close_win)
close_btn.place(x=160, y=380, width=120, height=40)

# KEEP THE MAIN WINDOW LOOPING UNTIL CLOSED
win.mainloop()
db.close()
