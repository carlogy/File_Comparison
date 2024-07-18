import csv
from FileIterator import FileIterator
from parse_json_file import parseJSONFile

def convert_to_csv(list):
    headers = list[0].keys()
    with open("./results/mismatching_entities.csv", "w") as csv_file:
        csvwriter = csv.writer(csv_file)

        csvwriter.writerow(headers)

        for entity in FileIterator(list):
            csvwriter.writerow(",".join({k : (entity[k]) for k in entity}))

    return "Completed writing results to csv"


list = parseJSONFile("validationFiles/test5.json")

print(convert_to_csv(list))
