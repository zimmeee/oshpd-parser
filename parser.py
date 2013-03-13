import sys



##should only accept as headers the ones that are 100% text

#have to deal with all these events for charge errors because it's not counting the commas and allowign non-price columns to dominate

#ways that procedures are represented
#Code
#Service code
#charge code
#CPT CODE but CPT CODES with more is a description
#item number
#CDM

#ways that money is represented
#charge             but not charge description
#price 
#prices
#TOTAL PROCE
#STD AMOUNT
#revenue
#chg_amt
#CHRG AMT
#lst chg

##if the most recent header is smaller then we must maintain the previous header

#need to make exceptions for blanks and N/As
#"NA"
#can also remove ? if we want
f=open(sys.argv[1],'r')
d=f.readlines()
f.close()

##first we want to identify what the real regions are where the data is icnluded

lengths=[]

numCols = [0,0,0,0,0,0,0]


#first identify the normal number of fields to have
for i in range(len(d)):
    v=d[i].rstrip().split("%*%*%*%%")
    lenVal = len(v)
    #print lenVal, d[i]
    try:
        numCols[lenVal]+=1
    except:
        while lenVal >= len(numCols):
            numCols.append(0)
        numCols[lenVal]+=1
print numCols

#the one with the field numbers should have a clear winner
nCols = numCols.index(max(numCols)) 

print nCols

#this will track how many are numeric
isNumeric=[0 for i in range(nCols)]

#identify the numerical columns
totalGood=0
for i in range(len(d)):
    v=d[i].rstrip().split("%*%*%*%%")
    #if this is a columns wtih the wrong number then skip it
    if len(v) == nCols:
        totalGood+=1
        for j in range(len(v)):
            try:
                temp = float(v[j].replace(",",""))
                isNumeric[j]+=1
            except ValueError:
                #print 'not a numeric',v[j]
                1==1
#figure out which columns are usually numeric, these will be the only ones
#where we aren't looking at more data
print isNumeric
print totalGood
maxGood=max(isNumeric)

#the ones where >50% are numeric we will call fixed numeric fields
checkNumeric=[]
for i in range(len(isNumeric)):
    if isNumeric[i] > maxGood*.95:
        checkNumeric.append(i)
print checkNumeric
print maxGood*.95,maxGood
failLines=[]
#now go through and parse fields
for i in range(len(d)):
    v=d[i].rstrip().split("%*%*%*%%")
    if len(v) != nCols:
        continue
#        failLines.append(i)
    else:
        needsWork=0
        for j in checkNumeric:
            try:
                temp = float(v[j].replace(",",""))
            except ValueError:

                ##these are actually null values
                if v[j].upper() not in ['','NA','-','NULL'] and len(v[j].split())!=0:

                    needsWork=1
        if needsWork:
            failLines.append(i)

print "WE ARE CHECKING THESE"
print checkNumeric
needsWork=len(failLines)
potentialLines=[]
realLines=[]

#number of problems
probLine=0
for i in failLines:
    print 'MAYBEHEADERS:\t',sys.argv[1],d[i].rstrip()

    v=d[i].rstrip().split("%*%*%*%%")
    countOff=0
    for j in checkNumeric:
        try:
            temp = float(v[j].replace(",",""))
        except ValueError:
            if v[j].upper() not in ['','NA','-','NULL'] and len(v[j].split())!=0:
                countOff+=1
    if countOff < len(checkNumeric):
        probLine+=1
        realLines.append(i)
    potentialLines.append(i)

for i in realLines:
    print 'REALHEADERS:\t',sys.argv[1],d[i].rstrip()
print potentialLines

totalLen=len(d)
print len(realLines),needsWork, 1.*(totalLen-needsWork)/totalLen
