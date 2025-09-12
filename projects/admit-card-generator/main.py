import datetime

def admit_card_generator():
    print("GIAIC Admit Card Generator")
    print("---------------------------")

    student_name = input("Enter student full name: ").strip().title()
    father_name = input("Enter father's name: ").strip().title()
    roll_number = int(input("Enter roll number: "))
    batch_number = input("Enter batch number: ").strip().title()
    course_name = input("Enter course name: ").strip().title()
    campus = input("Enter campus location: ").strip().title()
    issue_date = datetime.datetime.now()

    print(f"""\n===== GIAIC - Student Admit Card =====
Name:           {student_name} {father_name}
Roll No:        {roll_number}
Batch:          Batch-{batch_number}
Course:         {course_name}
Campus:         {campus}
Issued Date:    {issue_date.strftime("%x")}
======================================""")
    
admit_card_generator()