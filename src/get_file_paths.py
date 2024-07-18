import os
import shutil

def checkDir(env):
    file_path = "./validationFiles"
    full_path = os.path.join(file_path, env.lower())

    if not os.path.exists(full_path):
        raise FileNotFoundError("The directory does not exist, or system permissions for this directory are not granted.\nRun ls -l (path provided) to view permissions.\nTo modify use command chmod.")

    if os.path.exists(full_path):
        return full_path

def getFilePaths(parent_dir):
    files = list(os.walk(parent_dir))
    children = files[0][2]
    list_of_child_paths = [os.path.join(parent_dir, child) for child in children]
    return list_of_child_paths
