import json
import csv
import os

if __name__ == "__main__":

    f = open('loc.json')
    loc = json.load(f)


    for x in range(len(loc)):    
        for y in range(x + 1, len(loc)):
            file1 = f"../jquery-data/{loc[x]['tag']}"
            file2 = f"../jquery-data/{loc[y]['tag']}"

            stream = os.popen(f"jsinspect {file1} {file2}")
            read = stream.read()
            if read == "":
                continue
        
            output = json.loads(read)
            
            loc_vi = loc[x]['loc'] 
            loc_vj = loc[y]['loc'] 

            loc_cij = 0

            for i in range(len(output)):
                # Check whether we are not adding things of the same file
                prev_path = ''
                for j in range(len(output[i]['instances'])):
                    if prev_path == output[i]['instances'][j]['path']:
                        continue
                    prev_path = output[i]['instances'][j]['path']
                    line_from = output[i]['instances'][j]['lines'][0] - 1
                    line_to = output[i]['instances'][j]['lines'][1]
                    loc_cij += (line_to - line_from)

            #Coverage book
            cov_book = loc_cij/(loc_vi + loc_vj)

            #Coverage ours
            cov_ours = (loc_cij*2)/(loc_vi + loc_vj)

            print(f"Coverage book: {cov_book}")
            print(f"Coverage ours: {cov_ours}")
