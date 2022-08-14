import os
def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i]<38:
            continue
        else:
            val=grades[i]
            rem=val%5
            if rem==3:
                grades[i]=val+2
            elif rem==4:
                grades[i]=val+1
            else:
                continue
    return grades   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
