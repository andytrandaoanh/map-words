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
	#result = list( dict.fromkeys(result))
	listMatch = list( dict.fromkeys(listMatch))
	
	sH.writeListToFile(listMatch, outFilePath)
	#print(listMatch)

	sH.openDir(outDir)
	sys.exit()

	