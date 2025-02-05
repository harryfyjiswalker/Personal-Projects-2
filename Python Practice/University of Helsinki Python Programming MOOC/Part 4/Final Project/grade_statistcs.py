import math
import statistics

def inputs_from_user():
    marks = []
    while True:
        num = input("Exam points and exercises completed:")
        if num == "":
            break
        marks.append(num)
    return marks

def points(marks):
    exam_points = []
    exercises = []
    examandexercise = []
    for m in marks:
        for i in range(len(m)):
            if m[i] == " ":
                exam_points.append(m[0:i])
                exercises.append(m[(i+1):len(m)])
    for i in range(len(exam_points)):
        sum = float(exam_points[i])+math.floor(0.1*float(exercises[i]))
        examandexercise.append(sum)
    return exam_points, exercises, examandexercise

def grade(exam_points, examandexercise):
    grade = []
    for i in range(len(exam_points)):
        if float(exam_points[i]) < 10:
            grade.append(0)
        elif float(exam_points[i]) >= 10:
            #for i in range(len(exam_points)):
            if 0 < float(examandexercise[i]) <= 14:
                grade.append(0)
            elif 15 <= float(examandexercise[i]) <= 17:
                grade.append(1)
            elif 18 <= float(examandexercise[i]) <= 20:
                grade.append(2)
            elif 21 <= float(examandexercise[i]) <= 23:
                grade.append(3)
            elif 24 <= float(examandexercise[i]) <= 27:
                grade.append(4)
            elif 28 <= float(examandexercise[i]) <= 30:
                    grade.append(5)
    numberfailed = grade.count(0)
    pointsaverage = statistics.mean(examandexercise)
    passpercentage = ((len(grade)-numberfailed)/len(grade))*100
    print("Statistics:")
    #print(exam_points)
    #print(examandexercise)
    #print(grade)
    print(f"Points average: {round(pointsaverage,1)}")
    print(f"Pass percentage: {round(passpercentage,1)}")
    gradedist = print(f"Grade distribution:\n5: {'*'* grade.count(5)}\n4: {'*'* grade.count(4)}\n3: {'*'* grade.count(3)}\n2: {'*'* grade.count(2)}\n1: {'*'* grade.count(1)}\n0: {'*'* grade.count(0)}")

def main():
    marks = inputs_from_user()
    exam_points, exercises, examandexercise = points(marks)
    grade(exam_points, examandexercise)

main()
