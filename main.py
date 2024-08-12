import argparse
from file_reader import FileReader
from stats import WeatherStats
from weather import WeatherData

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

    def process_yearly_weather(self, year):
        """
        Processes weather data for a specific year and prints the highest temperature,
        lowest temperature, and most humid day.

        Parameters:
            year (str): The year for which to display weather extremes.
        """
        files = self.file_reader.get_files_for_year(year)
        weather_data = []

        for file in files:
            raw_data = self.file_reader.read_weather_file(file)
            for row in raw_data:
                weather_data.append(WeatherData.from_csv_row(row))

        # Filter out None values that might have been returned by from_csv_row
        weather_data = [data for data in weather_data if data is not None]

        highest_temp, highest_temp_day, lowest_temp, lowest_temp_day, most_humid_day, most_humid_day_date = WeatherStats.find_extremes(weather_data)

        print(f"Highest: {highest_temp}C on {highest_temp_day}")
        print(f"Lowest: {lowest_temp}C on {lowest_temp_day}")
        print(f"Humidity: {most_humid_day}% on {most_humid_day_date}")


    def process_monthly_weather(self, year, month):
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

        raw_data = self.file_reader.read_weather_file(file)
        weather_data = [WeatherData.from_csv_row(row) for row in raw_data]

        avg_high_temp, avg_low_temp, avg_mean_humidity = WeatherStats.calculate_averages(weather_data)

        print(f"Average Highest Temperature: {avg_high_temp}C")
        print(f"Average Lowest Temperature: {avg_low_temp}C")
        print(f"Average Mean Humidity: {avg_mean_humidity}%")



def validate_year_month(value):
    parts = value.split('/')
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("Year/Month must be in the format YYYY/MM.")
    
    year, month = parts
    if not (year.isdigit() and len(year) == 4):
        raise argparse.ArgumentTypeError("Year must be a four-digit number.")
    
    if not (month.isdigit() and 1 <= int(month) <= 12):
        raise argparse.ArgumentTypeError("Month must be a number between 1 and 12.")
    
    return value

def validate_year(value):
    if not (value.isdigit() and len(value) == 4):
        raise argparse.ArgumentTypeError("Year must be a four-digit number.")
    
    return value

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process weather data.")
    parser.add_argument('directory', type=str, help="Directory containing weather files")
    parser.add_argument('-e', '--extremes', type=validate_year, help="Year for which to display extremes")
    parser.add_argument('-a', '--averages', type=validate_year_month, help="Year/Month for which to display averages")

    args = parser.parse_args()

    weather_man = WeatherMan(args.directory)

    if args.extremes:
        weather_man.process_yearly_weather(args.extremes)
    elif args.averages:
        year, month = args.averages.split('/')
        weather_man.process_monthly_weather(year, month)
    else:
        parser.print_help()
