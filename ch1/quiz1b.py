import unicodecsv

enrollments_filename = '../data/enrollments.csv'
engagement_filename = '../data/daily_engagement.csv'
submissions_filename = '../data/project_submissions.csv'

with open(enrollments_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)
        
with open(engagement_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    daily_engagement = list(reader)
        
with open(submissions_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    project_submissions = list(reader)

print enrollments[0] 
print daily_engagement[0]
print project_submissions[0]
