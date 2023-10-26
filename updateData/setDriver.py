from selenium import webdriver
from scrape_players_and_stats import *
import requests
from get_url import *
from selenium.webdriver.chrome.options import *

def setDriver():
    
    
        urls=get_url()

    
        # Initialize WebDriver
        #put youre chrome driver path
        webdriver_path = 'E:/chromedriver_win32/chromedriver.exe'
       
        driver = webdriver.Chrome()
        try:
                for url in urls:
                        driver.get(url)
                        scrape_players_and_stats(driver, url, webdriver_path)
        finally:
                        # Close the WebDriver when done
                        driver.quit()

