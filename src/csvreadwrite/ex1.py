import csv
import os

thispath = os.path.abspath(__file__)
thisdir = os.path.dirname(thispath)

datafile = 'dataread.csv'
datapath = os.path.join(thisdir, datafile)

# Read
with open(datapath, 'r') as f:
    data = csv.reader(f)
    for rowdata in data:
        print(rowdata)
    
    print(data.line_num)


# Dict reader
with open(datapath, 'r') as f:
    data = csv.DictReader(f)
    for rowdata in data:
        print(rowdata)

    print(data.fieldnames)
    print(data.line_num)

