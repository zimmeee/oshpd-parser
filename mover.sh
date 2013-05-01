dir=/Users/aernis/Documents/Projects/ChargeMaster/StrataRXcsv/
gooddir=/Users/aernis/Documents/Projects/ChargeMaster/StrataRXcsv/cleanFiles/
multidir=/Users/aernis/Documents/Projects/ChargeMaster/StrataRXcsv/multiCleanFiles/
notesdir=/Users/aernis/Documents/Projects/ChargeMaster/StrataRXcsv/notesFiles/
messydir=/Users/aernis/Documents/Projects/ChargeMaster/StrataRXcsv/messyFiles/
smalldir=/Users/aernis/Documents/Projects/ChargeMaster/StrataRXcsv/smallProbFiles/
blankdir=/Users/aernis/Documents/Projects/ChargeMaster/StrataRXcsv/BlankFiles/

#run this from the directory hwere the files are
cd $dir
for file in *
 do ls $file;
 python /Users/aernis/Documents/Projects/ChargeMaster/code/parser.py $file
 echo 'perfect? p ?multi-line m but good, n notes, huge mess h, blank b, small problems s'
 read a;
 if [[ $a == "p" ]]; then
     echo 'mv $file ${gooddir}${file}'
     mv $file ${gooddir}${file}
 elif [[ $a == "m" ]]; then
     echo 'mv $file ${multidir}${file}'
     mv $file ${multidir}${file}
 elif [[ $a == "n" ]]; then
     echo 'mv $file ${notesdir}${file}'
     mv $file ${notesdir}${file}
 elif [[ $a == "h" ]]; then
     echo 'mv $file ${messydir}${file}'
     mv $file ${messydir}${file}
 elif [[ $a == "s" ]]; then
     echo 'mv $file ${smalldir}${file}'
     mv $file ${smalldir}${file}
 elif [[ $a == "b" ]]; then
     echo 'mv $file ${blankdir}${file}'
     mv $file ${blankdir}${file}
fi
 echo ''
 echo ''
 echo ''
 echo ''
 echo ''
 echo ''
 echo ''
 echo ''
done;


common problem MAYBEHEADERS:106105029_CDM_ALL_2009.CSV Urinalysis, without microscopy%*%*%*%%81002 or 81003%*%*%*%%31.29
MAYBEHEADERS:106105029_CDM_ALL_2009.CSV Urinalysis, with microscopy%*%*%*%%81000 or 81001%*%*%*%%

other common things
panel
Cost/Time Dependent
cost + 10%
variable
minimum
ranges $16,500.00 - $51,700.00
various
counter
no charge

good notes test file
106361110_CDM_ALL_2006

good multiple test file
106382715_CDM_2007


notesdir=/Users/aernis/Documents/Projects/ChargeMaster/StrataRXcsv/notesFiles/
cleannotesdir=/Users/aernis/Documents/Projects/ChargeMaster/StrataRXcsv/notesFiles/cleanNotes/
for file in *
 do ls $file;
 python /Users/aernis/Documents/Projects/ChargeMaster/code/github/oshpd-parser/parser.py $file
 echo 'now clean? y '
 read a;
 if [[ $a == "y" ]]; then
     echo 'mv $file ${cleannotesdir}${file}'
     mv $file ${cleannotesdir}${file}
  fi
done;