import csv
from FileIterator import FileIterator
from parse_json_file import parseJSONFile

def convert_to_csv(list):
    headers = list[0].keys()
    with open("./results/mismatching_entities.csv", "w") as csv_file:
        csvwriter = csv.DictWriter(csv_file, fieldnames= headers)
        csvwriter.writeheader()
        csvwriter.writerows([entity for entity in FileIterator(list)])

    return "Completed writing results to csv"

# list = parseJSONFile("validationFiles/test5.json")

# print(convert_to_csv(list))
