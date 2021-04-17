import os.path

def getVersion():
    if os.path.isfile('./version.txt'):
        with open('./version.txt') as f:
            return f.readline().strip()
    else:
        return "N/A"