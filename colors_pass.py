from formatted import r

crazysized = len(r)

colors = []

for i in range(0, crazysized):
	colors += [r[i]['state'], r[i]['action_dates']['signed']]

for i in range(0, crazysized):
 	colors += [r[i]['state']]

newco = ['#ffcccc' if x==None else '#99ff66' for x in colors]

print colors