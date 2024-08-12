"""
This module contains the FileReader class for reading weather data from CSV files.

The FileReader class includes methods for reading weather data files and retrieving
files based on year and month.
"""

import os
import csv


class FileReader:
    """
    A class to handle reading weather data files from a specified directory.

    Attributes:
        directory (str): The directory containing the weather data files.
    """

    def __init__(self, directory):
        """
        Initializes the FileReader with the given directory.

        Parameters:
            directory (str): The directory containing the weather data files.
        """
        self.directory = directory

    def read_weather_file(self, filepath):
        """
        Reads weather data from a CSV file. The first row is treated as a header.

        Parameters:
            filepath (str): The path to the weather data file.

        Returns:
            tuple: A tuple containing the header row and a list of data rows.
        """
        weather_data = []
        header = []
        with open(filepath, "r") as file:
            reader = csv.reader(file)
            header = next(reader)  # Read the header row
            for row in reader:
                weather_data.append(row)
        return header, weather_data

    def get_files_for_year(self, year):
        """
        Gets all files in the directory that match the given year.

        Parameters:
            year (str): The year for which to retrieve files.

        Returns:
            list: A list of file paths for the specified year.
        """
        files = os.listdir(self.directory)
        return [
            os.path.join(self.directory, file) for file in files if f"_{year}" in file
        ]

    def get_file_for_month(self, year, month):
        """
        Gets the file for a specific year and month.

        Args:
            year (str): The year of the file to retrieve.
            month (str): The month of the file to retrieve (1-12).

        Returns:
            str: The path to the file for the specified year and month, or None if not found.
        """
        month_name = {
            "1": "Jan",
            "2": "Feb",
            "3": "Mar",
            "4": "Apr",
            "5": "May",
            "6": "Jun",
            "7": "Jul",
            "8": "Aug",
            "9": "Sep",
            "10": "Oct",
            "11": "Nov",
            "12": "Dec",
        }.get(month, "")
        if not month_name:
            return None
        for file in os.listdir(self.directory):
            if file.endswith(f"{year}_{month_name}.txt"):
                return os.path.join(self.directory, file)
        return None
