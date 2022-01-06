import requests
import xml.etree.ElementTree as ET  
import csv
from bs4 import BeautifulSoup

token = {insert token here}

#Import xml file
tree = ET.parse("C:\\Directory\\to\\file.xml")
root = tree.getroot()


for partvalue in root.iter("EbaySearch"):
    keyword = partvalue.text
    #add your appid to url here
    url = "https://open.api.ebay.com/shopping?callName=FindProducts&appid={your_app_id}&QueryKeywords=" +keyword

    payload={}

    headers = {
    'X-EBAY-API-IAF-TOKEN': token,
    'X-EBAY-API-VERSION': '1063',
    #SITE-ID 15 is for AU, if you want a different location change with appropriate - https://developer.ebay.com/devzone/merchandising/docs/concepts/siteidtoglobalid.html
    'X-EBAY-API-SITE-ID': '15'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    #Show reuslts
    #print(response.text)
    
    root = ET.fromstring(response.content)
    
    
    
    epid =[]   
    
    #add "productID" to epid list
    for child in root.iter("{urn:ebay:apis:eBLBaseComponents}ProductID"):

        epid.append(child.text)
        
        print("Our part number: " + keyword)
        print("EPID: " + epid[0])
        
        ######### CSV EXPORT #########
        with open("C:\\directory\\to\\output\\file.csv", 'a', newline='') as csvfile:
             partwriter = csv.writer(csvfile, delimiter= ";",
                                   quotechar='|',
                                   quoting=csv.QUOTE_MINIMAL)
             partwriter.writerow([keyword, epid[0]])
             
            
             csvfile.flush()
                