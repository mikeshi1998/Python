# Yuchen Shi
# ITP115, Spring 2018
# Assignment A6
# yuchensh@usc.edu

def chooseYear():
    year=int(input("What year would you like to view data for? (2008 or 2009): "))
    while year != 2008 and year != 2009:
        year=int(input("*Invalid input, please try again!\nWhat year would you like to view data for? (2008 or 2009): "))
    if year == 2008:
        return 2008
    if year == 2009:
        return 2009


def getMaxMPG(year):
    maxMPG = 0
    if year==2008:
        fileIn = open("epaVehicleData2008.csv", "r")
        for line in fileIn:
            delimiter=","
            dataList=line.split(delimiter)
            if "VANS" in dataList[0] or "PICKUP" in dataList[0] or "CLASS" in dataList[0]:
                continue
            MPG=int(dataList[9])
            if MPG>maxMPG:
                maxMPG=MPG
        fileIn.close()
        return maxMPG
    elif year==2009:
        fileIn = open("epaVehicleData2009.csv", "r")
        for line in fileIn:
            delimiter=","
            dataList=line.split(delimiter)
            if "VANS" in dataList[0] or "PICKUP" in dataList[0] or "CLASS" in dataList[0]:
                continue
            MPG=int(dataList[9])
            if MPG>maxMPG:
                maxMPG=MPG
        fileIn.close()
        return maxMPG

def getMinMPG(year):
    minMPG = 10000
    if year==2008:
        fileIn = open("epaVehicleData2008.csv", "r")
        for line in fileIn:
            delimiter=","
            dataList=line.split(delimiter)
            if "VANS" in dataList[0] or "PICKUP" in dataList[0] or "CLASS" in dataList[0]:
                continue
            MPG=int(dataList[9])
            if MPG<minMPG:
                minMPG=MPG
        fileIn.close()
        return minMPG
    elif year==2009:
        fileIn = open("epaVehicleData2009.csv", "r")
        for line in fileIn:
            delimiter = ","
            dataList = line.split(delimiter)
            if "VANS" in dataList[0] or "PICKUP" in dataList[0] or "CLASS" in dataList[0]:
                continue
            MPG=int(dataList[9])
            if MPG < minMPG:
                minMPG = MPG
        fileIn.close()
        return minMPG

def getMaxMFR(year, maxMPG):
    maxMFR=[]
    if year==2008:
        fileIn = open("epaVehicleData2008.csv", "r")
        for line in fileIn:
            delimiter = ","
            dataList = line.split(delimiter)
            if "VANS" in dataList[0] or "PICKUP" in dataList[0] or "CLASS" in dataList[0]:
                continue
            MPG=int(dataList[9])
            if MPG==maxMPG:
                maxMFR.append(dataList[1])
                maxMFR.append(dataList[2])
        fileIn.close()
        return maxMFR
    elif year==2009:
        fileIn = open("epaVehicleData2009.csv", "r")
        for line in fileIn:
            delimiter = ","
            dataList = line.split(delimiter)
            if "VANS" in dataList[0] or "PICKUP" in dataList[0] or "CLASS" in dataList[0]:
                continue
            MPG=int(dataList[9])
            if MPG == maxMPG:
                maxMFR.append(dataList[1])
                maxMFR.append(dataList[2])
        fileIn.close()
        return maxMFR

def getMinMFR(year, minMPG):
    minMFR=[]
    if year==2008:
        fileIn = open("epaVehicleData2008.csv", "r")
        for line in fileIn:
            delimiter = ","
            dataList = line.split(delimiter)
            if "VANS" in dataList[0] or "PICKUP" in dataList[0] or "CLASS" in dataList[0]:
                continue
            MPG=int(dataList[9])
            if MPG==minMPG:
                minMFR.append(dataList[1])
                minMFR.append(dataList[2])
        fileIn.close()
        return minMFR
    elif year==2009:
        fileIn = open("epaVehicleData2009.csv", "r")
        for line in fileIn:
            delimiter = ","
            dataList = line.split(delimiter)
            if "VANS" in dataList[0] or "PICKUP" in dataList[0] or "CLASS" in dataList[0]:
                continue
            MPG=int(dataList[9])
            if MPG == minMPG:
                minMFR.append(dataList[1])
                minMFR.append(dataList[2])
        fileIn.close()
        return minMFR



def main():
    print("Welcome to EPA Mileage Calculator")
    year=chooseYear()
    maxMPG=getMaxMPG(year)
    minMPG=getMinMPG(year)
    maxMFR=getMaxMFR(year, maxMPG)
    minMFR=getMinMFR(year, minMPG)
    outputFile=input("Enter the filename to save results to: ")
    fileOut=open(outputFile, "w")
    print("EPA Highway MPG Calculator (" + str(year) + ")\n---------------------------------", file=fileOut)
    print("Maximum Mileage (highway): " + str(maxMPG), file=fileOut)
    for item in maxMFR:
        if maxMFR.index(item)%2==0:
            print("\t" + item, end=" ", file=fileOut)
        elif maxMFR.index(item)%2==1:
            print(item, file=fileOut)
    print("Minimum Mileage (highway): " + str(minMPG), file=fileOut)
    for item in minMFR:
        if minMFR.index(item)%2==0:
            print("\t"+item, end=" ", file=fileOut)
        elif minMFR.index(item)%2==1:
            print(item, file=fileOut)
    fileOut.close()
    print("Operation Success! Mileage data has been saved to", outputFile, "\nThanks, and have a great day!")

main()
