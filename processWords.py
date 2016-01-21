''' Handles the computation of key words per category and the non-relevant words '''
import re

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



''' NOT NEEDED CURRENTLY '''
''' Combine the freq dict from each category into 1 aggregated dict and remove trash words '''
def getCombinedFreqDict (freq_dict):
    aggregateFreqDict = dict()

    for category in freq_dict:
        for word in freq_dict[category]:
            aggregateFreqDict[word] = aggregateFreqDict.get(word,0) + freq_dict[category][word]

            aggregateFreqDict = removeTrashKeys(aggregateFreqDict)

    return aggregateFreqDict