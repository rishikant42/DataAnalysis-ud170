import unicodecsv

engagement_filename = '../data/daily_engagement.csv'
submissions_filename = '../data/project_submissions.csv'
    
daily_engagement = []     # Replace this with your code
project_submissions = []  # Replace this with your code

with open(engagement_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    
    for row in reader:
        daily_engagement.append(row)
        
with open(submissions_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    
    for row in reader:
        project_submissions.append(row)

print daily_engagement[0]
print project_submissions[0]
