from selenium import webdriver
from selenium.webdriver.common.keys import Keys


wd_path="/home/ayyuce/chrome/chromedriver"
wd = webdriver.Chrome(executable_path=wd_path)
wd.get("https://www.yurticikargo.com/")
shipmentSRC = wd.find_element_by_id("shipment-search-btn")
shipmentSRC.send_keys('gonderi_kodunuzu_girin')
shipmentSRC.send_keys(Keys.ENTER)
