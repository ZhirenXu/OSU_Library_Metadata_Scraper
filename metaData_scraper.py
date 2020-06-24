import Greeting
import CategoryList
import LiTagList
import SimpleCSV
import Run
import concurrent.futures
import Login

def main(*argv):
    itemURL = []
    csvIn = ""
    csvOut = ""
    categoryList = []
    liTagList = []
    numOfUrl = 0

    Greeting.showInfo()
    argv = Login.login()
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
    if argv == ():
        Run.runProcessParallel(itemURL, liTagList, outFile, numOfUrl)
    else:
        Run.runProcessParallelLogin(argv, itemURL, liTagList, outFile, numOfUrl)
    outFile.close()
    Greeting.sysExit(csvOut)
    
if __name__ == "__main__":
    main()
