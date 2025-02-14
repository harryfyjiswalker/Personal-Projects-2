def add_student(students: dict, name: str):
    students[name]=[]

def print_student(students:dict, name:str):
    if name in students:
        if len(students[name]) == 0:
            print(f"{name}:\n no completed courses")
        else:
            print(f"{name}:\n {len(students[name])} completed courses:")
            completed_courses = students[name]
            gradesum = 0
            for i in range(0, len(completed_courses)):
                gradesum += completed_courses[i][1]
                print(f"  {completed_courses[i][0]} {completed_courses[i][1]}")
            average_grade = gradesum/len(completed_courses)
            print(f" average grade {average_grade}")
                        
    else:
        print(f"{name}: no such person in the database")

def average_grade(students:dict, name:str):
    if name in students:
        if len(students[name]) == 0:
            print(f"{name}:\n no completed courses")
        else:
            completed_courses = students[name]
            gradesum = 0
            for i in range(0, len(completed_courses)):
                gradesum += completed_courses[i][1]
            average_grade = gradesum/len(completed_courses)
    return average_grade

def add_course(students:dict, name:str, course_grade_tuple:tuple):
    if course_grade_tuple[1] != 0:
        if course_grade_tuple[0] not in [course[0] for course in students[name]]:
            students[name].append(course_grade_tuple)
        else:
            for i, (course, grade) in enumerate(students[name]):
                if course == course_grade_tuple[0] and grade < course_grade_tuple[1]:
                    students[name][i] = course_grade_tuple 
                    break

def summary(students: dict):
    print(f"students {len(students)}")
    lengths = []
    averagegradelist = []
    for name in students:
        lengths.append(len(students[name]))
        averagegradelist.append(average_grade(students, name))
    index = lengths.index(max(lengths))
    index1 = averagegradelist.index(max(averagegradelist))
    mostcourses = list(students.keys())[index]
    topgrade = list(students.keys())[index1]
    print(f"most courses completed {max(lengths)} {mostcourses}")
    print(f"best average grade {max(averagegradelist)} {topgrade}")
    

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
