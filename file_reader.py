import os

class FileReader:
    @staticmethod
    def get_files(files_dir: str, year: str):
        for filename in os.listdir(files_dir):
            if filename.endswith('.txt') and f"{year}_" in filename:
                yield os.path.join(files_dir, filename)
