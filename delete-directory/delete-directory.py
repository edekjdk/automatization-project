import os

def deleteDirectory(path):
    for file in os.listdir(path):
        pathToFile = os.path.join(path, file)
        os.chmod(pathToFile, 0o777)
        os.remove(pathToFile)

deleteDirectory(r"C:\Users\luszc\Downloads")