import os
from os.path import isdir
import json
import re
from pprint import pprint


def getFreqData():
    freqDict = dict()

    for curCategory in os.listdir(os.chdir('OCR Results')):
        if isdir(curCategory):
            print(curCategory)
            freqDict[curCategory] = getDictForCategory(curCategory)

    return freqDict


# returns a dictionary of words -> frequency of ONE
# category
def getDictForCategory(category):
    freqDict = dict()
    jsonDict = dict()

    for j in os.listdir(os.chdir(category)):
        if j.endswith(".json"):
            with open(j) as data_file:
                jsonDict = json.load(data_file)
                freqDict = convert2FreqDict(jsonDict, freqDict)
    return freqDict


def convert2FreqDict(jsonDict, freqDict):
    words = jsonDict["pages"][0]['words']
    length = len(words)

    for i in range(0, length):
        tempKey = words[i]['value']
        key = re.sub(r'[^a-zA-Z0-9 ]', r'', tempKey.lower())  # discard all special char
        freqDict[key] = freqDict.get(key, 0) + 1

    return freqDict

temp_dict = dict()
temp_dict = getFreqData()

pprint(len(temp_dict))


#testing comment