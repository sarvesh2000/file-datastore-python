import platform
import os
from pathlib import Path
import json
import fcntl
from filedatastorelib
if(platform.system() == 'Windows'):
    defPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    print(defPath)
else:
    defPath = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
    print(defPath)
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