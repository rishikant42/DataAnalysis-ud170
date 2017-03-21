import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv('../data/enrollments.csv')
daily_engagement = read_csv('../data/daily_engagement.csv')
project_submissions = read_csv('../data/project_submissions.csv')
        
def get_unique_students(data):
    unique_students = set()
    for data_point in data:
        unique_students.add(data_point['account_key'])
    return unique_students

unique_enrolled_students = get_unique_students(enrollments)
print len(unique_enrolled_students)

for engagement_record in daily_engagement:
    engagement_record['account_key'] = engagement_record['acct']
    del(engagement_record['acct'])
        
unique_engagement_students = get_unique_students(daily_engagement)
print len(unique_engagement_students)

unique_project_submitters = get_unique_students(project_submissions)
print len(unique_project_submitters )
