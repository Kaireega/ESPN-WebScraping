# ESPN-WebScraping

#scrape_players_ans_stats.py
This script is responsible for scraping player statistics and organizing them into a dictionary. It will handle each link and extract player stats based on a predefined structure.
(The graph that will be made for each link will been done the same way as we do the DB)

If we were to add a DB, we will make it in a new file. "scrape_players_ad_stats.py" has the ability to upload the data from the dictionary that was created. This gives us control of each of the stats for each player where the player index = key value index. The key is equivalent to the header on each link. 
We create a key called 'POS' given it is not counted as a header but returns its key value back.

#scrape_header.py
This script is responsible for grabbing the headers (excluding 'POS') for the stats from a source. It could be used to obtain the column names for the statistics.


#main.py
The main script that orchestrates the scraping process for all links and manages the overall flow of the program.
