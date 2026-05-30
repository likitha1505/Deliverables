import csv
result = []
with open("grades.csv","r")as infile:
    reader = csv.reader(infile)
    next(reader)
    for row in reader:
        Name = row[0]
        marks=list(map(int,row[1:]))
        average = sum(marks)/len(marks)
        result.append([Name,average])
with open("results.csv","w")as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Name","average"])
    writer.writerows(result)
