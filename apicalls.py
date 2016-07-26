from bills import get_bills_dict

import functools, json, logging, sunlight

logging.basicConfig(level=logging.DEBUG)
sunlight.config.API_KEY = '6602b71c9fc34861ba0e16d86f9cd4af'

bills_dict = get_bills_dict()
second = ['NM', 'FL', 'AZ', 'MD', 'UT']
each_bill = []
each_bill2 = []

for k,v in bills_dict.items():
	if k in second:
		for index, element in enumerate(v):
			each_bill2 += [{'state' : k, 'bill_id' : v[index]}]
	else:
		for index, element in enumerate(v):
			each_bill += [{'state' : k, 'bill_id' : v[index]}]		

print each_bill2

# Fetch
# ============================================================================ 
bodycam1 = []
unregistered = []

for index, element in enumerate(each_bill):
	inspect = sunlight.openstates.bills(**each_bill[index])
	try:
		bodycam1.append(inspect[0])
	except IndexError:
		print("No data returned for: {0}.".format(element))
		unregistered.append(element)

for index, element in enumerate(each_bill2):
	inspect = sunlight.openstates.bills(**each_bill2[index])
	try:
		bodycam1.append(inspect[1])
	except IndexError:
		print("No data returned for: {0}.".format(element))
		unregistered.append(element)

print("Retrieved data for {0}/{1} bills.".format(len(bodycam1), len(each_bill)))

billids = [d['id'] for d in bodycam1]

print billids

# d = dict.fromkeys(', ids)

jsonarray = json.dumps(bodycam1)

print jsonarray
