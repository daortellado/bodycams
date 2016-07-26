from re import findall
from states import ABBREVIATIONS, to_abbreviation

import json as J

def get_empty_dict():
  """ Generates an empty dict for storing State/Bill information. """
  return dict([key, []] for key in ABBREVIATIONS.keys())

def open_json(resource, mode):
    """ Open JSOn resource and close file handle. """
    
    json_file = open(resource, mode)
    values = J.load(json_file)
    json_file.close()
    
    return values

def update_dict(dict, json):
    """ Update the number of bills found for a given state. """
    bills = find_bills(json)
    state = find_state(json)
    
    if (state != None):
        dict[state] += bills

def find_bills(item):
    """ Finds bills mentioned in the Legislation or Bill(s) entry of an object. """
    bills = []
    legislation ='Legislation or Bill(s)'
    entry       = item[legislation]
    
    alternate_pattern = '(HB|HF|SB|AB)s? (\d+) & (\d+)'
    main_pattern      = '((HB|HF|SB|AB|H) \d+)'

    # Match pattern
    alt_entries  = findall(alternate_pattern, entry)
    main_entries = findall(main_pattern, entry)

    # Extract & return interesting entries
    bills += [data[0] for data in main_entries]

    for data in alt_entries:
        bills += [data[0], data[1], data[0], data[2]]
    
    return bills
    
def find_state(json):
    """ Returns the state name or abbreviation for the given JSON object. """
    if 'state' not in json:
        return None
    else:
        return to_abbreviation(json['state'])
