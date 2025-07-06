def sufix(n):
    if n==1:
        return "st"
    elif n==2:
        return "nd"
    elif n ==3:
        return "rd"
    else:
        return "th"
def Student_Names(No_of_students):
    Student_name = []
    for count in range (1,No_of_students+1):
        get_sufix= sufix(count)
        Each_Stuent_name = input(f"Enter the {count}{get_sufix} Student Name: ")
        Student_name.append(Each_Stuent_name)
        count+=1
    return Student_name