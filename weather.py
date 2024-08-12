# weather.py
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
        Creates a WeatherData instance from a dictionary representing a CSV row.

        Parameters:
            row (dict): A dictionary where the keys are header names.

        Returns:
            WeatherData: An instance of WeatherData, or None if the row is invalid.
        """
        if row.get('Date') == 'Date' or not row:
            return None
        
        date = row.get('PKT')
        max_temp = row.get('Max TemperatureC')
        min_temp = row.get('Min TemperatureC')
        mean_humidity = row.get(' Mean Humidity')

        try:
            return WeatherData(date, max_temp, min_temp, mean_humidity)
        except ValueError:
            # Log the error or handle it appropriately
            print(f"Error processing row: {row}")
            return None
