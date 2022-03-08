import json
import csv
import os

releases = []

if __name__ == "__main__":
    with open('../jquery-data/jquery_releases.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            releases.append(row)
    


    for release in releases:
        print(f"Executing Cloc for release {release['tag']}")
        os.system(f"cloc ../jquery-data/{release['tag']}/")
