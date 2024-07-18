import csv
import os

def parse_csv(path):
    if not os.path.exists(path):
        raise FileNotFoundError("The directory does not exist, or system permissions for this directory are not granted.\nRun ls -l (path provided) to view permissions.\nTo modify use command chmod.")

    if os.path.getsize(path) == 0:
        raise ValueError(f"The json file provided is empty. Please verify file at {path} is not empty and retry.")
    with open(path, newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        csv_object = [row for row in csv_reader]
        return csv_object
