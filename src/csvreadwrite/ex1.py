import csv
import os

thispath = os.path.abspath(__file__)
thisdir = os.path.dirname(thispath)

file_read = 'read_header.csv'
file_read_noheader = 'read_noheader.csv'
file_write = 'write.csv'

path_read = os.path.join(thisdir, file_read)
path_read_noheader = os.path.join(thisdir, file_read_noheader)
path_write = os.path.join(thisdir, file_write)


# Check has_header
with open(path_read, 'r') as f:
    has_header = csv.Sniffer().has_header(f.read())
    print(has_header)


# reader
with open(path_read, 'r') as f:
    data = csv.reader(f, delimiter=',', skipinitialspace=True)
    for rowdata in data:
        print(rowdata)
    
    print(data.line_num)


# DictReader
with open(path_read, 'r') as f:
    data = csv.DictReader(f, delimiter=',', skipinitialspace=True)
    for rowdata in data:
        print(rowdata)

    print(data.fieldnames)
    print(data.line_num)


# DictReader (csv with no header)
with open(path_read_noheader, 'r') as f:
    fieldnames = ['Item', 'Calories(Cal)', 'Total Fat(g)', 'Total Carbs(g)', 'Protein(g)']
    data = csv.DictReader(f, delimiter=',', skipinitialspace=True, fieldnames=fieldnames)
    for rowdata in data:
        print(rowdata)

    print(data.fieldnames)
    print(data.line_num)


# writer
with open(path_write, 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['Vanilla Cone', 200, 5, 33, 5])
    writer.writerow(['Baked Apple Pie', 230, None, None, 2])


# DictWriter
with open(path_write, 'w', newline='') as f:
    fieldnames = ['Item', 'Calories(Cal)', 'Total Fat(g)', 'Total Carbs(g)', 'Protein(g)']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    
    writer.writerow({'Item': 'Vanilla Cone', 
                      'Calories(Cal)': 200, 
                      'Total Fat(g)': 5, 
                      'Total Carbs(g)': 33, 
                      'Protein(g)': 5})
    
    writer.writerow({'Item': 'Baked Apple Pie', 
                      'Calories(Cal)': 230, 
                      'Protein(g)': 2})

