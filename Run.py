import urllib.request
import concurrent.futures
from bs4 import BeautifulSoup
import FindObjectTitle
import FindCategoryValue

def loadUrl(url):
    html = urllib.request.urlopen(url)
    return html

##main process of the metadata scrapper
# @param    url
#           the url that wait to be scrapped
# @param    liTagList
#           A list contain all the <li> tag we need
# @param    outputFile
#           a CSV file for output
# @param    numOfUrl
#           How many url need to be scraped
def runProcessParallel(urlList, liTagList, outputFile, numOfUrl):
    # iterator to show program progress
    categoryValue = []
    i = 1
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_url = {executor.submit(loadUrl, url): url for url in urlList}
        for future in concurrent.futures.as_completed(future_to_url):
            # original url link
            url = future_to_url[future]
            # opened url
            html = future.result()
            # load target digital collection in html parser
            soup = BeautifulSoup(html, 'html.parser', from_encoding = 'utf-8')
            # find collection title
            FindObjectTitle.findObjectTitle(soup, categoryValue)
            # find original url link
            categoryValue.append(url)
            # find attributes value
            FindCategoryValue.findCategoryValue(soup, liTagList, categoryValue, outputFile)
            print("We have successfully web-scraped ", i, " / ", numOfUrl, " records")
            # reset categoryValue for next collection
            categoryValue = []
            i = i + 1

