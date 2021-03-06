# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeapYear(year):
    # Takes the year as an input and checks if the input year is a leap year using the algorithm 
    # from http://en.wikipedia.org/wiki/Leap_year#Algorithm. Returns 'True' or 'False':
    if year/4.0 > year/4:
        return False
    else:
        if year/100.0 > year/100:
            return True
        else:
            if year/400.0 > year/400:
                return False
            else:
                return True
    
def daysOfMonthCorrect(y):
    # Takes the year as an input and changes the number of days in February if this is a leap year.
    # Returns the variable that refers to the list containing the correct days of months: 
    if isLeapYear(y): 
        correct_daysOfMonths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        correct_daysOfMonths = daysOfMonths
    return correct_daysOfMonths

def days_birth_year(y,m,d):
    # Takes the date in a form of 3 integers (year, month, day) as an input and counts the number of days
    # from the date to the end of the year. Good for counting the days lived in the year of birth. 
    # Returns the integer:
    if m == 12:
        # if the month of birth is December, then the result is simply days in December 
        # minus birthday:
        return 31 - d
    else:
        # if the month of birth is other than December, then it counts the number of days
        # in the frame 'the month of birth > the end of the year' and reduces the 
        # result by the number of days from the beginning of the month of birth to the birthday: 
        actual_daysOfMonths = daysOfMonthCorrect(y)
        frame = actual_daysOfMonths[m-1:]
        result = 0
        for e in frame:
            result += e
        result = result - d
        return result
        
def days_current_year(y,m,d):
    # Takes the date in a form of 3 integers (year, month, day) as an input and counts the number of days
    # from the beginning of the year to the input date. Good for counting the days lived in the current year. 
    # Returns the integer:
    if m == 1:
        # if the current month is January, the the result is equal to current day:
        return d
    else:
        # if the current month is other than January, then it counts the number of days
        # in the frame 'the beginning of the year > the month before current' and increases the 
        # result by the number of days from the beginning of the current month to the current day:
        actual_daysOfMonths = daysOfMonthCorrect(y)
        frame = actual_daysOfMonths[:m-1]
        result = 0
        for e in frame:
            result += e
        result += d
        return result

def isWrongDate(y1, m1, d1, y2, m2, d2):
    # Takes two dates in a form of 6 integers (year1, month1, day1, year2, month2, day2) as an input and checks 
    # if the input dates are wrong, i.e. if the second date is 'older' than the first one.
    # Returns 'True' or 'False':
    if y2 < y1:
        return True
    if y2 == y1:
        if m2 < m1:
            return True
        if m2 == m1:
            if d2 < d1:
                return True
    else:
        return False


def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    # Takes two dates in a form of 6 integers (year1, month1, day1, year2, month2, day2) as an input and counts 
    # the number of days between these dates using the functions defined above. Returns 'None' if the input dates
    # are wrong, and the integer equal to the number of days between the correct dates:
    if isWrongDate(y1, m1, d1, y2, m2, d2):
        print 'The input dates are seemingly wrong!'
        return None
    else:
        if y2 == y1:
            # in this case, it is enough to substract the days before the birthday from all of the days in the current year:  
            days = days_current_year(y2,m2,d2) - days_current_year(y1,m1,d1)
        if y2 - y1 == 1:
            # in this case, it is enough to add the days lived in the birth year to the days lived in the current year:
            days = days_birth_year(y1,m1,d1) + days_current_year(y2,m2,d2)
        if y2 - y1 > 1:
            # the first stage is to count the number of days for the 'complete' years, i.e. 
            # all the years except for the year of birth and the current year. The variable
            # 'days' is being increased by 365 or 366 days depending on the leap-year-check:  
            days = 0
            year_check = y1 + 1
            while year_check < y2:
                if isLeapYear(year_check):
                    days += 366
                else:
                    days += 365
                year_check += 1
            # the next stage is to add days from the 'incomplete' years, i.e. days lived in 
            # the year of birth and the current year:
            days += days_birth_year(y1,m1,d1) + days_current_year(y2,m2,d2)
        return days

print daysBetweenDates(1989,9,10,2018,3,4)