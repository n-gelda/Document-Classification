import os
from os.path import isdir
import json
import re
from pprint import pprint

''' Returns freq and posSize Dict containing all categories embedded as sub dictionaries '''
def getData():
    freqDict = dict() # Struct: dict -> dict
    posSizeDict = dict() # Struct: dict -> 1Dlist -> 1Dlist

    for curCategory in os.listdir(os.chdir('OCR Results')):
        if curCategory.endswith("#"):
            freqDict[curCategory], posSizeDict[curCategory] = getDictForCategory(curCategory)

    os.chdir('..')
    return freqDict, posSizeDict


''' Returns a dictionary for freq, and posSize for the category/dir name supplied in input arg '''
def getDictForCategory(category):
    freqDict = dict()
    posSizeList2D = [] # 2D list of ['word', x/right, y/bottom, h, w]
    jsonDict = dict()

    for j in os.listdir(os.chdir(category)):
        if j.endswith(".json"):
            with open(j) as data_file:
                jsonDict = json.load(data_file)
                freqDict = convert2FreqDict(jsonDict, freqDict)
                posSizeList2D.append(convert2posSizeList(jsonDict, posSizeList2D))
    os.chdir('..')
    return freqDict, posSizeList2D

''' Given a jsonDict, it adds the freq data into the freqDict table '''
def convert2FreqDict(jsonDict, freqDict):
    words = jsonDict["pages"][0]['words']
    length = len(words)

    for i in range(0, length):
        tempKey = words[i]['value']
        key = re.sub(r'[^a-zA-Z0-9]', r'', tempKey.lower())  # discard all special char
        freqDict[key] = freqDict.get(key, 0) + 1

    if '' in freqDict: # remove '' as words from dict (some single char may be converted to just '')
        del freqDict['']
    return freqDict

''' Given a jsonDict, it adds the size and position data into posSize '''
def convert2posSizeList(jsonDict, posSizeList2D):

    # loop that transform loaded json file into table with desired attribute
    for x in range(0, len(jsonDict["pages"][0]["words"])):
        tempKey = jsonDict["pages"][0]["words"][x]['value'].casefold()
        tempKey = re.sub('[^a-zA-Z]', '', tempKey) # convert words to lower case and remove special char
        posSizeList2D.append([
                             tempKey,
                             jsonDict["pages"][0]["words"][x]['bbox']['right'],
                             jsonDict["pages"][0]["words"][x]['bbox']['bottom'],
                             jsonDict["pages"][0]["words"][x]['bbox']['height'],
                             jsonDict["pages"][0]["words"][x]['bbox']['width']])

    return posSizeList2D

def getSingleFreqDict(filePath):
    singleFreqDict = dict()
    singleDict = dict()
    with open(filePath) as data_file:
            jsonDict = json.load(data_file)
            freqDict = convert2FreqDict(jsonDict, singleFreqDict)

    return singleFreqDict
