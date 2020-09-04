import pickle
from userClass import *

def createNewSave(filename,name,role,hostIP,port):
    with open(filename, 'wb') as output:
        obj = saveData(name,role,hostIP,port)
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
    return obj

def loadSave(filename):
    try:
        with open(filename, 'rb') as input:
            save = pickle.load(input)
    except:
        save = createNewSave(filename,"Guest","None","00.0.0.000","0000")
    return save

def saveGame(obj, filename):
    try:
        with open(filename, 'wb') as output:  # Overwrites any existing file.
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
    except:
        pass