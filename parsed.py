from formatted import r
import json
import io

crazysize = len(r)

cleaned_data = []

# for i in range(0, crazysize):
# 	cleaned_data = {'state' : r[i]['state'], 'bill' : r[i]['bill_id'], 
# 		'introduced' : r[i]['action_dates']['first'], 'introduced' : r[i]['action_dates']['last'], 'signed' : r[i]['action_dates']['signed']}
# 	cleaner.append(cleaned_data)
first_date = []
last_date = []
first_date_string = []
last_date_string = []

for i in range(0, crazysize):
	first = r[i]['action_dates']['first']
	last = r[i]['action_dates']['last']
	first_date += [[first[:4], first[5:7], first[8:10]]]
	last_date += [[last[:4], last[5:7], last[8:10]]]

for i in range (0, crazysize):
	first_date_string += [', '.join(first_date[i])]
	last_date_string += [', '.join(last_date[i])]

# for i in range(0, crazysize):
# 	cleaned_data += [['\'%s\''%r[i]['bill_id'], '\'%s\''%r[i]['bill_id'], '\'%s\''%r[i]['state'], 'new Date(%s)' % first_date_string[i], 'new Date (%s)' % last_date_string[i], 'null', '100', 'null']]

for i in range(0, crazysize):
	cleaned_data += [['\'%s\''%r[i]['state'], '\'%s\''%r[i]['bill_id'], 'new Date(%s)' % first_date_string[i], 'new Date (%s)' % last_date_string[i]]]


print cleaned_data

jsonarray2 = json.dumps(cleaned_data)

print len(cleaned_data)

print jsonarray2
# # 'signed' : r[i]['action_dates']['signed']

# with open('billsshortened.json', 'w') as f:
#       json.dump(jsonarray2, f)

with io.open('billsshortened.json', 'w', encoding='utf8') as json_file:
  data = json.dumps(jsonarray2, ensure_ascii=False, encoding='utf8')
  json_file.write(unicode(data))