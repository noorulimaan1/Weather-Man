import csv
from datetime import datetime
from stats import WeatherStats

class WeatherProcessor:
    def __init__(self, stats: WeatherStats):
        self.stats = stats

    def read_file(self, filepath: str):
        """Reads the file and processes each row."""
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.process_row(row)

    def process_row(self, row):
        """Processes an individual row."""
        if not self.is_valid_row(row):
            return
        
        try:
            if len(row) < 9:
                print(f"Row has insufficient columns: {row}")
                return

            date_str = row[0]
            max_temp = row[1]
            min_temp = row[3]
            mean_humidity = row[8]

            date, max_temp, min_temp, mean_humidity = self.parse_row(date_str, max_temp, min_temp, mean_humidity)
            
            if date is None:
                print(f"Skipping row due to invalid date: {row}")
                return
            
            day_str = date.strftime('%B %d')

            # Update statistics
            self.update_statistics(max_temp, min_temp, mean_humidity, day_str)

        except Exception as e:
            self.handle_exception(row, e)


    def is_valid_row(self, row):
        """Checks if a row is valid."""
        return row and row[0] != 'PKT'

    def parse_row(self, date_str, max_temp, min_temp, mean_humidity):
        """Parses and converts row data into appropriate types."""
        if not date_str or not min_temp or not max_temp:
            return None, None, None, None

        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            print(f"Invalid date format: {date_str}")
            return None, None, None, None

        max_temp = int(max_temp) if max_temp else None
        min_temp = int(min_temp) if min_temp else None
        mean_humidity = int(mean_humidity) if mean_humidity else None

        return date, max_temp, min_temp, mean_humidity


    def update_statistics(self, max_temp, min_temp, mean_humidity, day_str):
        """Updates the weather statistics with the given data."""
        if max_temp is not None:
            self.stats.update_highest(max_temp, day_str)
        if min_temp is not None:
            self.stats.update_lowest(min_temp, day_str)
        if mean_humidity is not None:
            self.stats.update_most_humid(mean_humidity, day_str)

    def handle_exception(self, row, exception):
        """Handles exceptions during row processing."""
        print(f"Error processing row: {row} with exception {exception}")
