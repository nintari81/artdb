from tkinter import *
from dbconnect import *


"""======================================================================
||                           SEARCH ARTIST                              ||
======================================================================="""
def search_artist():
    
    def close_show():
        show.destroy()


    def search():
        show_search.delete(0, END)
        artist = artist_name.get()
        cursor.execute("SELECT * FROM artists WHERE name=?",[artist])

        for i in cursor.fetchall():
            result = f"{i[1]}, {i[2]}, {i[3]}, {i[4]}, {i[5]}"
            show_search.insert(END, result)


    show = Tk()
    show.geometry("800x500")
    show.title("search results")

    name_lbl = Label(show, text="name: ")
    name_lbl.place(x=10, y=15)
    artist_name = Entry(show)
    artist_name.place(x=80, y=10, width=200)
    artist_name.focus()

    search_btn = Button(show, text="search", command=search)
    search_btn.place(x=300, y=10, width=120, height=30)

    close_btn = Button(show, text="close", command=close_show)
    close_btn.place(x=430, y=10, width=120, height=30)

    show_search = Listbox(show)
    show_search.place(x=10, y=50, width=780, height=400)

    show.mainloop()


"""======================================================================
||                            SEARCH PRICE                              ||
======================================================================="""
def search_price():
    
    def close_show():
        show.destroy()


    def search():
        show_search.delete(0, END)
        min = min_price.get()
        max = max_price.get()
        cursor.execute("""SELECT pieces.pieceid, artists.name, pieces.artistid, pieces.title, pieces.price 
        FROM pieces,artists WHERE artists.artistid=pieces.artistid AND pieces.price>=? AND pieces.price<=?""",[min, max])
        for i in cursor.fetchall():
            # result = f"{i[0]}, {i[1]}, {i[2]}, {i[3]}, {i[4]}"
            result = f"{i[1]}, {i[3]}, {i[4]}"
            show_search.insert(END, result)

        min_price.focus()
    

    show = Tk()
    show.geometry("560x450")
    show.title("search results")

    min_lbl = Label(show, text="min: ")
    min_lbl.place(x=10, y=15)
    min_price = Entry(show)
    min_price.place(x=50, y=10, width=50)
    min_price.focus()

    max_lbl = Label(show, text="max: ")
    max_lbl.place(x=110, y=15)
    max_price = Entry(show)
    max_price.place(x=150, y=10, width=50)

    search_btn = Button(show, text="search", command=search)
    search_btn.place(x=300, y=10, width=120, height=30)

    close_btn = Button(show, text="close", command=close_show)
    close_btn.place(x=430, y=10, width=120, height=30)

    show_search = Listbox(show)
    show_search.place(x=10, y=50, width=540, height=380)

    show.mainloop()


"""======================================================================
||                           SEARCH MEDIUM                              ||
======================================================================="""
def search_medium():
    
    def close_show():
        show.destroy()


    def search():
        show_search.delete(0, END)
        medium = medium_name.get()
        cursor.execute("""SELECT pieces.pieceid, artists.name, pieces.title, pieces.medium
        FROM pieces,artists WHERE artists.artistid=pieces.artistid AND pieces.medium=?""",[medium])

        for i in cursor.fetchall():
            result = f"{i[0]}, {i[1]}, {i[2]}, {i[3]}"
            show_search.insert(END, result)


    show = Tk()
    show.geometry("560x450")
    show.title("search results")

    name_lbl = Label(show, text="medium: ")
    name_lbl.place(x=10, y=15)
    medium_name = Entry(show)
    medium_name.place(x=80, y=10, width=200)
    medium_name.focus()

    search_btn = Button(show, text="search", command=search)
    search_btn.place(x=300, y=10, width=120, height=30)

    close_btn = Button(show, text="close", command=close_show)
    close_btn.place(x=430, y=10, width=120, height=30)

    show_search = Listbox(show)
    show_search.place(x=10, y=50, width=540, height=380)

    show.mainloop()
