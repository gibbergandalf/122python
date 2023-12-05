# translation, focus on powershell
# naming convention is beeing ignored...
import os
from inspect import getsourcefile
folderPath = os.getenv("LocalAppdata") + "\\GIBB_BackupScript"  # windows
configFilePath = folderPath + "\\conf.txt"
logFilePath = folderPath + "\\log.txt"

pathToScript = os.path.abspath(getsourcefile(lambda: 0))

print(f"Folder Path: {folderPath}")  # f vor Klammer und dann curlies erlaubt Variablennamen
print(configFilePath)

#######
# FUNCTIONS
#######


def set_destination_folder():
    destinationFolder = input("Please enter destination folder:")


def set_source_folder():
    sourceFolder = input("Please enter source folder:")

def set_iterations():
    iterations = input("How many days of backups would you like to keep [0-100]")


#########
# START PROGRAM

set_destination_folder()
set_source_folder()
set_iterations()