from StudentNames import Student_Names
def Student_info(No_of_students,No_of_subjects,Total_test_marks):
    Total_marks=0
    M={} 
    Count=0 
    for Student in Student_Names(No_of_students):
        Sub ={}
        for _ in range(No_of_subjects):
            Sub_marks = input(f"Enter the subject and marks with comma of {Student}: ")
            if "," not in Sub_marks:
                print("Invalid input........")
                return 
            subject,marks = Sub_marks.split(",")
            Sub[subject] = int(marks)
        for _ ,mark in Sub.items():
            Total_marks=Total_marks+int(mark)
        Per= (Total_marks/int(Total_test_marks))*100
        print(f"The percentage of {Student} is {Per}")
        M[Student]= Total_marks
        Total_marks=0
        Count+=1
    return M