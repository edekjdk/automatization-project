import os
import datetime
from shutil import move


def desktopCleaner():
    desktopDirectory = r"C:\Users\luszc\Desktop"
    movedFilesDirectory = r"C:\desktopCleaner"
    currentDateDirectory = os.path.join(movedFilesDirectory, datetime.date.today().isoformat())
a
    if os.listdir(desktopDirectory):
        os.makedirs(currentDateDirectory, exist_ok=True)
        moveFilesFromDesktop(desktopDirectory, currentDateDirectory)


def moveFilesFromDesktop(desktopDirectory, currentDateDirectory):
    createLogFile(os.listdir(desktopDirectory))
    for file in os.listdir(desktopDirectory):
        desktopFileDirectory = os.path.join(desktopDirectory, file)
        destinationFileDirectory = os.path.join(currentDateDirectory, file)

        destinationFileDirectory = resolveFileNameConflict(destinationFileDirectory)

        os.chmod(desktopFileDirectory, 0o777)
        os.chmod(currentDateDirectory, 0o777)
        move(desktopFileDirectory, destinationFileDirectory)


def resolveFileNameConflict(destinationPath):
    base, extension = os.path.splitext(destinationPath)
    counter = 1

    while os.path.exists(destinationPath):
        destinationPath = f"{base}_{counter}{extension}"
        counter += 1

    return destinationPath


def createLogFile(desktopDirectory):
    logFile = r"C:\desktopCleaner\filesLog.txt"
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(logFile, 'a') as file:
        file.write("{} moved {} files\n".format(date, len(desktopDirectory)))
        file.write("Files: ")
        file.write(", ".join("{}".format(x) for x in desktopDirectory))
        file.write("\n")
        file.write("-" * 30)
        file.write("\n\n")


desktopCleaner()
