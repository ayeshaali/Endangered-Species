import csv

f = open('funfacts.csv', 'r')
data = csv.reader(f)

f1 = open('newfunfacts.csv', 'w')
write = csv.writer(f1)

for i in data:
	a = str(i)
	split2 = a.split(' * ')
	write.writerow(split2)

