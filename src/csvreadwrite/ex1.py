import csv
import os

thispath = os.path.abspath(__file__)
thisdir = os.path.dirname(thispath)

file_read = 'read.csv'
file_write = 'write.csv'

path_read = os.path.join(thisdir, file_read)
path_write = os.path.join(thisdir, file_write)


# Check has_header
with open(path_read, 'r') as f:
    has_header = csv.Sniffer().has_header(f.read())
    print(has_header)


# Read
with open(path_read, 'r') as f:
    data = csv.reader(f, delimiter=',', skipinitialspace=True)
    for rowdata in data:
        print(rowdata)
    
    print(data.line_num)


# Dict reader
with open(path_read, 'r') as f:
    data = csv.DictReader(f, delimiter=',', skipinitialspace=True)
    for rowdata in data:
        print(rowdata)

    print(data.fieldnames)
    print(data.line_num)

