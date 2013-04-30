# Filters out the CDM files from the full set of downloaded files
# 
# To run: Change path_to_dir to the directory containing all of the OHSPD
# XLS and XLSX files then:
#		python FileChecker.py
# Matching files will be MOVED to path_to_dir/CDM 
# 
# Data files retrieved from 
# http://www.oshpd.ca.gov/chargemaster/default.aspx
# on 3/5/2013
#
# Downloaded *.xls (6392 files), actually downloaded 6294 (mostly 403 errors)
# 
# According to OHSPD, it contains 479 Hospitals and spans 8 years
# Upper bound on the number of matching records: 479 * 8 = 3832
# Actual number of matching records: 3220
#

import os
import re  

path_to_dir = '/Users/aernis/Documents/ChargeMaster/originalXls'

p = re.compile('(\d+)+[_|-]cdm[_|-]?(all)?_(\d{4})', re.IGNORECASE)

counter = 0

files_in_dir = os.listdir( path_to_dir )
for f in files_in_dir:
	m = p.match( f )
	if m:
		src  = path_to_dir + os.sep + f
		dest = path_to_dir + os.sep + 'CDM' + os.sep + f
		print src
		print dest
		os.rename( src, dest )
		print f
		counter = counter + 1

print 'Matching data files:', counter
