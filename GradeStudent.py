# "A" - any grade 90-100, inclusive
# "B" - any grade 80-89, inclusive
# "C" - any grade 70-79, inclusive
# "D" - any grade 60-69, inclusive
# "F" - any grade <60


def get_grade(score):
    # Check the condition and return the grade
    if(score>=90 and score<100):
        return "A"
    elif(score>=80 and score<89):
        return "B"
    elif(score>=70 and score<79):
        return "C"
    elif(score>=60 and score<69):
        return "D"
    else:
        return "F"
    
# Testing the function
print("Grade for a score of 95 is :",get_grade(95)) # Output: A
print("Grade for a score of 95 is :",get_grade(85)) # Output: B
print("Grade for a score of 95 is :",get_grade(75)) # Output: C
print("Grade for a score of 95 is :",get_grade(65)) # Output: D
print("Grade for a score of 95 is :",get_grade(55)) # Output: F