path = input("Enter a file path")
if (len(path) == 0):
    print("No Path Provided. Using Default Path")
else:
    print("Path Provided is ")
    print(path)
    f = open('datastore.txt')
    data = f.readline()
    print(data)

