import unicodecsv

with open('../data/enrollments.csv', 'rb') as f:
    reader = list(unicodecsv.DictReader(f))
    enrollments = list(reader)

size = len(enrollments)

for i in range(size):
    print enrollments[i]
