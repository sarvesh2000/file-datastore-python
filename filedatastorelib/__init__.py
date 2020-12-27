def keyCheck():
    while True:
            key = input("Enter a key (max. length 32) ")
            if len(key) <= 32:
                break
            else:
                print("Key length is more - keep it shorter!")
    return key
def startOperations(path):
    while True:
        try:
            print("Operations permitted are:\n1. Create a new Key Value Pair\n2. Read the Key Value Pairs\n3. Update a Key Value Pair\n4. Delete a Key Value Pair\nEnter your choice (1-4):")
            choice = int(input())
            if(choice < 1 or choice > 4):
                print("Sorry, I didn't understand that.")
                continue
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    if(choice == 1):
        print("Create Mode Selected")
        key = keyCheck()
        filename = "datastore.txt"
        newPath = os.path.join(path,filename)
        if(os.path.exists(newPath)):
            f = open(newPath, "r")
            fcntl.flock(f, fcntl.LOCK_EX)
            count = 1
            Lines = f.readlines()
            for line in Lines:
                dataKey = line.split('=')[0].strip()
                print("Data Key " + dataKey)
                count = count + 1
                if key == dataKey :
                    print("Key already exists in the datastore. Please enter a new key.")
                    keyCheck()
            fcntl.flock(f, fcntl.LOCK_UN)
            f.close()
        while True:
            JSONPath = Path(str(input("Enter the path of the JSON Object File")))
            if(os.path.exists(JSONPath)):
                if((Path(JSONPath).stat().st_size/1000)>16):
                    print("JSON File Size greater than 16KB. Please reduce your file size.")
                    continue
                else:
                    JSONFile = open(JSONPath)
                    data = json.load(JSONFile)
                    print(data)
                    f = open(newPath, "a+")
                    fcntl.flock(f, fcntl.LOCK_EX)
                    f.write(key + "= " + json.dumps(data) + "\n")
                    print("Key Value Pair Added Successfully")
                    fcntl.flock(f, fcntl.LOCK_UN)
                    f.close()
                    JSONFile.close()
                break
            else:
                print("File Doesn't Exist")
                continue

    elif(choice == 2):
        print("Read Mode Selected")
        key = keyCheck()
        filename = "datastore.txt"
        newPath = os.path.join(path,filename)
        if(os.path.exists(newPath)):
            f = open(newPath, "r")
            fcntl.flock(f, fcntl.LOCK_EX)
            Lines = f.readlines()
            flag = False
            for line in Lines:
                dataKey = line.split('=')[0].strip()
                dataValue = line.split('=')[1].strip()
                if key == dataKey :
                    print("Data Key " + dataKey)
                    print("Data Value " + dataValue)
                    flag = True
                    break
            if not flag :
                print("Key Not Found")
            fcntl.flock(f, fcntl.LOCK_UN)
            f.close()
    elif(choice == 3):
        print("Update Mode Selected")
        key = keyCheck()
        filename = "datastore.txt"
        newPath = os.path.join(path,filename)
        if(os.path.exists(newPath)):
            f = open(newPath, "r")
            fcntl.flock(f, fcntl.LOCK_EX)
            Lines = f.readlines()
            flag = False
            fcntl.flock(f, fcntl.LOCK_UN)
            f.close()
            f = open(newPath, "w")
            fcntl.flock(f, fcntl.LOCK_EX)
            for line in Lines:
                dataKey = line.split('=')[0].strip()
                dataValue = line.split('=')[1].strip()
                if key != dataKey :
                    flag = True
                    f.write(line)
                else:
                    flag = True
                    while True:
                        JSONPath = Path(str(input("Enter the path of the JSON Object File")))
                        if(os.path.exists(JSONPath)):
                            if((Path(JSONPath).stat().st_size/1000)>16):
                                print("JSON File Size greater than 16KB. Please reduce your file size.")
                                continue
                            else:
                                JSONFile = open(JSONPath)
                                data = json.load(JSONFile)
                                print(data)
                                f = open(newPath, "w")
                                f.write(key + "= " + json.dumps(data) + "\n")
                                print("Key Value Pair Updated Successfully")
                                fcntl.flock(f, fcntl.LOCK_UN)
                                f.close()
                            break
                        else:
                            print("File Doesn't Exist")
                            continue
            if not flag :
                print("Key Not Found")
                print("Update Operation Successful.")
    else:
        print("Delete Mode Selected")
        key = keyCheck()
        filename = "datastore.txt"
        newPath = os.path.join(path,filename)
        if(os.path.exists(newPath)):
            f = open(newPath, "r")
            fcntl.flock(f, fcntl.LOCK_EX)
            Lines = f.readlines()
            flag = False
            f.close()
            f = open(newPath, "w")
            for line in Lines:
                dataKey = line.split('=')[0].strip()
                dataValue = line.split('=')[1].strip()
                if key != dataKey :
                    flag = True
                    f.write(line)
            if not flag :
                print("Key Not Found")
            print("Delete Operation Successful.")
            fcntl.flock(f, fcntl.LOCK_UN)
            f.close()