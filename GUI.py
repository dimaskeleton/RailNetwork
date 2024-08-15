import tkinter as tk
from tkinter import messagebox
from DatabaseManager import *


class RailwayGUI:
    def __init__(self, master, db_manager):
        self.master = master  # Main Tkinter for the window
        self.db_manager = db_manager  # Instance off DatabaseManager for operations
        master.title("Railway Management System")  # Assigns a title to the main window

        # Buttons linked to each function in the Railway Management System using the DatabaseManager
        tk.Button(master, text="Total Passengers Per Station", command=self.display_total_passengers_per_station).pack()  # Button to display the total passengers  per station
        tk.Button(master, text="Total Passengers", command=self.display_total_passengers).pack()  # Button to display the total passengers added up
        tk.Button(master, text="Station with Highest Passengers", command=self.display_station_highest_passengers).pack()  # Button to display the station with the highest passengers
        tk.Button(master, text="Total Distance Per Station", command=self.display_total_distance_per_station).pack()  # Button to display the total distance per station
        tk.Button(master, text="Station with Longest Distance", command=self.display_longest_station).pack()  # Button to display the station with the highest distance
        tk.Button(master, text="Order Stations by Distance", command=self.display_ordered_stations_by_distance).pack()  # Button to display the stations sorted by distance

    # Displays a messagebox displaying the total passengers per station
    def display_total_passengers_per_station(self):
        passengers_per_station = self.db_manager.total_passengers_per_station()  # Gets the total passengers from the database
        message = "\n".join([f"{station}: {passengers} passengers" for station, passengers in
                             passengers_per_station.items()])  # Formats the passengers_per_station to be displayed
        messagebox.showinfo("Total Passengers Per Station",
                            message)  # Displays the formatted passengers_per_station in a messagebox

    # Displays a messagebox displaying the total number of passengers
    def display_total_passengers(self):
        total_passengers = self.db_manager.total_passengers()  # Gets the total number of passengers from the database
        messagebox.showinfo("Total Passengers",
                            f"Total Passengers: {total_passengers}")  # Displays the total passengers in a messagebox

    # Displays a messagebox displaying the station with the highest number of passengers
    def display_station_highest_passengers(self):
        station, passengers = self.db_manager.station_highest_passengers()  # Gets the station with the highest number of passengers from the database
        messagebox.showinfo("Station with Highest Passenger Count Is: ",
                            f"Station: {station} with {passengers} passengers")  # Displays the station and its passenger count in a message box

    # Displays a messagebox displaying the total distance each station covers
    def display_total_distance_per_station(self):
        distance_per_station = self.db_manager.total_distance_per_station()  # Gets the total distance per station from the database
        message = "\n".join([f"{station}: {distance} miles" for station, distance in
                             distance_per_station.items()])  # Formats the distance_per_station to be displayed
        messagebox.showinfo("Total Distance Per Station",
                            message)  # Displays the formatted distance_per_station in a messagebox

    # Displays a messagebox displaying the station with the longest distance
    def display_longest_station(self):
        station, distance = self.db_manager.longest_station()  # Gets the station with the longest distance
        messagebox.showinfo("Station with Longest Distance",
                            f"Station: {station} with {distance} miles")  # Displays the station along with its distance in a message box

    # Displays a messagebox displaying the stations sorted in ascending order based on distance
    def display_ordered_stations_by_distance(self):
        sorted_stations = self.db_manager.order_stations_by_distance()  # Gets the stations ordered by distance from the database
        message = "\n".join([f"{station}: {distance} miles" for station, distance in
                             sorted_stations])  # Formatted the sorted_stations to be displayed
        messagebox.showinfo("Stations Ordered by Distance",
                            message)  # Displays the formatted sorted_stations in a messagebox


# Main function to run the code
if __name__ == "__main__":
    root = tk.Tk()  # Main window
    db_path = "YOUR_LOCATION"  # Database path
    db_manager = DatabaseManager(db_path)  # Instance of DatabaseManager
    app = RailwayGUI(root, db_manager)  # Initializes GUI app
    root.mainloop()  # Starts tkinter loop
