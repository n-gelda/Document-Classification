import os
from os.path import isdir
import json
import re
from pprint import pprint

''' return a dict -> dict[cat] -> dict[cat][fileName] -> dict[cat][fileName][word'''
def getTrainingDataWordMap() :

    wordMapDict = dict()
    wordMapSingleCategoryDict = dict()

    numOfFiles = 0

    for category in os.listdir(os.chdir('OCR Results')):
        if category.endswith("#"):

            for fileName in os.listdir(os.chdir(category)):
                if fileName.endswith(".json"):
                    wordMapWordsDict = dict()
                    with open(fileName) as data_file:
                        numOfFiles += 1
                        jsonDict = json.load(data_file)

                        for x in range(0, len(jsonDict["pages"][0]["words"])):
                            word = jsonDict["pages"][0]["words"][x]['value'].casefold()
                            word = re.sub('[^a-zA-Z]', '', word) # convert words to lower case and remove special char
                            if word != '':
                                wordMapWordsDict[word] = 1

                    wordMapSingleCategoryDict[fileName] = wordMapWordsDict

            wordMapDict[category] = wordMapSingleCategoryDict
            os.chdir('..')



    os.chdir('..')

    return wordMapDict, numOfFiles

##################################################################################
''' Returns freq and posSize Dict containing all categories embedded as sub dictionaries '''
def getData():
    freqDict = dict() # Struct: dict -> dict
    posSizeDict = dict() # Struct: dict -> 1Dlist -> 1Dlist
    tfidf_dict = dict() # Struct: dict[category] -> dict[word]:tfidf_weighting

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
    numOfFiles = 0 # A counter, keeps track of the number of files
                   # in each category.

    for j in os.listdir(os.chdir(category)):
        if j.endswith(".json"):
            with open(j) as data_file:
                numOfFiles += 1
                jsonDict = json.load(data_file)
                # upperJsonDict = ditchLowerPageData(jsonDict)

                freqDict = convert2FreqDict(jsonDict, freqDict)
                posSizeList2D.append(convert2posSizeList(jsonDict, posSizeList2D))
    print(category," ",numOfFiles)
    freqDict = averagingFreqDict(freqDict,numOfFiles)
    os.chdir('..')
    return freqDict, posSizeList2D

''' Given a jsonDict, it adds the freq data into the freqDict table '''
def convert2FreqDict(jsonDict, freqDict):

    for x in range(0, len(jsonDict["pages"][0]["words"])):

        tempKey = jsonDict["pages"][0]["words"][x]['value']
        key = re.sub(r'[^a-zA-Z0-9]', r'', tempKey.lower())  # discard all special char
        freqDict[key] = freqDict.get(key, 0) + 1

    if '' in freqDict: # remove '' as words from dict (some single char may be converted to just '')
        del freqDict['']

    return freqDict

''' Given a jsonDict, it adds the size and position data into posSize '''
def convert2posSizeList(jsonDict, posSizeList2D):

    # loop that transform loaded json file into table with desired attribute
    for x in range(0, len(jsonDict["pages"][0]["words"])): # look at the json file to understand what x is

        tempKey = jsonDict["pages"][0]["words"][x]['value'].casefold()
        tempKey = re.sub('[^a-zA-Z]', '', tempKey) # convert words to lower case and remove special char
        posSizeList2D.append([
                             tempKey,
                             jsonDict["pages"][0]["words"][x]['bbox']['right'],
                             jsonDict["pages"][0]["words"][x]['bbox']['bottom'],
                             jsonDict["pages"][0]["words"][x]['bbox']['height'],
                             jsonDict["pages"][0]["words"][x]['bbox']['width']])

    return posSizeList2D

def averagingFreqDict(freqDict,numOfElements):

    for word in freqDict:
        freqDict[word] = freqDict[word] / numOfElements

    return freqDict


def getSingleFreqDict(filePath):
    singleFreqDict = dict()
    singleDict = dict()
    with open(filePath) as data_file:
            jsonDict = json.load(data_file)
            freqDict = convert2FreqDict(jsonDict, singleFreqDict)

    return singleFreqDict


''' NOT NEEDED CURRENTLY '''
def ditchLowerPageData(jsonDict):

    minTop = 100000 # arbitrarily picked (large num)
    maxBottom = 0 # arbitrarily picked (small number)

    # find midpoint of page
    for x in range(0,len(jsonDict["pages"][0]["words"])):
        if (jsonDict["pages"][0]["words"][x]['bbox']['top'] < minTop):
            minTop = jsonDict["pages"][0]["words"][x]['bbox']['top']
        if(jsonDict["pages"][0]["words"][x]['bbox']['bottom'] > maxBottom):
            maxBottom = jsonDict["pages"][0]["words"][x]['bbox']['bottom']
    midPage = (minTop + maxBottom)/2


    upperJsonDictTemp = dict()
    upperJsonDict1 = dict()
    upperJsonDict2 = dict()
    upperJsonDict = dict()

    i = 0
    for x in range(0,len(jsonDict["pages"][0]["words"])):
        if (jsonDict["pages"][0]["words"][x]['bbox']['bottom'] < midPage):
            upperJsonDictTemp[i] = jsonDict["pages"][0]["words"][x]
            i += 1

    upperJsonDict1["words"] = upperJsonDictTemp
    upperJsonDict2[0] = upperJsonDict1
    upperJsonDict["pages"] = upperJsonDict2

    #pprint(upperJsonDict)

    return upperJsonDict
