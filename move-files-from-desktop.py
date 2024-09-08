import os
import datetime
from shutil import move


def desktopCleaner():
    desktopDirectory = r"C:\Users\luszc\Desktop"
    movedFilesDirectory = r"C:\desktopCleaner"
    currentDateDirectory = os.path.join(movedFilesDirectory, datetime.date.today().isoformat())

    if len(os.listdir(desktopDirectory)) != 0:
        if datetime.date.today().isoformat() in os.listdir(movedFilesDirectory):
            moveFilesFromDesktop(desktopDirectory, currentDateDirectory)
        else:
            os.mkdir(currentDateDirectory)
            moveFilesFromDesktop(desktopDirectory, currentDateDirectory)


def moveFilesFromDesktop(desktopDirecotry, currentDateDirectory):
    # print(os.listdir(desktopDirecotry))
    createLogFile(os.listdir(desktopDirecotry))
    for file in os.listdir(desktopDirecotry):
        desktopfileDirectory = os.path.join(desktopDirecotry, file)
        os.chmod(desktopfileDirectory, 0o777)
        os.chmod(currentDateDirectory, 0o777)
        move(desktopfileDirectory, currentDateDirectory)


def createLogFile(desktopDirectory):
    logFile = r"C:\desktopCleaner\filesLog.txt"
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file = open(logFile, 'a')
    file.write("{} moved {} files\n".format(date, len(desktopDirectory)))
    file.write("Files: ")
    file.write(" ".join("{}".format(x) for x in desktopDirectory))
    file.write("\n")
    file.write("-"*30)
    file.write("\n\n")



desktopCleaner()




