import os, sys

def openDir(targetdir):
	#open directory when done	
	rpath = os.path.realpath(targetdir)
	os.startfile(rpath)

def getNormalPath(bookID, outDir):
	fname = "Matches Book"
	TEXT_EXT = ".txt"
	incString = str(bookID)
	increment = incString.zfill(4)
	normal_path =  os.path.join(outDir, fname + increment + TEXT_EXT) 
	return(normal_path)
	
def readTextFile(filepath):
	try:
	    ofile = open(filepath, 'r', encoding = 'utf-8') 
	    data = ofile.read()
	    return data
	except FileNotFoundError:
	    print("file not found")    
	except Exception as e:
	    print(e)  


def writeTupleToFile(dataTuple, outPath):	
    with open(outPath, 'w', encoding ='utf-8') as file:
        for item in dataTuple:
        	lineData = str(item[0]) + ',' + str(item[1])
        	file.write(lineData + "\n")



       

def writeListToFile(vlist, vpath):
    with open(vpath, 'w', encoding ='utf-8') as file:
        for item in vlist:    
            file.write(item + "\n")

