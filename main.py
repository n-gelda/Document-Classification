''' ############################################### '''
'''     Text Document Classification Algorithm      '''
''' ############################################### '''
from pprint import pprint
import numpy as np
import pandas as pdr
import matplotlib.pyplot as plt
from scipy import signal
import os

import collections

import readData
import processWords
import dataProcessing

''' ###################################### '''
''' ##     COMPUTE SAMPLE BANK DATA     ## '''
''' ###################################### '''

freq_dict = dict()
posSize_dict = dict()

freq_dict, posSize_dict = readData.getData()

freq_dict = processWords.filterTrashWords(freq_dict)


''' ########################################################## '''
''' ## READ IN INPUT DATA and CORRELATE AGAINST SAMPLE BANK ## '''
''' ########################################################## '''
TP = 0
FP = 0
Total = 0
for curCategory in os.listdir(os.chdir('input_files')):
    if curCategory.endswith("#"):
        for j in os.listdir(os.chdir(curCategory)):
            if j.endswith(".json"):
                inputFreqDict = readData.getSingleFreqDict(j)

                os.chdir('..')
                os.chdir('..') #one of these will go in production code

                inputFreqDict = processWords.removeTrashWords(inputFreqDict)

                corr = dataProcessing.commonWordNormCrossCorr(freq_dict,inputFreqDict)

                maxCorr = 0
                bestCategory = 'Body#'
                for category in corr:
                    if corr[category] > maxCorr:
                        maxCorr = corr[category]
                        bestCategory = category

                if bestCategory == curCategory:
                    print("True Positive")
                    TP += 1
                else:
                    print("False Positive")
                    FP += 1
                Total += 1
                print(curCategory, ':', j)
                pprint(corr)





                os.chdir('input_files/'+curCategory)
                # print(curCategory,':',j,':',freqDict)
        os.chdir('..')

print("True Positive Rate = ",TP/Total)
print("False Positive Rate = ", FP/Total)




print('\n')
print('hello you both are stud!')