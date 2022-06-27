import json
import jsonschema
from jsonschema import validate


## module created to loop through NESTED json/dictionary key value pairs 
def cleanJson(jsonData):
    removeKeys = []
    for k, v in jsonData.items():
        if v is None:
            removeKeys.append(k)
        if isinstance(v, dict):
            cleanJson(v)
        else:
            pass
            #print("{0} : {1}".format(k, v))

    ## remove if none
    for k in removeKeys:
        del jsonData[k]

    return jsonData
