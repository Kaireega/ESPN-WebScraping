from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import plotly.express as px
import plotly.graph_objects as go
import copy

# Set up WebDriver and navigate to the initial URL
webdriver_path = '/Users/ree/Downloads/chromedriver-mac-arm64/chromedriver'
url = 'https://www.espn.com/college-football/stats/player'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
# Initialize WebDriver
driver = webdriver.Chrome()
driver.get(url)


def scrape_header():
    headers = BeautifulSoup(driver.page_source, 'lxml')
    header = headers.find(class_='Table__Scroller')
    pos = header.find('div')
    tags = header.find_all('a')
    stat_header = [g.get_text() for g in tags]
    stat_header = [pos.text] + stat_header
    return stat_header

# Function to scrape player names and stats


def scrape_players_and_stats():
    # Click "Show More" repeatedly until it's not available
    while True:
        try:
            show_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'loadMore__link')))
            show_more_button.click()

        except Exception as e:
            # print("No more 'Show More' button found. Exiting.")
            break

    # Scrape player names and stats from the fully loaded page
    soup = BeautifulSoup(driver.page_source, 'lxml')
    players_chart = soup.find(class_='Table__TBODY')

    # Scrape player names
    player_tags = players_chart.find_all('a')
    players = [tag.get_text() for tag in player_tags]

    # Scrape player stats
    tbody_elements = soup.find_all(class_='Table__TBODY')

    if len(tbody_elements) >= 2:
        second_players_chart = tbody_elements[1]
        td_elements = second_players_chart.find_all('td', class_='Table__TD')

        # Initialize a list to group statistics in sets of 11
        grouped_stats = []

        for index, td_element in enumerate(td_elements):
            player_stat = td_element.get_text()

            # Add the player_stat to the current group
            if index % 11 == 0:
                grouped_stats.append([player_stat])
            else:
                grouped_stats[-1].append(player_stat)

    return players, grouped_stats


# Scrape header and player data
header = scrape_header()
players, grouped_stats = scrape_players_and_stats()

# Close the WebDriver when done
driver.quit()

# Create a DataFrame for the header
header_df = pd.DataFrame({'Header': header})

# Create a DataFrame for player data
data = {'Player': players}
for i, stat in enumerate(header):
    data[stat] = [stats[i] for stats in grouped_stats]
player_df = pd.DataFrame(data)
# print(player_df)

host = '127.0.0.1'
user = 'root'
password = 'BigDog13!'
database = 'webscraping'

conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database)
engine = create_engine(
    f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")

table_name = 'players'
cursor = conn.cursor()
# Create the table in MySQL using SQLAlchemy
player_df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

# Load data into the MySQL table using SQLAlchemy
player_df.to_sql(name=table_name, con=engine, if_exists='append', index=False)


conn.commit()
conn.close()
# Set display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# # Define the SQL query
# sql_query = """
#     SELECT DISTINCT Player, (RTG * 0.4) + (YDS * 0.3) + ((TD - 'INT') * 0.3) AS calculated_result
#     FROM webscraping.players;
# """

# # Execute the SQL query and fetch results into a DataFrame
# df = pd.read_sql(sql_query, con=engine)
# df = df.sort_values(by='calculated_result', ascending=False)
# print(df)
