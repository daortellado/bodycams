from apicalls import billids, jsonarray
import json
import requests

billidsize = len(billids)

url = []

for i in range(0, billidsize):
	url += ['http://openstates.org/api/v1/bills/%s/?apikey=6602b71c9fc34861ba0e16d86f9cd4af' % billids[i]]

print url

r = []

for i in range (0, billidsize):
	r += [requests.get(url[i]).json()]

#stuff = r.json()

jsonarray1 = json.dumps(r)

print jsonarray1

with open('billdetail.json', 'w') as f:
     json.dump(jsonarray1, f)

with open('billsearch.json', 'w') as f:
     json.dump(jsonarray, f)