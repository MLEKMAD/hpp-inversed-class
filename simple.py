import re
import pandas as pd
from collections import Counter
import time
def cleanData(file):
    token = []
    #Removing the punctuations  and other irrelevant string content not meant for mapping
    wform = re.compile("[a-z]+")
    for line in file:
        if len(line) > 0:
            token.append(wform.findall(line.lower()))
    token = [x for x in token if x != []]
    #list = [item for i in token for item in i]
    return token
def countWords(Path):
    file = open (Path,encoding="utf8")
    list1 = cleanData(file)
    listOfWords = []
    for line in list1 :
        listOfWords +=line 
    return Counter(listOfWords)
start_time = int(round(time.time() * 1000))
countWords(Path='./data.txt')
end_time = int(round(time.time() * 1000))
print("--- %s milliseconds ---" % (end_time - start_time))



