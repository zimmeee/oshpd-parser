# 
# This is a starter for file parsing. At the time of writing
# this only tries to pick out the headers
# 

import csv
import glob

def nonEmptyEntries( row ):
	return len( [x for x in row if x] )

# Naive algorithm for finding the header:
# Get the number of columns in the last line of the file
# and treat this as the number of data columns, N
# (assumption that this is a line of data, not comments)
# 
# Loop through line by line and return the first line 
# containing N non-empty elements
#
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


