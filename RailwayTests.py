from DatabaseManager import *


# Sets up test database to ensure all functions in DatabaseManager are working properly
def setup_test_db():
    db_path = "test_railways.db"  # Defines the path for the test database

    conn = sqlite3.connect(db_path)  # Creates a connection to the database
    cursor = conn.cursor()  # Creates cursor for SQL commands

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

    # List of tuples each one containing an entry to be added to the test database with the data to be tested
    test_data = [
        (1, 'RouteA', 'Station1', 150, 180),
        (2, 'RouteB', 'Station2', 170, 100),
        (3, 'RouteC', 'Station3', 200, 310)
    ]

    cursor.executemany('INSERT INTO Railways VALUES (?,?,?,?,?)', test_data)  # Inserts the test data into the database
    conn.commit()  # Commits the changes and saves it
    conn.close()  # Closes the connection


# Test to ensure the total_passengers_per_station method is working properly
def test_total_passengers_per_station():
    db_manager = DatabaseManager('test_railways.db')
    passengers_per_station = db_manager.total_passengers_per_station()
    expected_results = {'Station3': 200, 'Station2': 170, 'Station1': 150}
    assert passengers_per_station == expected_results


# Test to ensure the total_passengers method is working properly
def test_total_passengers():
    db_manager = DatabaseManager('test_railways.db')
    total = db_manager.total_passengers()
    expected_total = 200 + 170 + 150
    assert total == expected_total


# Test to ensure the station_highest_passengers method is working properly
def test_station_highest_passengers():
    db_manager = DatabaseManager('test_railways.db')
    highest_station, max_passengers = db_manager.station_highest_passengers()
    expected_station = 'Station3'
    expected_passengers = 200
    assert highest_station == expected_station
    assert max_passengers == expected_passengers


# Test to ensure the total_distance_per_station method is working properly
def test_total_distance_per_station():
    db_manager = DatabaseManager('test_railways.db')
    distance_per_station = db_manager.total_distance_per_station()
    expected_distances = {'Station1': 180, 'Station2': 100, 'Station3': 310}
    assert distance_per_station == expected_distances


# Test to ensure the longest_station method is working properly
def test_longest_station():
    db_manager = DatabaseManager('test_railways.db')
    longest, max_distance = db_manager.longest_station()
    expected_longest = 'Station3'
    expected_distance = 310
    assert longest == expected_longest
    assert max_distance == expected_distance


# Test to ensure the order_stations_by_distance method is working properly
def test_order_stations_by_distance():
    db_manager = DatabaseManager('test_railways.db')
    sorted_stations = db_manager.order_stations_by_distance()
    expected_sorted_stations = [('Station2', 100), ('Station1', 180), ('Station3', 310)]
    assert sorted_stations == expected_sorted_stations
