class WeatherStats:
    @staticmethod
    def find_extremes(weather_data):
        highest_temp = None
        lowest_temp = None
        most_humid_day = None
        highest_temp_day = ""
        lowest_temp_day = ""
        most_humid_day_date = ""

        for data in weather_data:
            if data.max_temp is not None:
                if highest_temp is None or data.max_temp > highest_temp:
                    highest_temp = data.max_temp
                    highest_temp_day = data.date

            if data.min_temp is not None:
                if lowest_temp is None or data.min_temp < lowest_temp:
                    lowest_temp = data.min_temp
                    lowest_temp_day = data.date

            if data.mean_humidity is not None:
                if most_humid_day is None or data.mean_humidity > most_humid_day:
                    most_humid_day = data.mean_humidity
                    most_humid_day_date = data.date

        return highest_temp, highest_temp_day, lowest_temp, lowest_temp_day, most_humid_day, most_humid_day_date

    @staticmethod
    def calculate_averages(weather_data):
        total_max_temp = 0
        total_min_temp = 0
        total_mean_humidity = 0
        count = 0

        for data in weather_data:
            if data.max_temp is not None and data.min_temp is not None and data.mean_humidity is not None:
                total_max_temp += data.max_temp
                total_min_temp += data.min_temp
                total_mean_humidity += data.mean_humidity
                count += 1

        if count == 0:
            return None, None, None

        return (total_max_temp // count,
                total_min_temp // count,
                total_mean_humidity // count)

    @staticmethod
    def find_daily_extremes(weather_data):
        for data in weather_data:
            if data.max_temp is not None:
                print(f"{data.date} Highest: {'+'*data.max_temp} {data.max_temp}")
            if data.min_temp is not None:
                print(f"{data.date} Lowest: {'+'*data.min_temp} {data.min_temp}")

