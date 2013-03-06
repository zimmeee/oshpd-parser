The purpose of this code is to compile ~3,000 excel spreadsheets into a single dataset. 

The files can be found at: http://www.oshpd.ca.gov/chargemaster/. Press the search button without supplying any arguments and it will return 6392 documents. Download ALL of the XLS and XLSX files - you may want to use a download manager like the good Firefox plug-in DownloadThemAll to help. Pick out the files that contain the ChargeMaster price list. I've included a script that I wrote to help me pick these out (FileChecker.py), but it may not be perfect. It is probably a reasonable starting place. 

Now you have all of the CDM files (~3220) in their own directory. The task is to compile these into a single cohesive dataset. The hard part, and the reason that it has proved difficult to automate, is that there is absolutely no standardized format. 

There are 3 main problems:
--------------------------

1. The column names are not standardized. For example:

	['CDM', 'CHARGE DESCRIPTION', '  PRIOR PRICE', 'CUR PRICE']
	['Charge#', 'Charge Description', 'HCPCS Code', 'June 2008 Price']
	['CHARGE CODE', 'DESCRIPTION', 'CHARGE AMOUNT']
	['Procedure #', 'Description', 'Charge']

2. The Excel spreadsheets frequently have multiple tabs, macros and may be encrypted. Therefore the conversion to from XLS to CSV is lossy and problematic. This can be seen in the large number of .CSV files with small sizes (~4kb) after conversion.

3. The files frequently have CSV formats that are formatted for human consumption, and contain sub-lists and sub-headers. For instance line 5 below represents a grouping which can be ignored for our purposes

    1: Evaluation & Management Services	2010 CPT Code	Outpatient Charge Amount
    2: Emergency Room Visit, Level 2 	99282	806.00
    3: Emergency Room Visit, Level 3 	99283	1,342.00
    4: Emergency Room Visit, Level 4 	99284	2,056.00
    5: Laboratory & Pathology Services	
    6: Basic Metabolic Panel	80048	178.00
    7: Comprehensive Metabolic Panel	80053	221.00
