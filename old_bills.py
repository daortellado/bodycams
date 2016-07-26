import json
import re
json_file = open('data.json', 'r')
values = json.load(json_file)
json_file.close()
bills = []
allbills = {}

states_dict = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

inv_states_dict = dict([[v,k] for k,v in states_dict.items()])

# state = [values[i]['state'] for i in range(50)]

for item in values:
    alt_format = re.findall('(HB|HF|SB|AB)s (\d+) & (\d+)', item['Legislation or Bill(s)'])
    for i in alt_format:
        bills += [i[0], i[1], i[0], i[2]]
    bills +=  re.findall('((HB|HF|SB|AB|H) \d+)',  item['Legislation or Bill(s)'])

bills =  [i[0] for i in bills]


# allbills = {k: inv_states_dict[k] for k in bills if k in inv_states_dict}

allbills['AZ'] = bills
# print bills
# print state
print bills

## MORE CRAZY SHIT

#print each_bill

def print_keyword_args1(**each_bill):
# kwargs is a dict of the keyword args passed to the function
    for key, value in each_bill.iteritems():
        if key in ['state']:
            print "%s = '%s'" % (key, value)

def print_keyword_args2(**each_bill):
# kwargs is a dict of the keyword args passed to the function
    for key, value in each_bill.iteritems():
        if key in ['bill_id']:
            print "%s = '%s'" % (key, value)

x = print_keyword_args2(**each_bill[0])
y = print_keyword_args1(**each_bill[0])
#bodycam1 = sunlight.openstates.bills(functools.partial(print_keyword_args2, **each_bill[0]), functools.partial(print_keyword_args2, **each_bill[0]))


# state_abbrev_to_bill_list[state] = [] 