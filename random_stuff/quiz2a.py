import unicodecsv

def count_lines(filename):
    inputFile = open(filename)
    readFile = unicodecsv.reader(inputFile)
    
    # Skip Header
    readFile.next()
    
    noOfLines = 0
    
    for x in readFile:
        noOfLines += 1
        
    return noOfLines

print count_lines("../data/daily_engagement.csv")
print count_lines("../data/enrollments.csv")
print count_lines("../data/project_submissions.csv")
