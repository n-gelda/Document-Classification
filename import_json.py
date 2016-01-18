# Nirvan
#import data from json file 
#14/01/2016

import json
from collections import defaultdict
from pprint import pprint
import re
import os

###############import json file##################

#open file and store as dictionary 


# for i in os.listdir(os.getcwd()): 
# 	if i.endswith(".py"):
# 		continue
#         for j in os.listdir(os.chdir(i)):
#         	if j.endswith(".json"): 
# 		    	print (j)
# 		        continue
# 		    else:
# 		        continue
	

file_path = "Body/TAS_01309380_1of1_01737502.json"
with open(file_path) as data_file:    
    data = json.load(data_file)

#remove superflous keys in the dictionary  
word = data["pages"][0]['words']





########### create frequency table #############

length = len(word)
i = 0
freq = dict()
freq['a'] = dict()

while i < length:
	temp = word[i]['value']
	key = re.sub(r'[^a-zA-Z0-9 ]',r'',temp.lower())
	freq['a'][key] = freq['a'].get(key, 0) + 1
	i += 1

pprint(freq)
################################################




