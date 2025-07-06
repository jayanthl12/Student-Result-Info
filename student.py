from studentinfo import Student_info
No_of_students = int(input("Eter the No of students: "))
No_of_subjects = int(input("Enter the No of Subjects: "))
Total_test_marks = input("Enter the Total test marks of exam: ")
for key,value in Student_info(No_of_students,No_of_subjects,Total_test_marks).items():
    print(f" {key}: {value}")