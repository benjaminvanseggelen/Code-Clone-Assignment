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
            read = stream.read(9999999)

            try:
                output = json.loads(read)
            except ValueError as e:
                print(f"No JSON continueing: {read}")
                continue
            
            def file_len(fname):
                with open(fname) as f:
                    for i, l in enumerate(f):
                        pass
                return i + 1

            loc_vi = loc[x]['loc'] 
            loc_vj = loc[y]['loc'] 

            # Calculating without using cloc
            loc_self_vi = 0
            loc_self_vj = 0

            loc_cij = 0

            similar_lines_i = {}
            similar_lines_j = {}

            for i in range(len(output)):
                for j in range(len(output[i]['instances'])):
                    path = output[i]['instances'][j]['path']
                    if file1 in path:
                        if not path in similar_lines_i:
                            similar_lines_i[path] = []
                        loc_self_vi += file_len(path)
                        similar_lines_i[path] += range(output[i]['instances'][j]['lines'][0], output[i]['instances'][j]['lines'][1])
                        similar_lines_i[path] = list(dict.fromkeys(similar_lines_i[path]))
                    if file2 in path:
                        if not path in similar_lines_j:
                            similar_lines_j[path] = []
                        loc_self_vj += file_len(path)
                        similar_lines_j[path] += range(output[i]['instances'][j]['lines'][0], output[i]['instances'][j]['lines'][1])
                        similar_lines_j[path] = list(dict.fromkeys(similar_lines_j[path]))

            for key in similar_lines_j:
                loc_cij += len(similar_lines_j[key])
            for key in similar_lines_i:
                loc_cij += len(similar_lines_i[key])

            loc_ci = 0
            for key in similar_lines_i:
                loc_ci += len(similar_lines_i[key])

            #Coverage book
            cov_book = loc_cij/(loc_self_vj + loc_self_vi)

            #Coverage ours
            cov_ours = loc_ci/loc_self_vi

            print(f"Book's coverage metric between jQuery {loc[x]['tag']} en {loc[y]['tag']}: {cov_book}")
            print(f"Our coverage metric between jQuery {loc[x]['tag']} en {loc[y]['tag']}: {cov_ours}")
            # print(f"Coverage ours: {cov_ours}")
