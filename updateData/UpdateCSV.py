import csv

def UpdateCSV(players,schools,grouped_stats_dict,csv_file_path):
        

        # Create a list to store the data that will be written to the CSV file
        csv_data = []
        if(len(players)>1):
            # Iterate through each name in the list
            for i, player in enumerate(players):
                row = {
                    "Player": player,
                    "School": schools[i]
                }

                # Iterate through each key-value pair in the dictionary
                for key, value in grouped_stats_dict.items():
                        row[key] = value[i]

                csv_data.append(row)

            # Write the data to a CSV file
            with open(csv_file_path, 'w', newline='') as csv_file:
                fieldnames = ["Player", "School"] + list(grouped_stats_dict.keys())
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for row in csv_data:
                    writer.writerow(row)
        else:
            print("hi")
            with open(csv_file_path, 'w', newline='') as csv_file:
                fieldnames = list(grouped_stats_dict.keys())
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for row in csv_data:
                    writer.writerow(row)