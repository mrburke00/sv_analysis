import requests
import csv
print('begin')
with open("horse/cluster_coords.txt", newline='') as f:
        with open('cluster_ant.txt', 'w') as o:
                data = csv.reader(f, delimiter = "\t")
                for line in data:
                        print(line)
                        url = "https://dfam.org/api/annotations"
                        params = {
                                # The summary format is metadata-only and does not include
                                # full details such as the consensus sequence and citation
                                "assembly":"DAequCab2.0",
                                "chrom":line[0],
                                "start":line[1],
                                "end":line[2],
                                "nrph":'true',
                        }
                        queries = []
                        types =[]
                        response = requests.get(url, params=params)
                        results = response.json()['hits']
                        #print(results)
                        #print(len(results))
                        for i in range(len(results)):
                                #print(results[i]['query'])
                                #print(results[i]['type'])
                                queries.append(results[i]['query'])
                                types.append(results[i]['type'])
                        print(queries)
                        print(types)
                        o.write('{}\t{}\t{}\t{}\t{}'.format(line[0], line[1], line[2], queries, types))
                        o.write('\n')


