import json
import os

def parseJSONFile(path):
    if not os.path.exists(path):
        raise FileNotFoundError("The directory does not exist, or system permissions for this directory are not granted.\nRun ls -l (path provided) to view permissions.\nTo modify use command chmod.")

    if os.path.getsize(path) == 0:
        raise ValueError(f"The json file provided is empty. Please verify file at {path} is not empty and retry.")

    with open(path, "r") as jsonFile:
        json_object = json.load(jsonFile)
        return json_object
