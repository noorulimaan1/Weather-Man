class WeatherStats:
    """
    A class to calculate statistics from weather data.

    Methods:
        find_extremes(weather_data): Finds the highest temperature, lowest temperature, and most humid day.
        calculate_averages(weather_data): Calculates the average highest temperature, lowest temperature, and mean humidity.
    """
    @staticmethod
    def find_extremes(weather_data):
        """
        Finds the highest temperature, lowest temperature, and most humid day from the weather data.

        Parameters:
            weather_data (list): A list of WeatherData instances.

        Returns:
            tuple: A tuple containing the highest temperature, highest temperature day,
                   lowest temperature, lowest temperature day, most humid day, and most humid day date.
        """
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

        # Ensure all return values are present
        return (
            highest_temp if highest_temp is not None else 'No Data',
            highest_temp_day if highest_temp_day else 'No Data',
            lowest_temp if lowest_temp is not None else 'No Data',
            lowest_temp_day if lowest_temp_day else 'No Data',
            most_humid_day if most_humid_day is not None else 'No Data',
            most_humid_day_date if most_humid_day_date else 'No Data'
        )


    @staticmethod
    def calculate_averages(weather_data):
        """
        Calculates average values for highest temperature, lowest temperature, and mean humidity.

        Args:
            weather_data (list): A list of WeatherData instances.

        Returns:
            tuple: A tuple containing the average highest temperature, average lowest temperature,
                   and average mean humidity, rounded to the nearest integer.
        """
        total_max_temp = total_min_temp = total_mean_humidity = 0
        count = 0

        for data in weather_data:
            if data.max_temp is not None:
                total_max_temp += data.max_temp
            if data.min_temp is not None:
                total_min_temp += data.min_temp
            if data.mean_humidity is not None:
                total_mean_humidity += data.mean_humidity
            count += 1

        if count == 0:
            return (0, 0, 0)

        avg_max_temp = round(total_max_temp / count)
        avg_min_temp = round(total_min_temp / count)
        avg_mean_humidity = round(total_mean_humidity / count)

        return (avg_max_temp, avg_min_temp, avg_mean_humidity)
