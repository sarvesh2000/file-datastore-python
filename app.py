import platform
import os
from pathlib import Path

def startOperations(path):
    filename = "datastore.txt"
    newPath = os.path.join(path,filename)
    f = open(newPath, "a+")
    while True:
        try:
            print("Operations permitted are:\n1. Create a new Key Value Pair\n2. Read the Key Value Pairs\n3. Update a Key Value Pair\n4. Delete a Key Value Pair\nEnter your choice (1-4):")
            choice = int(input())
            if(choice <1 or choice >4):
                print("Sorry, I didn't understand that.")
                continue
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    if(choice == 1):
        print("Create Mode Selected")
        while True:
            key = input("Enter a key (max. length 32) ")
            if len(key) <= 32:
                break
            else:
                print("Key length is more - keep it shorter!")
        while True:
            JSONPath = Path(str(input("Enter the path of the JSON Object File")))
            if(os.path.exists(JSONPath)):
                if((Path(JSONPath).stat().st_size/1000)>16):
                    print("JSON File Size greater than 16KB. Please reduce your file size.")
                    continue
                else:
                    JSONFile = open(JSONPath)
                break
            else:
                print("File Doesn't Exist")
                continue

        

    elif(choice == 2):
        print("Read Mode Selected")
    elif(choice == 3):
        print("Update Mode Selected")
    else:
        print("Delete Mode Selected")
if(platform.system() == 'Windows'):
    defPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    print(defPath)
else:
    defPath = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
    print(defPath)

path = input("Enter a file path")
if (len(path) == 0):
    print("No Path Provided. Using Default Path " + defPath)
    startOperations(defPath)
else:
    print("Path Provided is ")
    print(path)
    startOperations(path)