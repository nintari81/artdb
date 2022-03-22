from tkinter import *
from dbconnect import *


"""======================================================================
||                              ADD ARTIST                              ||
======================================================================="""
def add_artist():

    def clear_form():
        artist_name.delete(0, END), artist_address.delete(0, END)
        artist_town.delete(0, END), artist_county.delete(0, END)
        artist_postcode.delete(0, END)
        artist_name.focus()


    def add_click():
    
        name = artist_name.get()
        address = artist_address.get()
        town = artist_town.get()
        county = artist_county.get()
        postcode = artist_postcode.get()

        if name == "":
            output_msg["text"] = "name cannot be empty!"
            print("name cannot be empty")
        else:
            # create new employee table entry
            cursor.execute("""INSERT INTO artists("Name","Address","Town","County","Postcode")
            VALUES
            (?,?,?,?,?)""",(name, address, town, county, postcode))
            db.commit()
            clear_form()
            output_msg["text"] = "artist data created"

        artist_name.focus()

    # MAIN WINDOW SETTINGS
    add_win = Tk()
    add_win.geometry("290x300")
    add_win.title("add artist")
    add_win.resizable(False, False)

    # LABELS AND ENTRY BOXES
    lbl = Label(add_win, text="enter artist details")
    lbl.place(x=10, y=10)

    name_lbl = Label(add_win, text="name: ")
    name_lbl.place(x=10, y=55)
    artist_name = Entry(add_win)
    artist_name.place(x=80, y=50, width=200)
    artist_name.focus()

    address_lbl = Label(add_win, text="address:")
    address_lbl.place(x=10, y=85)
    artist_address = Entry(add_win)
    artist_address.place(x=80, y=80, width=200)

    town_lbl = Label(add_win, text="town:")
    town_lbl.place(x=10, y=115)
    artist_town = Entry(add_win)
    artist_town.place(x=80, y=110, width=200)

    county_lbl = Label(add_win, text="county:")
    county_lbl.place(x=10, y=145)
    artist_county = Entry(add_win)
    artist_county.place(x=80, y=140, width=200)

    postcode_lbl = Label(add_win, text="postcode:")
    postcode_lbl.place(x=10, y=175)
    artist_postcode = Entry(add_win)
    artist_postcode.place(x=80, y=170, width=200)

    output_msg = Label(add_win, text="::")
    output_msg.place(x=10, y=210)

    # BUTTONS
    add_btn = Button(add_win, text="add", command=add_click)
    add_btn.place(x=10, y=250, width=120, height=40)

    clear_btn = Button(add_win, text="clear", command=clear_form)
    clear_btn.place(x=160, y=250, width=120, height=40)

    # KEEP THE WINDOW LOOPING
    add_win.mainloop()


"""======================================================================
||                               ADD ART                                ||
======================================================================="""
def add_art():
    
    def clear_form():
        artist_id.delete(0, END),
        artist_name.delete(0, END),
        art_name.delete(0, END),
        art_medium.delete(0, END),
        art_price.delete(0, END)
        artist_id.focus()


    def add_click():
    
        id = artist_id.get()
        artist = artist_name.get()
        piece = art_name.get()
        medium = art_medium.get()
        price = art_price.get()

        if artist_id == "":
            output_msg["text"] = "id cannot be empty!"
            print("id cannot be empty")
        else:
            # create new employee table entry
            cursor.execute("""INSERT INTO pieces("ArtistID","Title","Medium","Price")
            VALUES
            (?,?,?,?)""",(id, piece, medium, price))
            db.commit()
            clear_form()
            output_msg["text"] = "art data created"

        artist_id.focus()

    # MAIN WINDOW SETTINGS
    add_art_win = Tk()
    add_art_win.geometry("310x300")
    add_art_win.title("add artwork")
    add_art_win.resizable(False, False)

    # LABELS AND ENTRY BOXES
    lbl = Label(add_art_win, text="enter piece details")
    lbl.place(x=10, y=10)

    artist_id_lbl = Label(add_art_win, text="artist id:")
    artist_id_lbl.place(x=10, y=55)
    artist_id = Entry(add_art_win)
    artist_id.place(x=100, y=50, width=200)

    artist_name_lbl = Label(add_art_win, text="name: ")
    artist_name_lbl.place(x=10, y=85)
    artist_name = Entry(add_art_win)
    artist_name.place(x=100, y=80, width=200)
    artist_name.focus()

    art_name_lbl = Label(add_art_win, text="piece name:")
    art_name_lbl.place(x=10, y=115)
    art_name = Entry(add_art_win)
    art_name.place(x=100, y=110, width=200)

    art_medium_lbl = Label(add_art_win, text="medium:")
    art_medium_lbl.place(x=10, y=145)
    art_medium = Entry(add_art_win)
    art_medium.place(x=100, y=140, width=200)

    art_price_lbl = Label(add_art_win, text="price:")
    art_price_lbl.place(x=10, y=175)
    art_price = Entry(add_art_win)
    art_price.place(x=100, y=170, width=200)

    output_msg = Label(add_art_win, text="::")
    output_msg.place(x=10, y=210)

    # BUTTONS
    add_btn = Button(add_art_win, text="add", command=add_click)
    add_btn.place(x=10, y=250, width=120, height=40)

    clear_btn = Button(add_art_win, text="clear", command=clear_form)
    clear_btn.place(x=180, y=250, width=120, height=40)

    artist_id.focus()

    # KEEP THE WINDOW LOOPING
    add_art_win.mainloop()