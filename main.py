''' ############################################### '''
'''		Text Document Classification Algorithm		'''
''' ############################################### '''
from pprint import pprint
import numpy as np
import pandas as pdr
import matplotlib.pyplot as plt

import collections

import readData
import processWords

freq_dict = dict()
posSize_dict = dict()

freq_dict, posSize_dict = readData.getData()

freq_dict = processWords.filterTrashWords(freq_dict)




# sum = 0
# i=0
# for n in aggregateFreqDict:
#     if aggregateFreqDict[n] > 10:
#         print(type(n)," ",n,': ',aggregateFreqDict[n])
#         sum = sum + int(aggregateFreqDict[n])
#         i += 1
# mean = sum/i
# print('mean freq = ', mean)

# ''' Sort dictionary by key '''
# aggregateFreqDict = collections.OrderedDict(sorted(aggregateFreqDict.items()))
# plt.plot(list(aggregateFreqDict.values()))
# plt.bar(range(len(aggregateFreqDict)),list(aggregateFreqDict.values()), align='center')
# plt.xticks(range(len(aggregateFreqDict)), list(aggregateFreqDict.keys()))
# plt.show()



print('\n')
print('hello you both are stud!')