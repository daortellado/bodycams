import json
import requests
from formatted import r
import json

crazysize = len(r)

legs = []

no_leg =[]

url2 = []

for i in range(0, crazysize):
	legs += [r[i]['sponsors'][0]['leg_id']]

no_leg_num = legs.count(None)

no_leg = filter(None, legs)

no_leg_size = len(no_leg)

for i in range(0, no_leg_size):
	url2 += ['http://openstates.org/api/v1/legislators/%s/?apikey=6602b71c9fc34861ba0e16d86f9cd4af' % no_leg[i]]

print url2

r2 = []

for i in range (0, no_leg_size):
	r2 += [requests.get(url2[i]).json()]

jsonarrayx = json.dumps(r2)

print jsonarrayx

with open('legdetail.json', 'w') as f:
     json.dump(jsonarrayx, f)