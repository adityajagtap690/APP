import csv

file = open("student.csv", "r")
reader = csv.reader(file)

for row in reader:
    print(row)

file.close()
