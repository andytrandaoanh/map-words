import os, sys
import system_handler as sH
from mysql_handler import getWordList
import re


def getOutPath(inFile, outDir):
	filePath = os.path.basename(inFile)
	#fname, fext = os.path.splitext(temp_path)
	pathOut =  os.path.join(outDir, filePath) 
	return(pathOut)

def processText(inFile, outDir):
	outFilePath = getOutPath(inFile, outDir)
	
	
	matches = sH.readTextFile(inFile)
	listMatch = matches.split("\n")
	cleanList = []
	for item in listMatch:
		parts = item.split(",")
		if(parts[0].strip()):
			cleanList.append(item)

	
	listMatch = list( dict.fromkeys(cleanList))
	
	sH.writeListToFile(listMatch, outFilePath)
	#print(listMatch)

	sH.openDir(outDir)
	sys.exit()

	