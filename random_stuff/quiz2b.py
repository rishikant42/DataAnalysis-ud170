import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv('../data/enrollments.csv')
daily_engagement = read_csv('../data/daily_engagement.csv')
project_submissions = read_csv('../data/project_submissions.csv')
        
print len(daily_engagement)
print len(enrollments)
print len(project_submissions)

print "============================================"

unique_enrolled_students = set()
for enrollment in enrollments:
    unique_enrolled_students.add(enrollment['account_key'])

print len(unique_enrolled_students)

unique_engagement_students = set()
for engagement_record in daily_engagement:
    unique_engagement_students.add(engagement_record['acct'])

print len(unique_engagement_students)

unique_project_submitters = set()
for submission in project_submissions:
    unique_project_submitters.add(submission['account_key'])

print len(unique_project_submitters)
