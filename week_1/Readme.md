# Instructors: Tarun Kumar & Bahawal Baloch
# Developer: Zaid Ahmed Soomro
# Institute: MUET Jamshoro
# Department: Software Engineering (First Semester)
# Language: Python
# DSU-DSC Python Bootcamp 2020
# Date: 9/12/2020 Wednesday

# Assignment no. 1 (Printing name in digonal)
    
    1) At first I have defined a function named foo().
    2) Then I created a list called name with each letter of a name separated with spaces so that I can print it in a digonal.
    3) Then I created a for loop:
            i) In this for loop I created a variable named 'i', 
            ii) That i named variable stored each letter of name from name list separately,
            iii) Then I used print() for printing it.
            iv) Then the loop repeated it self four times (length of name).
    4) Then the foo() function was called.       
    5) This program follows all PEP 8 rules.

# Assignment no. 2 (Test Record)
    1) First I created two different lists, namely list_of_records and marks_record.
    2) Then I created a while loop, here's what it contains:
            i) I created six variables inside the while loop which took output from user.
                Names and uses of input variables:
                    i) roll_input = It takes Roll number of student.
                    ii) name_input = It takes name of student.
                    iii) age_input = It takes age of student.
                    iv) marks_input = It takes marks of student.
                    v) pf_input = It asks that is the student pass or fail. If the marks are less than forty then you have to declare that student fail.
                    vi) Total = It stores total marks of test. It does'nt take user input.
            ii) Then I created a dictionary named user_input which stores student's data given by user.
            iii) Then all the data is sent (copy) to the major list which stores all dictionaries (list_of_records).
            iv) Then the marks stored in the dictionary (user_input) are sent (copy) to the list called marks_record.         
            v) Then I created a condition using if statement. Explained below:
                i) The major reason for creating this condition is to end the loop as the desired number of user input is took from the user.
                ii) I set the condition that if the length of the list_of_records reaches 5 (As instructed that minimum 5 inputs are required), run the following command:
                iii) I created a for loop which creates a variable dics and that variable stores items in list_of_records separately.
                iv) Then a new line is printed after every dictionary using print().
                v) Then I created a for loop again which stores keys and values from dics in nascent variables k and v respectively.
                vi) Then the value of each key from dics using print(). A space is added between each printed value using end=" ".
                vii) Then thee are three print statements which calculate and print max marks, min marks and avg marks respectively.
                viii) Now if that condition (if) becomes true, then the while loop will be terminated using break, otherwise it will repeat itself (using continue, instructed in else condition) untill if statement becomes true.
    3) This program follows all PEP 8 rules.
    
    NOTE: Keypoint that I learnt in this assignment was "How To Handle DATA".

# Assignment no. 3 (Song Lyrics Program)
    1) First the built in time module is imported.
    2) Then a function named foo() which contains parameter called take_input is defined.
        i) Then a variable called lyrics is defined which will break parameter string into parts after every comma (, ) and will store those parts in a list.
        ii) Then I created a for loop which defines a new variable called line and stores each item separately from list created in lyrics.
        iii) Then each line is printed from new line with a tab using print().
        iv) Then a delay of 1 second is occured using time.sleep().
        v) After that, that for loop repeats it self until items in the list end.
    3) Then the foo() function is called with default parameter (Twinkle Twinkle Little Star poem).
    4) This program follows all PEP 8 rules.
    
    NOTE: Key point that I learnt from this assignment was time.sleep().
    
