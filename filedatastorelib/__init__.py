import platform
import os
from pathlib import Path
import json
import fcntl

if(platform.system() == 'Windows'):
    defPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    print(defPath)
else:
    defPath = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
    print(defPath)