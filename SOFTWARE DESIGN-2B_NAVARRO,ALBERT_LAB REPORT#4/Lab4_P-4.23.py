from os import listdir
from os.path import isfile, join

def find(path, filename):
    for f in listdir(path):
        if isfile(join(path, f)):
            if filename in f:
                print(f)
        else:
            find(join(path, f), filename)

find("C:/Users/Arman.LAPTOP-DBRIVTDS/PycharmProjects/SingleLinkedList/ATM", "bb")