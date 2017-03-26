import unicodecsv

enrollments = []
with open('../data/enrollments.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)

    for row in reader:
        enrollments.append(row)

size = len(enrollments)

for i in range(size):
    print enrollments[i]
