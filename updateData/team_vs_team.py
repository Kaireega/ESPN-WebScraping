from UpdateWeekCSV import *
from scrape_header import *
from week_finder import *
from vs_who_url import *




def team_vs_team(driver, url, webdriver_path):
    
    # Scrape info 
    header=scrape_header(driver,"t")
    
    
    
    #saving player data to csv
    urls=vs_who_url() 
    
    for i in range (0,len(urls)):
        if url==urls[i]:
            name=f"/espn/data/week{i}.csv"
            UpdateWeekCSV(header,name)
   