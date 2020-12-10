# Assignment given by Tarun Kumar & Bahawal Baloch
# Developer: Zaid Ahmed Soomro
# Institute: MUET Jamshoro
# Department: Software Engineering (First Semester)
# Language: Python
# DSU-DSC Python Bootcamp 2020
# Date: 9/12/2020 Wednesday

list_of_records = []
marks_record = []

while True:
    roll_input = input("\nEnter roll no. of student: ")
    name_input = input("Enter name of student: ")
    age_input = input("Enter age of student: ")
    marks_input = input("Enter marks of student: ")
    # Fail if marks are less than 40
    pf_input = input("Pass or Fail: ")
    total = 100
    user_input = {
        'roll no': str(roll_input),
        'name': name_input.title(),
        'age': str(age_input),
        'marks': int(marks_input),
        'pass/fail': pf_input.upper()
    }
    list_of_records.append(user_input)
    marks_record.append(user_input['marks'])
    if len(list_of_records) > 4:
        for dics in list_of_records:
            print(end="\n")
            for k, v in dics.items():
                print(v, end=" ")
        print("\nMaximum marks in this test are " + str(max(marks_record)) + f" out of {total}.")
        print("\nMinimum marks in this test are " + str(min(marks_record)) + f" out of {total}.")
        print("\nAverage score in this test is " + str(sum(marks_record)/len(marks_record)) + f" out of {total}")
        break
    else:
        continue
