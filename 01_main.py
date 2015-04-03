__author__ = 'sereg'
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
students = [lloyd,alice,tyler]
#for e in students:
#    print e["name"]
#    print e["homework"]
#    print e["quizzes"]
#    print e["tests"]
num = [100.0, 92.0, 98.0, 100.0]
def average(numbers):
    total = sum(numbers)
    total = total / len(numbers)
    return total
#print average(num)
#print students[1]["name"]
def get_average(student):
    homework = 0.1 * average(student["homework"])
    quizzes = 0.3 * average(student["quizzes"])
    tests = 0.6 * average(student["tests"])
    m = homework + quizzes + tests
    return m
def get_letter_grade(score):
    if get_average(score) > int(90):
        return "A"
    elif get_average(score) > int(80):
        return "B"
    elif get_average(score) > 70:
        return "C"
    elif get_average(score) > 60:
        return "D"
    else:
        return "once again A"
#for e in students:
#    print get_average(e)
#    print get_letter_grade(e)
def get_class_average(students):
    results = []
    for each in students:
        k = get_average(each)
        results.append(k)
    return average(results)
print get_class_average(students)