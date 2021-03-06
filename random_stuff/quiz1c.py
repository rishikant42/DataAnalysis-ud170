import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv('../data/enrollments.csv')
daily_engagement = read_csv('../data/daily_engagement.csv')
project_submissions = read_csv('../data/project_submissions.csv')
        
print len(enrollments)
print enrollments[0] 
print daily_engagement[0]
print project_submissions[0]
