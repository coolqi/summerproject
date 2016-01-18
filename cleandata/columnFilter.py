import csv
from collections import defaultdict

columns = defaultdict(list) # each value in each column is appended to a list
newfile = open('newpost.csv','w+')
with open('post001.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    fieldnames = ['Title', 'Description']
    writer = csv.DictWriter(newfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for row in reader:
        writer.writerow({fieldnames[0]: row[fieldnames[0]], fieldnames[1]: row[fieldnames[1]]})
        