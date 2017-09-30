#!/usr/bin/python
import sys
import json
#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)


data=json.loads(sys.argv[1])

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

clean_data=json.dumps(data)

from pprint import pprint
pprint(data["matches"][0]["text"])

pprint("----")

pprint(clean_data)
