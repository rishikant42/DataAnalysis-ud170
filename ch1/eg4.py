import unicodecsv

with open('../data/enrollments.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)

    for row in reader:
        print row

f.close()
