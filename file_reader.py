import os
import csv
from constants import MONTH_NAME_MAPPING
from weather import WeatherData


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
        Reads weather data from a CSV file into a list of dictionaries.
        Each dictionary represents a row with header names as keys.

        Parameters:
            filepath (str): The path to the weather data file.

        Returns:
            list: A list of dictionaries where each dictionary represents a row.
        """
        weather_data = []
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)  # Read the file into a dictionary format
            for row in reader:
                data = WeatherData.from_csv_row(row)
                if data is not None:
                    weather_data.append(data)
        return weather_data

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
        month_name = MONTH_NAME_MAPPING.get(month, "")
        if not month_name:
            return None
        for file in os.listdir(self.directory):
            if file.endswith(f"{year}_{month_name}.txt"):
                return os.path.join(self.directory, file)
        return None
