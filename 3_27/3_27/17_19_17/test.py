from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('https://cn.bing.com/')

driver.quit()