'''
6_03_MultipleExpressions.py
'''

score = input("input your score: ")

if 90 <= int(score):
    grade = "A"    
elif 80 <= int(score) < 90:
    grade = "B"
elif 70 <= int(score) < 80:
    grade = "C"
elif 60 <= int(score) < 70:
    grade = "D"
else:
    grade = "F"

print("Your grade is " + grade)
