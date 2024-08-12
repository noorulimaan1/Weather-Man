class WeatherData:
    """
    A class to represent weather data for a specific date.

    Attributes:
        date (str): The date of the weather data.
        max_temp (int): The maximum temperature.
        min_temp (int): The minimum temperature.
        mean_humidity (int): The mean humidity.
    """
    def __init__(self, date, max_temp, min_temp, mean_humidity):
        self.date = date
        self.max_temp = int(max_temp) if max_temp else None
        self.min_temp = int(min_temp) if min_temp else None
        self.mean_humidity = int(mean_humidity) if mean_humidity else None

    @staticmethod
    def from_csv_row(row):
        """
        Creates a WeatherData instance from a CSV row.

        Parameters:
            row (list): A list of values from a CSV row.

        Returns:
            WeatherData: An instance of WeatherData, or None if the row is invalid.
        """
        if row[0] == 'Date' or not row:
            return None
        
        date = row[0]
        max_temp = row[1]
        min_temp = row[3]
        mean_humidity = row[7]

        try:
            return WeatherData(date, max_temp, min_temp, mean_humidity)
        except ValueError:
            # Log the error or handle it appropriately
            print(f"Error processing row: {row}")
            return None
