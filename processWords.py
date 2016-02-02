''' Handles the computation of key words per category and the non-relevant words '''
import re
import numpy as np
import os
import json
import math
import time


''' COMPUTE TF-IDF '''

def computeTFIDF (freq_dict, wordMapDict, numOfFile):
    tfidf_dict = dict()

    for category in freq_dict:

        tfidf_singleCategory_dict = dict()
        for word in freq_dict[category]:

            tf = math.log(freq_dict[category][word], 3)

            idf = computeIDF(word, wordMapDict, numOfFile)

            tfidf_singleCategory_dict[word] = tf * idf

        tfidf_dict[category] = tfidf_singleCategory_dict

    return tfidf_dict

def computeIDF(word, wordMapDict, N):

    df = 0

    for category in wordMapDict:
        for file in wordMapDict[category]:
            if word in wordMapDict[category][file]:
                df += 1


    if df == 0:
        return 0
    else:
        idf = math.log(N/df, 10)

        if word == 'the':
            print(idf)
        return idf

''' //compute TF-IDF end// '''


##########################################################

''' takes in freq_dict, and returns a dict within a dict of top ranking words per category, and returns freq_dict without the trash words '''
def filterTrashWords (freq_dict):

    for category in freq_dict:
        freq_dict[category] = removeTrashWords(freq_dict[category])

    # categoryKeyWordsRanking = dict()
    # categoryKeyWordsRanking = getCateogriesKeyWords (freq_dict)

    return freq_dict #,categoryKeyWordsRanking

def removeTrashWords (dictionary):
    dictionary = removeDigitKeys(dictionary)
    dictionary = removeCommonWords(dictionary)

    return dictionary

''' remove dictionary elements that contains digit within its key/words '''
def removeDigitKeys (dictionary):
    keyToRemove = []
    _digits = re.compile('\d')
    for key in dictionary:
        if bool(_digits.search(key)):
            keyToRemove.append(key)

    for key in keyToRemove:
        del dictionary[key]

    return dictionary

''' remove words from dictionary that are from the top common english words '''
def removeCommonWords (dictionary):
    top100WordList = dict()
    top100WordList = top100('top100words.txt')

    for key in top100WordList:
        if top100WordList[key] in dictionary:
            del dictionary[top100WordList[key]]

    return dictionary

''' returns a dictionary of the top 100 occurring words '''
def top100 (filePath):
    top100 = dict()
    temp = []
    with open(filePath, 'r') as f:
        for line in f:
            temp = line.split()
            top100[temp[0]] = temp[1]
    return top100

''' apply a threshold that removes all word with word freq below the mean '''
def applyMeanThreshold (freq_dict):
    for category in freq_dict:
        curCatAvg = np.mean(list(freq_dict[category].values()))

        # for word in freq_dict[category]:
        #     if freq_dict[category][word] > curCatAvg:




''' NOT NEEDED CURRENTLY '''
''' Combine the freq dict from each category into 1 aggregated dict and remove trash words '''
def getCombinedFreqDict (freq_dict):
    aggregateFreqDict = dict()

    for category in freq_dict:
        for word in freq_dict[category]:
            aggregateFreqDict[word] = aggregateFreqDict.get(word,0) + freq_dict[category][word]

            aggregateFreqDict = removeTrashKeys(aggregateFreqDict)

    return aggregateFreqDict