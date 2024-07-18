from FileIterator import FileIterator


def iterator_helper(fileA, fileB):
    mismatched_entities = []
    try:
        for entity in FileIterator(fileA):
            if entity not in fileB:
                mismatched_entities.append(entity)
                continue

            entityB = fileB[fileB.index(entity)]
            mismatched_key_values = {k : (entity[k], entityB[k]) for k in entity if k in entityB and entity[k] != entityB[k]}

            if mismatched_key_values:
                mismatched_entities.append(entity)

    except:
        raise ValueError("Unable to iterate through files. Please ensure files are of .json or .csv format and try again.")
    if mismatched_entities:

        return mismatched_entities

    return None
