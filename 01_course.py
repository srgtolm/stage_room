__author__ = 'sereg'

def date(month, day):
    """
    Given numbers month and day, returns a string of the form '2/12',
    with the month followed by the day.
    """
    return str(month) + "/" + str(day)

print date(2, 12)

def number_of_i(word):
    """Returns the number of lower-case i's in the word."""
    return word.count("i")

print number_of_i("missisipi")

#print float("5 five")
#print int("five")
print float("5")
print float("5.4")