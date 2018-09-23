# Jiazhen Huang
# ITP 115, Spring 2018
# Lab L8
# jiazhenh@usc.edu

def main():
    fileIn = open("story.txt","r")
    dict = {}
    linecounter = 0
    for line in fileIn:
        line = line.strip().lower()
        linecounter += 1
        linelist = []
        linelist.append(line)
        linelist = line.split()
        for word in linelist: # go letter by letter in each line
            word = word.strip(",.':;")
            if word not in dict:
                dict[word] = [linecounter]
            else:
                dict[word].append(linecounter)
    fileIn.close()
    sortedWords = list(dict.keys())
    sortedWords.sort()
    print("Here is the concordance for the file 'story.txt'\n")
    for item in sortedWords:
        print(item + ":", dict[item])

main()