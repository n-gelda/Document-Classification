''' takes in freq_dict, and returns '''
def getWords (freq_dict):

    combinedFreqDict = dict() # 1D dictionary {"words": freq, ....}
    combinedFreqDict = getCombineFreqDict (freq_dict)


    irrelevantWords = getIrrelevantWords (combinedFreqDict)

    categoryKeyWordsRanking = dict()
    categoryKeyWordsRanking = getCateogriesKeyWords (freq_dict, irrelevantWords)

    return categoryKeyWordsRanking, irrelevantWords

def getCombinedFreqDict (freq_dict):
    aggregateFreqDict = dict()

    for category in freq_dict:
        for word in freq_dict[category]:
            aggregateFreqDict[word] = aggregateFreqDict.get(word,0) + freq_dict[category][word]


    return aggregateFreqDict

