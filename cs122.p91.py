def distinct_majors(filename):
    '''
    
    '''
    majors = {}
    with open('majors-s23-short.txt', 'r') as file:
        lines = file.readlines()#skips first line
        for line in lines:
            major = line.strip()
            if major not in majors:
                majors[major] = 1
            else:
                majors[major] += 1
        return majors
    

def post_process(majors):
    if 'CIS' in majors and 'CS' in majors:
        combined_value = majors['CIS'] + majors['CS']
        majors['combined CS'] = combined_value
        del majors['CIS']
        del majors ['CS']

    return majors

def report_majors(majors):
    sorted_majors = sorted(majors.items())
    total_students = sum(majors.values())

    print("Distinct Majors:")
    for major, count in sorted_majors:
        print(f"{major}: {count} student(s)")
    print(f"Total number of distinct majors: {len(majors)}")
    print(f"Total number of students in CS 122 this term: {total_students}")

def main():
    filename = 'majors-s23-short.txt'
    majors = distinct_majors(filename)
    majors = post_process(majors)
    report_majors(majors)

#main()

