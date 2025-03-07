def Calc_stud():
    name = input("please enter name of student:")
    stud_mark = {} #creating a dictionary to store subject name and marks
    for i in range(1,6):
        stud_marks= input(f"Enter subject {i} Name:")
        scores= int(input(f"Enter marks for {stud_marks}:"))
        stud_mark[stud_marks] = scores
    
    total_marks=sum(stud_mark.values())
    print("Total marks of student:", total_marks)
    total_possible_marks= 500 #for the 5 subjects
    stud_percentage=(total_marks/total_possible_marks)*100 
    print("student percentage:",stud_percentage)
    if stud_percentage<30:
        print("GRADE:E")
    elif stud_percentage>30 and stud_percentage<50:
        print("GRADE:D") 
    elif stud_percentage>30 and stud_percentage<70:
        print("GRADE:B") 

    elif stud_percentage>70:
        print("GRADE:A") 

Calc_stud()
    