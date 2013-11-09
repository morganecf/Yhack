import json
import pandas as pd
data = pd.read_csv("course.csv")
courses = data.Course
courseNames = data.CourseName

for course, courseName in zip(courses,courseNames):

    course = Course(code=course, short_name=CourseName)
    course.save()