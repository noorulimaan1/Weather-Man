import sys
from file_reader import FileReader
from stats import WeatherStats
from weather import WeatherData


class WeatherMan:
    def __init__(self, directory):
        self.file_reader = FileReader(directory)

    def process_year(self, year):
        files = self.file_reader.get_files_for_year(year)
        weather_data = []

        for file in files:
            raw_data = self.file_reader.read_weather_file(file)
            for row in raw_data:
                weather_data.append(WeatherData.from_csv_row(row))

        highest_temp, highest_temp_day, lowest_temp, lowest_temp_day, most_humid_day, most_humid_day_date = WeatherStats.find_extremes(
            weather_data)

        print(f"Highest: {highest_temp}C on {highest_temp_day}")
        print(f"Lowest: {lowest_temp}C on {lowest_temp_day}")
        print(f"Humidity: {most_humid_day}% on {most_humid_day_date}")

    def process_month(self, year, month):
        file = self.file_reader.get_file_for_month(year, month)
        if not file:
            print(f"No data available for {year}/{month}")
            return

        raw_data = self.file_reader.read_weather_file(file)
        weather_data = [WeatherData.from_csv_row(row) for row in raw_data]

        avg_high_temp, avg_low_temp, avg_mean_humidity = WeatherStats.calculate_averages(
            weather_data)

        print(f"Average Highest Temperature: {avg_high_temp}C")
        print(f"Average Lowest Temperature: {avg_low_temp}C")
        print(f"Average Mean Humidity: {avg_mean_humidity}%")


if __name__ == "__main__":
    directory = sys.argv[1]
    option = sys.argv[2]
    weather_man = WeatherMan(directory)

    if option == "-e":
        year = sys.argv[3]
        weather_man.process_year(year)
    elif option == "-a":
        year, month = sys.argv[3].split('/')
        weather_man.process_month(year, month)
    else:
        print("Invalid option")
