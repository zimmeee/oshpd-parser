import sys
import os

path_to_dir = '/Users/zimmen/Documents/Projects/Healthcare/ChargeMaster/data/CDM/csv'

# This has the list of files to parse
f = open( sys.argv[1], 'r' )
d = f.readlines()
f.close()

for i in range(len(d)):
	filename = d[i].strip()
	stringtoexecute = 'python parser.py ' + '/'.join( [path_to_dir, filename] ) + ' headerDump.csv'
	# print stringtoexecute
	os.system( stringtoexecute ) 