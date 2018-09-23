# Yuchen Shi
# ITP115, Spring 2018
# Lab L12
# yuchensh@usc.edu

def main():
    fileIn=open("story.txt", "r")
    concordance={}
    counter=0
    for line in fileIn:
        line=line.strip()
        counter = counter + 1
        delimiter=" "
        lineList=line.split(delimiter)
        for words in lineList:
            words=words.lower()
            words=words.strip(";")
            words=words.strip(",")
            words=words.strip(".")
            words=words.strip(":")
            if words not in concordance:
                concordance[words]=[counter]
            else:
                concordance[words].append(counter)
    fileIn.close()
    del concordance[""]
    sortedKeyList=list(concordance.keys())
    sortedKeyList.sort()
    print("Here is the concordance for the file 'story.txt'")
    for key in sortedKeyList:
        print(str(key) + ":", concordance[key])

main()
