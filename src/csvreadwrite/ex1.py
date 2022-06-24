import csv
import os

thispath = os.path.abspath(__file__)
thisdir = os.path.dirname(thispath)

datafile = 'dataread.csv'
datapath = os.path.join(thisdir, datafile)


# Check has_header
with open(datapath, 'r') as f:
    has_header = csv.Sniffer().has_header(f.read())
    print(has_header)


# Read
with open(datapath, 'r') as f:
    data = csv.reader(f, delimiter=',', skipinitialspace=True)
    for rowdata in data:
        print(rowdata)
    
    print(data.line_num)


# Dict reader
with open(datapath, 'r') as f:
    data = csv.DictReader(f, delimiter=',', skipinitialspace=True)
    for rowdata in data:
        print(rowdata)

    print(data.fieldnames)
    print(data.line_num)

