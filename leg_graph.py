from leg import r2

partysize = len(r2)

partyx = []

# for i in range(0, 38):
# 	partyx += [r2[i]['old_roles'][0]['party']]

for i in range(0, partysize):
	partyx += [r2[i].get('party', "Unknown")]

print partyx.count('Democratic')
print partyx.count('Republican')
print partyx.count('Unknown')