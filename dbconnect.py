"""=======================================================================
||                      OPEN OR CREATE THE DATABASE                     ||
======================================================================="""

import sqlite3

# connect to or create database
with sqlite3.connect("./database/art.db") as db: cursor=db.cursor()

# create the artists table
cursor.execute("""CREATE TABLE IF NOT EXISTS artists(
    ArtistID integer PRIMARY KEY,
    "Name" text NOT NULL,
    "Address" text,
    Town text,
    County text,
    Postcode text);""")

# create the art pieces table
cursor.execute("""CREATE TABLE IF NOT EXISTS pieces(
    PieceID integer PRIMARY KEY,
    ArtistID integer NOT NULL,
    Title text NOT NULL,
    Medium text NOT NULL,
    Price integer NOT NULL);""")

# create table data in pieces table
# cursor.execute("""INSERT INTO pieces
# (PieceID, ArtistID, Title, Medium, Price)
#     VALUES
#     (3, 2, "A stroll to Westminster", "Ink", 190),
#     (4, 1, "African giant", "Oil", 800),
#     (5, 3, "Water daemon", "Acrylic", 1700),
#     (6, 4, "A seagull", "Watercolour", 35),
#     (7, 1, "Three friends", "Oil", 1800),
#     (8, 2, "Summer breeze 1", "Acrylic", 1350),
#     (9, 4, "Mr Hamster", "Watercolour", 35),
#     (10, 1, "Pulpit Rock, Dorset", "Oil", 600),
#     (11, 5, "Trawler Dungeness beach", "Oil", 195),
#     (12, 2, "Dance in the snow", "Oil", 250),
#     (13, 4, "St Tropez port", "Ink", 45),
#     (14, 3, "Pirate assassin", "Acrylic", 420),
#     (15, 1, "Morning walk", "Oil", 800),
#     (16, 4, "A baby barn swallow", "Watercolour", 35),
#     (17, 4, "The old working mills", "Ink", 395)
#     """)

db.commit()

"""=======================================================================
||                  END OF OPEN OR CREATE THE DATABASE                  ||
======================================================================="""
