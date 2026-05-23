import os
import sys
import math
import json
import random
import datetime
import pathlib
import subprocess
import csv
import re
import collections


# This file intentionally contains several beginner-level quality issues.
# It is used to test the AI Code Review Agent.


def process_student_data(students):
    print("Starting student processing")
    total = 0
    passed = 0
    failed = 0
    excellent = 0
    weak = 0
    names = []
    results = []
    for student in students:
        names.append(student["name"])
        grade = student["grade"]
        total = total + grade
        if grade >= 90:
            excellent = excellent + 1
            results.append(student["name"] + " excellent")
            if student["attendance"] > 80:
                print(student["name"] + " is excellent and active")
            else:
                print(student["name"] + " is excellent but attendance is low")
        elif grade >= 50:
            passed = passed + 1
            results.append(student["name"] + " passed")
            if student["attendance"] > 70:
                print(student["name"] + " passed with good attendance")
            else:
                print(student["name"] + " passed but attendance is weak")
        else:
            failed = failed + 1
            weak = weak + 1
            results.append(student["name"] + " failed")
            if student["attendance"] < 50:
                print(student["name"] + " failed and attendance is very low")
            else:
                print(student["name"] + " failed but attendance is acceptable")
    average = total / len(students)
    print("Average grade:", average)
    print("Passed:", passed)
    print("Failed:", failed)
    print("Excellent:", excellent)
    print("Weak:", weak)
    print("Names:", names)
    print("Results:", results)
    return results


students = [
    {"name": "Alice", "grade": 92, "attendance": 85},
    {"name": "Bob", "grade": 45, "attendance": 40},
    {"name": "Charlie", "grade": 67, "attendance": 75},
]

process_student_data(students)
