import os


def CreateFolder(*args):
    if not os.path.exists(*args):
        os.makedirs(*args)