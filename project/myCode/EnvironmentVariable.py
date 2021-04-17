import os

def getEnvironmentVariable(variableName):
    if variableName in os.environ:
            return os.environ[variableName]
    else:
        raise Exception("Environment variable named (" + variableName + ") does not exists and it should.")