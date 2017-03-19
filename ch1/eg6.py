import unicodecsv

from datetime import datetime as dt

def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')

def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

enrollments_filename = '../data/enrollments.csv'
engagement_filename = '../data/daily_engagement.csv'
submissions_filename = '../data/project_submissions.csv'

with open(enrollments_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)

    for enrollment in enrollments:
        enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
        enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
        enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
        enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
        enrollment['join_date'] = parse_date(enrollment['join_date'])

        
with open(engagement_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    daily_engagement = list(reader)

    for engagement_record in daily_engagement:
        engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
        engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
        engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
        engagement_record['total_minutes_visted'] = int(float(engagement_record['total_minutes_visited']))
        engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])
        
with open(submissions_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    project_submissions = list(reader)

    for submission in project_submissions:
        submission['completion_date'] = parse_date(submission['completion_date'])
        submission['creation_date'] = parse_date(submission['creation_date'])


print enrollments[0] 
print daily_engagement[0]
print project_submissions[0]
