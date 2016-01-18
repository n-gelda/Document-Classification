import os
from os.path import isdir
import json
import re
from pprint import pprint



def getFreqData (): 
	freqDict = dict()
	for curCategory in os.listdir(): 
		if isdir(curCategory):
			print(curCategory)
			freqDict[curCategory] = {"Key": 7}#getDictForCategory(curCategory)
	
	return freqDict

#returns a dictionary of words -> frequency of ONE
#category 
def getDictForCategory (category):	

	freqDict = dict()
	jsonDict = dict()
	
	for j in os.listdir(os.chdir(category)):
		if j.endswith(".json"): 
			with open(j) as data_file:						   
				jsonDict = json.load(data_file)
				freqDict = convert2FreqDict(jsonDict, freqDict)
	return freqDict			    



def convert2FreqDict(jsonDict, freqDict):
	word = jsonDict["pages"][0]['words']
	length = len(word)

	for i in range(0,length):
		tempKey = word[i]['value']
		key = re.sub(r'[^a-zA-Z0-9 ]',r'',tempKey.lower()) # discard all special char
		freqDict[key] = freqDict.get(key, 0) + 1

	return freqDict







# temp = getDictForCategory("RTW")
# pprint("RTW:", len(temp))
# temp = getDictForCategory("Invoice")
# pprint("Invoice:", len(temp))
# temp = getDictForCategory("Body")
# pprint("Body:", len(temp))
# temp = getDictForCategory("Medical Cert")
# pprint("Medical Cert:", len(temp))
# temp = getDictForCategory("Other")
# pprint("Other:", len(temp))
# temp = getDictForCategory("Progress Report")
# pprint("Progress Report:", len(temp))
# temp = getFreqData()
# pprint("ALL:", len(temp))

temp_dict = dict()
temp_dict = getFreqData()

pprint(temp_dict["Invoice"])




# temp_dict = dict()
# temp_dict = getData()

# print(temp_dict['from'])





# for curCategory in os.listdir(): 
# 		if isdir(curCategory):

# dict1 = dict()
# for subfolders in folder: 
# 	dict1[subf] = computer dictionary 





