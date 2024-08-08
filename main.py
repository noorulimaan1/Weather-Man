import sys
import os


from file_reader import FileReader
from stats import WeatherStats
from weather import WeatherProcessor



def parse_args():
    if len(sys.argv) != 4:
        print("Usage: python main.py weatherfiles -e year")
        sys.exit(1)
    files_dir = sys.argv[1]
    command = sys.argv[2]
    year = sys.argv[3]
    return files_dir, command, year


def main():
    files_dir, command, year = parse_args()

    if command != '-e':
        print("Invalid command. Use -e for yearly data.")
        sys.exit(1)

    stats = WeatherStats()
    processor = WeatherProcessor(stats)

    for filepath in FileReader.get_files(files_dir, year):
        processor.read_file(filepath)

    stats.display()


if __name__ == '__main__':
    main()
