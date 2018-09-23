# Yuchen Shi
# ITP115, Spring 2018
# Assignment 8
# yuchensh@usc.edu

from bs4 import BeautifulSoup
import urllib.request

def main():
    url="http://classes.usc.edu/term-20181/classes/itp/"
    page=urllib.request.urlopen(url)
    soup=BeautifulSoup(page.read(), "html.parser")

    units=int(input("Enter the number of units you wish to search for classes by (1-4): "))
    while units not in [1, 2, 3, 4]:
        units=int(input("*Invalid input, please try again.\nEnter the number of units you wish to search for classes by (1-4): "))
    fileOut=open("results.txt", "w")
    if units == 1:
        print("Here are all of the ITP classes that are 1.0 unit: ", file=fileOut)
    else:
        print("Here are all of the ITP classes that are " + str(units) + ".0 units: ", file=fileOut)
    allTagList=soup.find_all("div", class_="course-info expandable")
    for tag in allTagList:
        unitTag=tag.find("span")
        if len(unitTag.text)<12:   # This section deals with the extra credit part
            unitRange=range(int(unitTag.text[1]), int(unitTag.text[1])+1)
        else:
            unitRange=range(int(unitTag.text[1]), int(unitTag.text[5])+1)
        aTag=tag.find("a")
        timeTagList=tag.find_all("td", class_="time")
        registeredTagList = tag.find_all("td", class_="registered")
        instructorTagList=tag.find_all("td", class_="instructor")
        if units in unitRange:
            print("\n" + aTag.text, file=fileOut)
            for i in range(0, len(timeTagList)):
                print(timeTagList[i].text + ", " + registeredTagList[i].text + ", " + instructorTagList[i].text, file=fileOut)
    print("See 'results.txt' for your results.")


main()
