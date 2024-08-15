import sqlite3

# Creates connection to database, if it doesn't exist create it
conn = sqlite3.connect('Railwaydetails.db')

# Creates cursor for SQL commands
cursor = conn.cursor()

# Creates a new table if it doesn't exist with the following columns:
# trainID primary key for each train
# route holds which route is assigned to the train
# station holds which station on the route
# number_of_passengers holds the amount of passengers per stations
# distance_miles holds the distance for each station from the starting point
cursor.execute('''
CREATE TABLE IF NOT EXISTS Railways (
    trainID INTEGER PRIMARY KEY, 
    route TEXT,
    station TEXT,
    number_of_passengers INTEGER,
    distance_miles INTEGER
)
''')

# List of tuples each one containing an entry to be added to the Railway database with all the information
railroad_data = [
    (1, 'RouteA', 'Station1', 170, 100),
    (2, 'RouteB', 'Station2', 150, 180),
    (3, 'RouteC', 'Station3', 130, 310),
    (4, 'RouteD', 'Station4', 160, 217),
    (5, 'RouteC', 'Station5', 140, 263),
    (6, 'RouteA', 'Station6', 220, 129),
    (7, 'RouteA', 'Station7', 180, 109),
    (8, 'RouteB', 'Station8', 190, 89),
    (9, 'RouteD', 'Station9', 200, 280),
    (10, 'RouteC', 'Station10', 180, 174)
]

# Inserts each tuple into the Railway database defined under railroad_data
cursor.executemany('INSERT INTO Railways VALUES (?,?,?,?,?)', railroad_data)

conn.commit()  # Commits the changes to the database and saves it
conn.close()  # Closes the connection to the database
