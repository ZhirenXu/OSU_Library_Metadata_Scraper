import sys

## print program info
def showInfo():
    print("******************************")
    print("*  Metadata Scrapper v1.2.7  *")
    print("*     Author: Zhiren Xu      *")
    print("*  published data: 04/20/21  *")
    print("******************************")

## print exit message
# @param    fileOut
#           name of output file
def sysExit(fileOut):
    print("The program is finished. The output file is: ", fileOut, " . It is located in the same folder with your main.py program. Press enter to exit.")
    key = input()
    sys.exit()
