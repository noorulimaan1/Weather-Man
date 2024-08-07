import os
import sys
import csv
from datetime import datetime


def parse_args():
    if len(sys.argv) != 4:
        print("Usage: weatherman.py /path/to/files-dir -e year")
        sys.exit(1)
    files_dir = sys.argv[1]
    command = sys.argv[2]
    year = sys.argv[3]
    return files_dir, command, year


def read_files(filepath, stats):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Skip header or any invalid rows
            if row[0] == 'PKT' or not row:
                continue

            try:
                date_str = row[0]
                max_temp = row[1]
                min_temp = row[3]
                mean_humidity = row[8]

                if not date_str or not max_temp or not min_temp:
                    continue

                date = datetime.strptime(date_str, '%Y-%m-%d')
                max_temp = int(max_temp) if max_temp else None
                min_temp = int(min_temp) if min_temp else None
                mean_humidity = int(mean_humidity) if mean_humidity else None

                day_str = date.strftime('%B %d')

                # Update highest temperature
                if max_temp is not None:
                    if stats['highest'] is None or max_temp > stats['highest'][0]:
                        stats['highest'] = (max_temp, day_str)

                # Update lowest temperature
                if min_temp is not None:
                    if stats['lowest'] is None or min_temp < stats['lowest'][0]:
                        stats['lowest'] = (min_temp, day_str)

                # Update most humid day
                if mean_humidity is not None:
                    if stats['most_humid'] is None or mean_humidity > stats['most_humid'][0]:
                        stats['most_humid'] = (mean_humidity, day_str)

            except Exception as e:
                print(f"Error processing row: {row} with exception {e}")


def display_year_stats(stats):
    if stats['highest'] is None:
        print("No data available for highest temperature.")
    else:
        print(f"Highest: {stats['highest'][0]}C on {stats['highest'][1]}")

    if stats['lowest'] is None:
        print("No data available for lowest temperature.")
    else:
        print(f"Lowest: {stats['lowest'][0]}C on {stats['lowest'][1]}")

    if stats['most_humid'] is None:
        print("No data available for most humid day.")
    else:
        print(f"Humidity: {stats['most_humid'][0]}% on {
              stats['most_humid'][1]}")


def main():
    files_dir, command, year = parse_args()

    if command != '-e':
        print("Invalid command. Use -e for yearly data.")
        sys.exit(1)

    stats = {'highest': None, 'lowest': None, 'most_humid': None}

    for filename in os.listdir(files_dir):
        if filename.endswith('.txt') and f"{year}_" in filename:
            filepath = os.path.join(files_dir, filename)
            read_files(filepath, stats)

    display_year_stats(stats)


if __name__ == '__main__':
    main()
