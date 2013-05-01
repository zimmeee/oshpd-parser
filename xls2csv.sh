# Converts all the file names to uppercase
# Then converts all the XLS and XLSX files to CSV
# Usage: ./xls2csv.sh <dir>

if test "$1" == "" ; then
	echo $'\a'You forgot to specify the directory with the xls files to be converted
	echo $0 dir/with/xls/files
	exit
fi

# Convert file names to uppercase
for f in $1*.*; do
	convmv --notest --upper $f
done

# Convert the xls[x]? files to csv
for f in $1*.XLS $1*.XLSX; do
  	python xls2csv.py -i "$f" -o "${f%.*}.CSV" -p '%*%*%*%%' 
done
