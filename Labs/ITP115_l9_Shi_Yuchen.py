# Yuchen Shi
# ITP115, Spring 2018
# Lab L9
# yuchensh@usc.edu

def readDictionaryFile(dictionaryFileName):
    fileIn=open(dictionaryFileName, "r")
    wordsDictionary=[]
    for line in fileIn:
        line=line.strip()
        wordsDictionary.append(line)
    fileIn.close()
    return wordsDictionary

def readTextFile(textFileName):
    fileIn=open(textFileName, "r")
    wordsText=[]
    for line in fileIn:
        line=line.lower().strip()
        tempList=line.split(" ")
        for w in tempList:
            w=w.strip(".")
            w=w.strip("?")
            w=w.strip(",")
            w=w.strip("\"")
            wordsText.append(w)
    fileIn.close()
    return wordsText

def findErrors(dictionaryList, textList):
    errorList=[]
    for text in textList:
        if text not in dictionaryList:
            errorList.append(text)
    return errorList

def writeErrors(errorList, outputFileName):
    fileOut=open(outputFileName, "w")
    for error in errorList:
        print(error, file=fileOut)
    fileOut.close()

def main():
    print("Welcome to the Spell Checker!")
    dictionaryFile=input("Please enter the dictionary file you wish to read in: ")
    textFile=input("Please enter the text file you wish to read in: ")
    outPutFile=input("Please enter the output file you wish to write to: ")
    dictionary=readDictionaryFile(dictionaryFile)
    text=readTextFile(textFile)
    errorList=findErrors(dictionary, text)
    writeErrors(errorList, outPutFile)
    print("Success! All misspelled words were written to", outPutFile)

main()
