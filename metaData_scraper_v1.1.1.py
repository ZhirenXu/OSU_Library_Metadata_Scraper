import Greeting
import CategoryList
import LiTagList
import SimpleCSV
import Run
import concurrent.futures

def main():
    itemURL = []
    csvIn = ""
    csvOut = ""
    categoryList = []
    liTagList = []
    numOfUrl = 0

    Greeting.showInfo()
    categoryList = CategoryList.getCategoryList()
    liTagList = LiTagList.getLiTagList()
    csvIn = SimpleCSV.getCSVInput()
    csvOut = SimpleCSV.getCSVOutput()
    
    itemURL = SimpleCSV.readCSV(csvIn)
    numOfUrl = len(itemURL)
    print("There are ", numOfUrl, " records in the input file.")
    # open file for output
    outFile = open(csvOut, 'w', encoding = 'utf8', newline='')
    SimpleCSV.writeCSV(categoryList, outFile)
    Run.runProcessParallel(itemURL, liTagList, outFile, numOfUrl)
    outFile.close()
    Greeting.sysExit(csvOut)
    
if __name__ == "__main__":
    main()
