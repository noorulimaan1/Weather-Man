from weather import WeatherData

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
        extremes = {
            "highest_temp": WeatherData(date="", max_temp=None, min_temp=None, mean_humidity=None),
            "lowest_temp": WeatherData(date="", max_temp=None, min_temp=None, mean_humidity=None),
            "most_humid": WeatherData(date="", max_temp=None, min_temp=None, mean_humidity=None)
        }

        for data in weather_data:
            if data.max_temp is not None:
                if extremes["highest_temp"].max_temp is None or data.max_temp > extremes["highest_temp"].max_temp:
                    extremes["highest_temp"] = data

            if data.min_temp is not None:
                if extremes["lowest_temp"].min_temp is None or data.min_temp < extremes["lowest_temp"].min_temp:
                    extremes["lowest_temp"] = data

            if data.mean_humidity is not None:
                if extremes["most_humid"].mean_humidity is None or data.mean_humidity > extremes["most_humid"].mean_humidity:
                    extremes["most_humid"] = data

        return (
            extremes["highest_temp"].max_temp if extremes["highest_temp"].max_temp is not None else 'No Data',
            extremes["highest_temp"].date,
            extremes["lowest_temp"].min_temp if extremes["lowest_temp"].min_temp is not None else 'No Data',
            extremes["lowest_temp"].date,
            extremes["most_humid"].mean_humidity if extremes["most_humid"].mean_humidity is not None else 'No Data',
            extremes["most_humid"].date
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