import os

class FileReader:
    def __init__(self, directory):
        self.directory = directory

    def read_weather_file(self, filepath):
        weather_data = []
        with open(filepath, 'r') as file:
            lines = file.readlines()[1:]  # Skip the header line
            for line in lines:
                weather_data.append(line.strip().split(','))
        return weather_data

    def get_files_for_year(self, year):
        files = os.listdir(self.directory)
        return [os.path.join(self.directory, file) for file in files if f'_{year}' in file]

    def get_file_for_month(self, year, month):
        month_name = {
            '1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr', '5': 'May', '6': 'Jun',
            '7': 'Jul', '8': 'Aug', '9': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
        }.get(month, '')
        for file in os.listdir(self.directory):
            if file.endswith(f'{year}_{month_name}.txt'):
                return os.path.join(self.directory, file)
        return None
