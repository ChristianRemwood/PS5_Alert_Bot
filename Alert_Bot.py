from selenium import webdriver
from selenium.webdriver.common.keys import Keys
sites = [
    "https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG?ref_=ast_sto_dp"
    ,"https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
    ,"https://www.target.com/p/playstation-5-console/-/A-81114595"
    ,"https://www.walmart.com/ip/PlayStation5-Console/363472942"
    ,"https://deals.dell.com/en-us/compare/64x0"
    ,"https://www.newegg.com/p/N82E16868110292"
    ,"https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5/11108140.html"
]
lookFor = [
    ["Currently unavailable.","$499"]
    ,"Sold Out"
    ,"Out of stock"
    ,["Out of stock","online only at"]
    ,"Sorry, this deal has sold out."
    ,"OUT OF STOCK."
    ,"OUT OF STOCK"
    ]
status = {}
#from twilio.rest import Client
#client = Client("your_twillio_keys", "your_twillio_id")
driver = webdriver.Chrome("C:/Users/cremwood/Downloads/chromedriver_win32/chromedriver.exe")
for currentSite in range(len(sites)):
    driver.get(sites[currentSite])
    print("Checking:" + driver.title)
    el = driver.find_element_by_tag_name('body')
    str1=el.text 
    if (type(lookFor[currentSite]) == list):
        if(str1.find(lookFor[currentSite][0])!=-1):
            status[driver.title] = "Not Available"
        elif (str1.find(lookFor[currentSite][1])!=-1):
            status[driver.title] = "In Stock"
        else:
            status[driver.title] = "In Stock from Scalpers, or restock scheduled"
    else:
        if(str1.find(lookFor[currentSite])!=-1):
            status[driver.title] = "Not Available"
        else:
            status[driver.title] = "In Stock"

print (status)
driver.close()
