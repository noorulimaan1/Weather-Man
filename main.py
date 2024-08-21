import argparse
from datetime import datetime
from file_reader import FileReader
from stats import WeatherStats


class WeatherMan:
    """
    A class to manage and process weather data for specific years or months.

    Attributes:
        file_reader (FileReader): An instance of FileReader for reading weather files.
    """
    def __init__(self, directory):
        """
        Initializes WeatherMan with the directory containing weather data files.

        Parameters:
            directory (str): The directory containing the weather data files.
        """
        self.file_reader = FileReader(directory)

    def process_annual_weather_extremes(self, year):
        """
        Processes weather data for a specific year and prints the highest temperature,
        lowest temperature, and most humid day.

        Parameters:
            year (str): The year for which to display weather extremes.
        """
        files = self.file_reader.get_files_for_year(year)
        weather_data = []

        for file in files:
                weather_data.extend(self.file_reader.read_weather_file(file))

        (
            highest_temp,
            highest_temp_day,
            lowest_temp,
            lowest_temp_day,
            most_humid_day,
            most_humid_day_date,
        ) = WeatherStats.find_extremes(weather_data)

        print(f"Highest: {highest_temp}C on {highest_temp_day}")
        print(f"Lowest: {lowest_temp}C on {lowest_temp_day}")
        print(f"Humidity: {most_humid_day}% on {most_humid_day_date}")

    def process_monthly_weather_averages(self, year, month):
        """
        Processes weather data for a specific month and prints the average highest temperature,
        average lowest temperature, and average mean humidity.

        Parameters:
            year (str): The year of the weather data.
            month (str): The month of the weather data.
        """
        file = self.file_reader.get_file_for_month(year, month)
        if not file:
            print(f"No data available for {year}/{month}")
            return

        weather_data = self.file_reader.read_weather_file(file)

        avg_high_temp, avg_low_temp, avg_mean_humidity = (
            WeatherStats.calculate_averages(weather_data)
        )

        print(f"Average Highest Temperature: {avg_high_temp}C")
        print(f"Average Lowest Temperature: {avg_low_temp}C")
        print(f"Average Mean Humidity: {avg_mean_humidity}%")

    def draw_bars(self, year, month):
        """
        Draws horizontal bar charts for the highest and lowest temperatures for each day of the given month.

        The highest temperatures are displayed in red and the lowest temperatures in blue.

        Parameters:
            year (str): The year for which to display the bar charts.
            month (str): The month for which to display the bar charts.
        """
        file = self.file_reader.get_file_for_month(year, month)
        if not file:
            print(f"No data available for {year}/{month}")
            return
        
        weather_data = self.file_reader.read_weather_file(file)
        
        WeatherStats.find_daily_extremes(weather_data)

def validate_year_month(value):
    """
    Validates the format of the year/month input using datetime.
    Parameters:
        value (str): The year/month string in the format "YYYY/MM".
    Returns:
        str: The validated year/month string.
    Raises:
        argparse.ArgumentTypeError: If the input format or year/month is invalid.
    """
    try:
        datetime.strptime(value, "%Y/%m")
    except (ValueError, IndexError) as exc:
        raise argparse.ArgumentTypeError(
            "Year/Month must be in the format YYYY/MM with valid year (0001-9999) and month (01-12)."
        ) from exc
    return value

def validate_year(value):
    """
    Validates that the input value is a valid year.
    Parameters:
        value (str): The year in the format "YYYY".
    Returns:
        str: The input value if it is valid.
    Raises:
        argparse.ArgumentTypeError: If the value is not a four-digit number or if it represents an invalid year.
    """
    try:
        datetime.strptime(value, "%Y")
    except (ValueError, IndexError) as exc:
        raise argparse.ArgumentTypeError(
            "Year must be a four-digit number within the range 0001-9999."
        ) from exc
    return value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process weather data.")
    parser.add_argument(
        "directory", type=str, help="Directory containing weather files"
    )
    parser.add_argument(
        "-e",
        "--extremes",
        type=validate_year,
        help="Year for which to display extremes",
    )
    parser.add_argument(
        "-a",
        "--averages",
        type=validate_year_month,
        help="Year/Month for which to display averages",
    )
    parser.add_argument(
        "-c",
        "--charts",
        type=validate_year_month,
        help="Year/Month for which to display temperature bars",
    )

    args = parser.parse_args()

    weather_man = WeatherMan(args.directory)

    if args.extremes:
        weather_man.process_annual_weather_extremes(args.extremes)
    elif args.averages:
        year, month = args.averages.split("/")
        weather_man.process_monthly_weather_averages(year, month)
    elif args.charts:
        year, month = args.charts.split("/")
        weather_man.draw_bars(year, month)
    else:
        parser.print_help()



