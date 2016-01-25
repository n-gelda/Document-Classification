import math

def commonWordNormCrossCorr (freq_dict_training, freq_dict_in):
    corr = dict()
    for category in freq_dict_training:
        commonWordList = commonWordResamplingList(freq_dict_training[category], freq_dict_in)
        corr[category] = commonWordsCorrelation(freq_dict_training[category], freq_dict_in, commonWordList)

    return corr

def commonWordResamplingList (freq_dict_training, freq_dict_in):
    commonWordList = []

    for word in freq_dict_in:
        if word in freq_dict_training:
            commonWordList.append(word)

    return commonWordList

def commonWordsCorrelation (freq_dict_training, freq_dict_in, commonWordList):

    # if len(freq_dict_training) != len(freq_dict_in):
    #     print('len (freq_dict_training) != len (freq_dict_input')
    #     return 1 #Error

    # calculate mean
    meanTrainingSignal = 0
    meanInputSignal = 0

    i = 0
    if len(commonWordList) != 0:
        for word in commonWordList:
            meanTrainingSignal += freq_dict_training[word]
            meanInputSignal += freq_dict_in[word]
        meanTrainingSignal /= len(commonWordList)
        meanInputSignal /= len(commonWordList)

        corr = 0

        for word in commonWordList:
            numer = (freq_dict_training[word]-meanTrainingSignal) * (freq_dict_in[word]-meanInputSignal)
            denom = math.sqrt(math.pow(freq_dict_training[word] - meanTrainingSignal,2) * math.pow(freq_dict_in[word] - meanInputSignal,2))

            if denom != 0: # current sol: ignore point where denom == 0, should be a better fix
                corr += numer/denom
                i += 1
    if i == 0:
        return 0
    else:
        return corr/i




















# def interpolateSignals (x,y):
#
#     if len(x) > len(y): # interpolate signal y
#
#
#     elif len(x) == len(y):
#         return x,y # no need to interpolate any signal
#
#     elif len(x) < len(y): # interpolate signal x
#
#
#     else:
#         print('Error with the function dataProciessing.interpolateSignal\n')
#
#     return x,y