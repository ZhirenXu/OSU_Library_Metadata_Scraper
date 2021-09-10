import urllib.request
import concurrent.futures
from bs4 import BeautifulSoup
from Code import FindCategoryValue
import requests
import time
from requests import Session

def loadUrl(url):
    html = urllib.request.urlopen(url)
    return html

def loadUrlSession(session, url):
    html = session.get(url)
    return html

##main process of the metadata scrapper
# @param    urlList
#           a list contains url that wait to be scrapped
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
    
    with concurrent.futures.ThreadPoolExecutor(max_workers = 5) as executor:
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
            #FindObjectTitle.findObjectVisibility(soup, categoryValue)
            # find original url link
            categoryValue.append(url)
            # find attributes value
            FindCategoryValue.findCategoryValue(soup, liTagList, categoryValue, outputFile)
            print("We have successfully web-scraped ", i, " / ", numOfUrl, " records")
            # reset categoryValue for next collection
            categoryValue = []
            i = i + 1

##main process of the metadata scrapper with login session
# @param    session
#           a session which contain login cookie
# @param    urlList
#           a list contain url that wait to be scrapped
# @param    liTagList
#           A list contain all the <li> tag we need
# @param    outputFile
#           a CSV file for output
# @param    numOfUrl
#           How many url need to be scraped
def runProcessParallelLogin(session, urlList, liTagList, outputFile, numOfUrl):
    # iterator to show program progress
    categoryValue = []
    i = 1
    
    with concurrent.futures.ThreadPoolExecutor(max_workers = 5) as executor:
        future_to_url = {executor.submit(loadUrlSession, session, url): url for url in urlList}
        for future in concurrent.futures.as_completed(future_to_url):
            t_start = time.process_time()
            # original url link
            url = future_to_url[future]
            # opened url
            html = future.result()
            # load target digital collection in html parser
            soup = BeautifulSoup(html.text, 'html.parser')
            # find internal id link
            categoryValue.append(url)
            # find attributes value
            FindCategoryValue.findCategoryValue(soup, liTagList, categoryValue, outputFile)
            print("We have successfully web-scraped ", i, " / ", numOfUrl, " records")
            t_end = time.process_time()
            print("Process Time: ", t_end - t_start)
            print("\n")
            # reset categoryValue for next collection
            categoryValue = []
            i = i + 1
