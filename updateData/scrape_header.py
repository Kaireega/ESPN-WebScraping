import re
from bs4 import BeautifulSoup

def scrape_header(driver, type):
    if type == 'p':
        headers = BeautifulSoup(driver.page_source, 'lxml')
        header = headers.find(class_='Table__Scroller')
        tags = header.find_all('a')
        stat_header = [g.get_text() for g in tags]
        stat_header.insert(0, 'POS')
        return stat_header

    elif type == 't':
            # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'lxml')

        # Find all divs with class 'ScheduleTables'
        schedule_tables_list = soup.find_all(class_='ScheduleTables')

        # Initialize a list to store the extracted information
        info_list = []

        # Iterate through each ScheduleTables element and extract information
        for schedule_tables in schedule_tables_list:
            # Find all <tr> elements within the current ScheduleTables
            tr_elements = schedule_tables.find_all('tr', class_='Table__TR')

            for tr in tr_elements:
                # Find all <td> elements within the <tr> element
                td_elements = tr.find_all('td')
                for td in td_elements:
                    info_list.append(td.get_text(strip=True))

        # Initialize a list to store the dictionaries
        info_list_dict = []
        
        # Iterate through info_list in chunks of 6
        for i in range(0, len(info_list), 6):
            info = {
                'Team': info_list[i],
                'Opo Team': info_list[i + 1],
                'Score': info_list[i + 2],
                'Players': info_list[i + 3:i + 6]
            }

            # Process and split player information for each player in the 'Players' field
            for j, player_string in enumerate(info['Players']):
                match = re.match(r"([A-Za-z\s]+)(\d+)", player_string)

                if match:
                    player_name = match.group(1).strip()
                    player_stats = match.group(2)
                    info['Players'][j] = {'Player': player_name, 'Stats': player_stats}
                else:
                    info['Players'][j] = {'Player': player_string, 'Stats': ''}

            info_list_dict.append(info)

        # Return the result as a list of dictionaries
        return info_list_dict
