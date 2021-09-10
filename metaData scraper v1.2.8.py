from Code import Greeting
from Code import Category
from Code import SimpleCSV
from Code import Run
import concurrent.futures
from Code import Login

def main(*argv):
    itemURL = []
    csvIn = ""
    csvOut = ""
    categoryList = []
    liTagList = []
    numOfUrl = 0
    session = 0
    
    Greeting.showInfo()
    while session == 0:
        session = Login.login()
    categoryList = Category.getCategoryList()
    liTagList = Category.getLiTagList()
    csvIn = SimpleCSV.getCSVInput()
    csvOut = SimpleCSV.getCSVOutput()
    
    itemURL = SimpleCSV.readCSV(csvIn)
    numOfUrl = len(itemURL)
    print("There are ", numOfUrl, " records in the input file.")
    # open file for output
    outFile = open(csvOut, 'w', encoding = 'utf8', newline='')
    SimpleCSV.writeCSV(categoryList, outFile)
    Run.runProcessParallelLogin(session, itemURL, liTagList, outFile, numOfUrl)
    outFile.close()
    Greeting.sysExit(csvOut)
    
if __name__ == "__main__":
    main()
