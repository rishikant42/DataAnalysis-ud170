import unicodecsv

enrollments = []
f = open('../data/enrollments.csv', 'rb')
reader = unicodecsv.DictReader(f)

for row in reader:
    print row

f.close()
