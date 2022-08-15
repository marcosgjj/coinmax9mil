def importKey(file):
    fileKey = open(file)
    key = fileKey.readline()
    fileKey.close()
    
    return key
