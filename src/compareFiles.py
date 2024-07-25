from compareFile_helper import iterator_helper
from parse_csv_file import parse_csv
from parse_json_file import parseJSONFile
from to_csv import convert_to_csv

def compareFiles(objectA, objectB):

    mismatched_entities = []

    objectTypeA = type(objectA)
    objectTypeB = type(objectB)

    match objectTypeA, objectTypeB:
        # case objectTypeA , objectTypeB if objectTypeA == dict and objectTypeB == dict:
        case a , b if a == dict and b == dict:

            if "data" in objectA and "data" in objectB:

                list_of_entitiesA = objectA["data"]
                list_of_entitiesB = objectB["data"]

                mismatching_items = iterator_helper(list_of_entitiesA, list_of_entitiesB)

                if mismatching_items != None:
                    mismatched_entities.extend(mismatching_items)

        # case objectTypeA, objectTypeB if objectTypeA == list and objectTypeB == list:
        case a, b if a == list and b == list:

            if "data" not in objectA and "data" not in objectB:

                mismatching_items = iterator_helper(objectA, objectB)

                if mismatching_items != None:
                    mismatched_entities.extend(mismatching_items)


        # case objectTypeA, objectTypeB if objectTypeA == list and  objectTypeB == dict:
        case a, b  if a == list and b == dict:

            if "data" in objectB:
                list_of_entitiesB  = objectB["data"]

                mismatching_items = iterator_helper(objectA, list_of_entitiesB)

                if mismatching_items != None:
                    mismatched_entities.extend(mismatching_items)


        # case objectTypeA, objectTypeB if objectTypeA == dict and objectTypeB == list:
        case a, b if a == dict and b == list:

            if "data" in objectA:
                list_of_entitiesA = objectA["data"]

                mismatching_items = iterator_helper(list_of_entitiesA, objectB)

                if mismatching_items !=  None:
                    mismatched_entities.extend(mismatching_items)

        case _:
            return "Unable to compare files."

    if mismatched_entities:
        convert_to_csv(mismatched_entities);
        return "Mismatching entities found between files. Check ./results directory for csv file of mismatching entities."
        # return f"Mismatching entities found between files.\nTotal mismatches: {len(mismatched_entities)}"

    return "No diffs found between files"


fileA = parseJSONFile("/Users/cyannuzz/Downloads/57419d8b-9ca3-4029-855b-d7fd64d1aa54/asset_pretty.json")
fileB = parse_csv("/Users/cyannuzz/Downloads/Asset Classification.csv")

print(compareFiles(objectA=fileA, objectB=fileB))
