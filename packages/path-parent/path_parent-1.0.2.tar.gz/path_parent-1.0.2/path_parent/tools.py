
import sys


def append(dest):
    if not dest in sys.path:
        sys.path.append(dest)


def remove(dest):
    if dest in sys.path:
        sys.path.remove(dest)


def clear(dest=""):
    if(len(dest) > 0):
        remove(dest)
    else:
        remove("..")
        remove("../..")
        remove("../../..")
