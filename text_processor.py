import sys
import re
import system_handler as sysHand
import mysql_data as sqlData


def matchWordToSent(wordList, sentList, bookID):
	results = []
	for word in wordList:
		for item in sentList:
			sentText = item[0]
			sentID = item[1]
			pattern = re.compile(r'\b%s\b' % word, re.I)
			matchObj = pattern.search(sentText)
			if (matchObj):
				results.append((word, sentID))
				print(matchObj)
	return results



def processText(bookID, outDir):
	
	outPath = sysHand.getNormalPath(bookID, outDir)
	#print('outPath:', outPath)	
	
	wordList = sqlData.getWordList()
	wordList.sort()	
	sentList = sqlData.getSentences(bookID)
	matchList = matchWordToSent(wordList, sentList, bookID)
	sysHand.writeTupleToFile(matchList, outPath)
	sysHand.openDir(outDir)
	sys.exit()
