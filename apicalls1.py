import sunlight
import json
from bills import get_bills_dict
import functools

import logging
logging.basicConfig(level=logging.DEBUG)
sunlight.config.API_KEY = '6602b71c9fc34861ba0e16d86f9cd4af'

bills_dict = get_bills_dict()

each_bill = []

for k,v in bills_dict.items():
	for index, element in enumerate(v):
		each_bill += [{'state' : k, 'bill_id' : v[index]}]

print each_bill

each_bill_size = len(each_bill)

print each_bill_size

bodycam1 =[]

for i in range(0, each_bill_size):
	bodycam1 += [sunlight.openstates.bills(**each_bill[i])[0]]
logging.debug(bodycam1)
#logging.debug(type(bodycam1))
d = bodycam1
jsonarray = json.dumps(d)

print jsonarray

#print(bills_dict)