from helpers import get_empty_dict, open_json, update_dict

import re, states

def get_bills_dict():
    # Extract data & get starter dictionary
    data       = open_json('data.json', 'r')
    bills_dict = get_empty_dict()
    
    # Iteratively update dictionary
    map(lambda entry : update_dict(bills_dict, entry), data)
    
    # bills_dict contains what you need.
    return bills_dict

get_bills_dict()