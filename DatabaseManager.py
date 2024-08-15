import sqlite3

'''
Purpose: Manage interactions between the railway database and the user giving information based on the railways such as
         using functions to get the total passengers, length, station capacity, etc. connecting with the sqlite database
         
Contract:
    total_passengers_per_station: Gets and returns the total number of passengers per station from the Railwaydetails.db
    total_passengers: Adds and returns the total number of passengers across all the stations from the Railwaydetails.db
    station_highest_passengers: Finds and returns the station with the highest number of passengers from Railwaydetails.db
    total_distance_per_station: Gets and returns the total distance each station covers from Railwaydetails.db 
    longest_station: Finds and returns the station covering the longest distance from Railwaydetails.db
    order_stations_by_distance: Sorts and returns the stations in ascending order based on their distances covered from Railwaydetails.db
'''


class DatabaseManager:
    # Initializes the DatabaseManager class with the path to the sqlite database
    def __init__(self, db_path):
        self.db_path = db_path  # Initializes and stores the database path.

    # Establish a connection to the database and creates a cursor
    def connect(self):
        self.conn = sqlite3.connect(self.db_path)  # Connects to the database
        self.cursor = self.conn.cursor()  # Creates cursor to execute commands with the database

    # Closes the database connection
    def close(self):
        if self.conn:
            self.conn.close()  # Closes the connection if it's open

    # Gets and returns the total number of passengers per station and prints the results as well
    def total_passengers_per_station(self):
        self.connect()  # Creates connection to the database
        # Executes an SQL command to add up number of passengers grouped by station from the Railwaydetails.db
        self.cursor.execute('SELECT station, SUM(number_of_passengers) FROM Railways GROUP BY station')
        results = self.cursor.fetchall()  # Gets the results from the SQL command
        self.close()  # Closes the connection to the database

        # Creates a dictionary from the results
        passengers_per_station = {station: passengers for station, passengers in results}

        # Iterates through the passengers_per_station dictionary
        for station, passengers in passengers_per_station.items():
            print(f"Station {station}: {passengers} passengers")  # Prints each station and it's total passengers
        return passengers_per_station  # Returns the dictionary with the results

    # Adds and returns the total number of passengers across all the stations and prints the results as well
    def total_passengers(self):
        passengers_per_station = self.total_passengers_per_station()  # Gets the total passengers per station
        total = sum(passengers_per_station.values())  # Sums up the total passengers from all the stations
        print(f"Total Passengers from all stations: {total}")  # Prints the total passengers from all the stations
        return total  # Returns the total passengers from all the stations

    # Finds and returns the station with the highest number of passengers and prints the results as well
    def station_highest_passengers(self):
        passengers_per_station = self.total_passengers_per_station()  # Gets the total passengers per station

        # Finds the station with the highest number of passengers
        highest_station = max(passengers_per_station, key=passengers_per_station.get)
        max_passengers = passengers_per_station[
            highest_station]  # Gets the number of passengers from the highest station

        # Prints the highest station, and it's passenger count being the highest
        print(
            f"Station with the Highest Number of Passengers: Station {highest_station} with {max_passengers} passengers")
        return highest_station, max_passengers  # Returns the station and it's passenger count

    # Gets and returns the total distance covered at each station and prints the results as well
    def total_distance_per_station(self):
        self.connect()  # Creates connection to the database
        # Executes an SQL command to add up the distances covered, grouped by station from the Railwaydetails.db
        self.cursor.execute('SELECT station, SUM(distance_miles) FROM Railways GROUP BY station')
        results = self.cursor.fetchall()  # Gets the results from the SQL command
        self.close()  # Closes the connection to the database

        # Creates a dictionary from the results
        distance_per_station = {station: distance for station, distance in results}

        # Iterates through the distance_per_station dictionary
        for station, distance in distance_per_station.items():
            print(f"Station {station}: {distance} miles")  # Prints each station and its total distance
        return distance_per_station  # Returns the dictionary with the results

    # Finds and returns the station with the longest distance and prints the results as well
    def longest_station(self):
        distance_per_station = self.total_distance_per_station()  # Gets the total distance per station
        longest = max(distance_per_station, key=distance_per_station.get)  # Finds the station with the longest distance
        max_distance = distance_per_station[longest]  # Gets the total distance from the station in 'longest'

        # Prints the station along with its distance
        print(f"Station with the Longest Distance: Station {longest} with {max_distance} miles")
        return longest, max_distance  # Returns the station along with its distance

    # Gets and sorts the stations in ascending order based on their distance
    def order_stations_by_distance(self):
        distance_per_station = self.total_distance_per_station()  # Gets the total distance per station

        # Function to help sorting
        def get_distance(item):
            return item[1]  # Returns the distance as a key for sorting

        # Sorts the station by distance in ascending order
        sorted_stations = sorted(distance_per_station.items(), key=get_distance)

        # Iterates through the sorted stations listed
        for station, distance in sorted_stations:
            print(
                f"Station {station} has a total distance of {distance} miles")  # Prints the station and total distance
        return sorted_stations  # Returns the sorted list of the stations by distance in ascending order
