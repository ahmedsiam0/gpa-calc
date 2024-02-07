#! /bin/python3

import json

data = {}

with open("grades.json", 'r', encoding="utf-8") as data_file:
    data = json.load(data_file)

grades_mult_credits = 0.0
total_credits = 0.0

for course_name, course_grades in data.items():
    grades_mult_credits += course_grades[0] * course_grades[1]
    total_credits += course_grades[0]

gpa = grades_mult_credits / total_credits

print(f"Your GPA = {gpa}")
