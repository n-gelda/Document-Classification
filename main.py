''' main '''
''' ############################################### '''
'''		Text Document Classification Algorithm		'''
''' ############################################### '''
from pprint import pprint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import collections

import readData
import computeKeyWords

freq_dict = dict()
posSize_dict = dict()

freq_dict, posSize_dict = readData.getData()

aggregateFreqDict = computeKeyWords.getCombinedFreqDict(freq_dict)


''' Sort dictionary by key '''
aggregateFreqDict = collections.OrderedDict(sorted(aggregateFreqDict.items()))
plt.plot(list(aggregateFreqDict.values()))
plt.show()


print('hello you both are stud!')