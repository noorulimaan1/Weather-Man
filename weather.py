class WeatherData:
    def __init__(self, date, max_temp, min_temp, mean_humidity):
        self.date = date
        self.max_temp = int(max_temp) if max_temp else None
        self.min_temp = int(min_temp) if min_temp else None
        self.mean_humidity = int(mean_humidity) if mean_humidity else None

    @staticmethod
    def from_csv_row(row):
        date = row[0]
        max_temp = row[1]
        min_temp = row[3]
        mean_humidity = row[7]
        return WeatherData(date, max_temp, min_temp, mean_humidity)
