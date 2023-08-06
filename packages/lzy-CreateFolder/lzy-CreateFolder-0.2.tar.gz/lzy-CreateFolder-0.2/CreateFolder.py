import os


def CreateFolder(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path