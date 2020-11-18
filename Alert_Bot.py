from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from twilio.rest import Client
#client = Client("your_twillio_keys", "your_twillio_id")
driver = webdriver.Chrome("'ChangeToPath'/chromedriver.exe")
driver.get("https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG?ref_=ast_sto_dp")
print(driver.title)
el = driver.find_element_by_tag_name('body')
str1=el.text 
if(str1.find("Currently unavailable.")!=-1):
    print("its still not available my guy")
else: 
    if(str1.find("$499")!=-1):
        print("yeet")
    else:
        print("Scalpers selling it")

driver.get("https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149")
print(driver.title)
el = driver.find_element_by_tag_name('body')
str1=el.text 
if(str1.find("Sold Out")!=-1):
    print("its still not available my guy")
else: 
    print("yeet")

driver.get("https://www.target.com/p/playstation-5-console/-/A-81114595")
print(driver.title)
el = driver.find_element_by_tag_name('body')
str1=el.text 
if(str1.find("Out of stock")!=-1):
    print("its still not available my guy")
else: 
    print("yeet")

driver.get("https://www.walmart.com/ip/PlayStation5-Console/363472942")
print(driver.title)
el = driver.find_element_by_tag_name('body')
str1=el.text 
if(str1.find("Out of stock")!=-1):
    print("its still not available my guy")
else: 
    print("yeet")

driver.get("https://deals.dell.com/en-us/compare/64x0")
print(driver.title)
el = driver.find_element_by_tag_name('body')
str1=el.text 
if(str1.find("Sorry, this deal has sold out.")!=-1):
    print("its still not available my guy")
else: 
    print("yeet")

driver.get("https://www.newegg.com/p/N82E16868110292")
print(driver.title)
el = driver.find_element_by_tag_name('body')
str1=el.text 
if(str1.find("OUT OF STOCK.")!=-1):
    print("its still not available my guy")
else: 
    print("yeet")
  
driver.close()
