import os
from os.path import isdir
import json
import re
from pprint import pprint

def getData ():	

	freqDict = dict()
	jsonDict = dict()
	for curCategory in os.listdir(): 
		if isdir(curCategory):
			freqDict[curCategory] = dict()		
			for j in os.listdir(os.chdir(curCategory)):
				if j.endswith(".json"): 
					
					with open(j) as data_file:						   
						jsonDict = json.load(data_file)
						freqDict[curCategory] = convert2FreqDict(jsonDict, freqDict, curCategory)
						
			os.chdir("..")
	return freqDict			    



def convert2FreqDict(jsonDict, freqDict, curCategory):
	word = jsonDict["pages"][0]['words']
	length = len(word)

	for i in range(0,length):
		tempKey = word[i]['value']
		key = re.sub(r'[^a-zA-Z0-9 ]',r'',tempKey.lower()) # discard all special char
		freqDict[curCategory][key] = freqDict[curCategory].get(key, 0) + 1

	return freqDict

temp_dict = dict()
temp_dict = getData()

print(temp_dict['from'])







