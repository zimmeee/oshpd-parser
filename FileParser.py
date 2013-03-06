# zimmen@insight~/Documents/Projects/Healthcare/ChargeMaster/src> python FileParser.py 
# /Users/zimmen/Documents/Projects/Healthcare/ChargeMaster/data/CDM/test/106190315_CDM_2008.csv
# ['CDM', 'CHARGE DESCRIPTION', '  PRIOR PRICE', 'CUR PRICE']
# /Users/zimmen/Documents/Projects/Healthcare/ChargeMaster/data/CDM/test/106190323_CDM_2008.csv
# ['Charge#', 'Charge Description', 'HCPCS Code', 'June 2008 Price']
# ['CHARGE CODE', 'DESCRIPTION', 'CHARGE AMOUNT']
# ['Procedure #', 'Description', 'Charge']
#
# # /Users/zimmen/Documents/Projects/Healthcare/ChargeMaster/data/CDM/test/106564121_CDM_All_2009.csv
# /Users/zimmen/Documents/Projects/Healthcare/ChargeMaster/data/CDM/test/106301098_CDM_All_2007.csv

import csv
import glob

def nonEmptyEntries( row ):
	return len( [x for x in row if x] )

def extractHeader( reader ):
	headers = []

	try:
		g = [line for line in reader]
		g[len(g) - 1]
   	except:
		return headers

	# Assume that the last line has the correct number of cols
	num_cols = nonEmptyEntries( g[len(g) - 1] )

	for line in g:
		if( nonEmptyEntries( line ) == num_cols ):
			headers = line
			break

	return headers


path_to_dir = '/Users/zimmen/Documents/Projects/Healthcare/ChargeMaster/data/CDM'

csv_files = glob.glob( '/'.join( [path_to_dir, '*.CSV'] ) )
for f in csv_files:
	print f
	reader = csv.reader( open( f ), delimiter = ";" )
	print extractHeader( reader ) 


