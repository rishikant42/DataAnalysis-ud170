import unicodecsv

enrollments = []
f = open('../data/enrollments.csv', 'rb')
reader = unicodecsv.DictReader(f)

for row in reader:
    enrollments.append(row)

f.close()

size = len(enrollments)

for i in range(size):
    print enrollments[i]
