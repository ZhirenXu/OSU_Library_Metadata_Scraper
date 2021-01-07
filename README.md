## Metadata Scrapper v1.2.5
Author: Zhiren Xu  
Publish data: 1/7/20

### What does it do
   OSU library has its digital collection repository, mainly contain scanned collections. This tool aim at scraping metadata from these records.
   
### Changelog
   Fix the bug that login return bad result when there is a login fail
   Rearrange header order according to requirement
   
### Prerequisites
   Run in Windows10 environment. 
   
   Must have admin level account in OSU library metadata department. 
   
   Python ver. 3.8 or higher, other version has not been tested. 
   
   Required Package: 
      
      BeautifulSoup 
      
   If not installed, please type following command in CMD: 
      
      pip install bs4  
      
### Instruction:  
   1. put csv file contain metadata's url in folder  
   2. run 'metaData_scraper.py'  
   3. follow instructions on display  
