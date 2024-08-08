class WeatherStats:
    def __init__(self):
        self.highest = None
        self.lowest = None
        self.most_humid = None

    def update_highest(self, temp, day):
        if self.highest is None or temp > self.highest[0]:
            self.highest = (temp, day)

    def update_lowest(self, temp, day):
        if self.lowest is None or temp < self.lowest[0]:
            self.lowest = (temp, day)

    def update_most_humid(self, humidity, day):
        if self.most_humid is None or humidity > self.most_humid[0]:
            self.most_humid = (humidity, day)

    def display(self):
        if self.highest is None:
            print("No data available for highest temperature.")
        else:
            print(f"Highest: {self.highest[0]}C on {self.highest[1]}")

        if self.lowest is None:
            print("No data available for lowest temperature.")
        else:
            print(f"Lowest: {self.lowest[0]}C on {self.lowest[1]}")

        if self.most_humid is None:
            print("No data available for most humid day.")
        else:
            print(f"Humidity: {self.most_humid[0]}% on {self.most_humid[1]}")
