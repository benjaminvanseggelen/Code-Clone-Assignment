import json
import csv
import os

releases = []
releases_loc = []

if __name__ == "__main__":
    with open('../jquery-data/jquery_releases.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            releases.append(row)

        for release in releases:
            print(f"Executing Cloc for release {release['tag']}")
            src_loc_csv = csv.reader(os.popen(f"cloc --csv --exclude-lang=CSS,HTML --quiet ../jquery-data/{release['tag']}/src").read().split('\n'))
            external_loc_csv = csv.reader(os.popen(f"cloc --csv --exclude-lang=CSS,HTML --quiet ../jquery-data/{release['tag']}/external").read().split('\n'))

            src_loc = 0
            external_loc = 0

            for row in src_loc_csv:
                if len(row) >= 2 and row[1] == 'Javascript':
                    src_loc = int(row[4]) + int(row[3]) + int(row[2])
                    # code + comment + blank
                    break

            for row in external_loc_csv:
                if len(row) >= 2 and row[1] == 'Javascript':
                    external_loc = int(row[4]) + int(row[3]) + int(row[2])
                    # code + comment + blank
                    break

            #total_loc = src_loc + external_loc

            total_loc = src_loc
            releases_loc.append({
                'tag': release['tag'],
                'loc': total_loc
            })


    with open('loc.json', 'w') as json_f:
        json.dump(releases_loc, json_f)