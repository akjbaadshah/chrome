import time
from selenium import webdriver
driver=webdriver.Chrome(executable_path=r"C:\Akj\chromedriver.exe")
driver.get('https://www.google.com/')
time.sleep(5)
driver.quit()

