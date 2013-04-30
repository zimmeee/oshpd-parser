# 
# This is a starter for file parsing. At the time of writing
# this only tries to pick out the headers
# 
import sys
import csv
import glob

UNKNOWN = '^^^ UNKNOWN ^^^'

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
   	except ValueError:
		return headers

	# Assume that the last line has the correct number of cols
	num_cols = nonEmptyEntries( g[len(g) - 1] )

	for line in g:
		if( nonEmptyEntries( line ) == num_cols ):
			headers = line
			break

	return headers

# Gets the number of columns in the data file
def getNumCols( lines, threshold ):
	num_cols  = -1
	colCounts = [0] * 100
	numRows   = len(lines)

	if numRows == 0:
		return num_cols

	for r in lines:
		try:
			colCounts[nonEmptyEntries(r)] += 1
		except:
			print '@@@ ' + str( nonEmptyEntries(r) )

	# print colCounts
	
	# If at least 2% of the columns have a value
	# we'll consider it
	percentages = [x / float(numRows) for x in colCounts]

	# Get the smallest percentage greater than threshold
	ordered = sorted( percentages )

	for i in range(len(percentages)):
		if ordered[i] > threshold:
			num_cols = percentages.index( ordered[i] )
			break

	# print 'Picked ' + str(num_cols) + ' columns with ' + str(percentages[num_cols]) + ' complete rows.'
	return [num_cols, percentages[num_cols]]

# We assume the header is the first line that has 
# the correct number of columns and is all characters
def extractHeader2( reader ):
	headers = []

	lines = [line.rstrip().split("**") for line in reader]

	[numCols, percentage] = getNumCols( lines, 0.02)

	# if the # of cols is < 3 something funky is happening
	if numCols > 2: 
		for line in lines:
			if( nonEmptyEntries( line ) == numCols ):
				headers = line
				break
	else:
		headers = UNKNOWN

	return [headers, numCols, percentage]


def parseDir( path ):
	path_to_dir = '/Users/zimmen/Documents/Projects/Healthcare/ChargeMaster/data/CDM/csv'

	csv_files = glob.glob( '/'.join( [path_to_dir, '*.CSV'] ) )

	good = 0
	bad  = 0
	total = 0 

	for f in csv_files:
		# print f
		total = total + 1
		cdmFile = open( f, 'r' )
		[header, numCols, percentage] = extractHeader2( cdmFile )
		if header == UNKNOWN:
			bad = bad + 1
		else:
			# print ','.join( [f, str(numCols), str(header), str(percentage)] )
			good = good + 1

	print 'GOOD: ' + str(good) + '\tBAD: ' + str(bad)

#f = open(sys.argv[1],'r')

#headers = extractHeader2( f )
#print headers

parseDir( 'hello' )


