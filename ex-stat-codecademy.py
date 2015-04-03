__author__ = 'sereg'

#grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
#grades = [0, 2, 3, 0, 1, 5, 7, 8]
grades = [0, 1, 2]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total

def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    print average
    print scores
    variance = 0
    for e in scores:
        variance += abs(average - e) ** 2
        print variance
    return float(variance) / len(scores)
#print grades_variance(grades)
#doubles_by_3 = [z ** 2 for z in range(1,12) if z % 2 == 0]
#print(doubles_by_3)
def flip_bit(number,n):
    k = n - 1
    mask = (0b1 << k)
    print bin(mask)
    result = number ^ mask
    return bin(result)
print flip_bit(0b111,2)