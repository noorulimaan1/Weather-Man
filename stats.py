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
            tuple: A tuple containing the highest tem perature, highest temperature day,
                   lowest temperature, lowest temperature day, most humid day, and most humid day date.
        """
        extremes = {
            "highest_temp": WeatherData(),
            "lowest_temp": WeatherData(),
            "most_humid": WeatherData(),
        }

        for data in weather_data:
            if data.max_temp is not None and (
                extremes["highest_temp"].max_temp is None
                or data.max_temp > extremes["highest_temp"].max_temp
            ):
                extremes["highest_temp"] = data

            if data.min_temp is not None and (
                extremes["lowest_temp"].min_temp is None
                or data.min_temp < extremes["lowest_temp"].min_temp
            ):
                extremes["lowest_temp"] = data

            if data.mean_humidity is not None and (
                extremes["most_humid"].mean_humidity is None
                or data.mean_humidity > extremes["most_humid"].mean_humidity
            ):
                extremes["most_humid"] = data

        highest_temp = extremes["highest_temp"].max_temp if extremes["highest_temp"].max_temp is not None else "No Data"
        highest_temp_date = extremes["highest_temp"].date

        lowest_temp = extremes["lowest_temp"].min_temp if extremes["lowest_temp"].min_temp is not None else "No Data"
        lowest_temp_date = extremes["lowest_temp"].date

        most_humid = extremes["most_humid"].mean_humidity if extremes["most_humid"].mean_humidity is not None else "No Data"
        most_humid_date = extremes["most_humid"].date

        return (
            highest_temp,
            highest_temp_date,
            lowest_temp,
            lowest_temp_date,
            most_humid,
            most_humid_date,
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
