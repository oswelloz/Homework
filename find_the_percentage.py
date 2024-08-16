if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # take the student marks and iterate to check individual student's marks
    # check it the student's name matches the query name
    # if True add all the student marks divided by number of marks given
    #return the average in a float format to the nearest to decimal places
    
    for student_nume, marks in student_marks.items(): 
        if query_name == student_nume: 
            average = (sum(marks)/len(marks))
            print(average)
        
        