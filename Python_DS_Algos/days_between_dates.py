def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates and returns that value.
    """

    # day of month invalid - eg day is 29 for Feb when no leap year
    if not day_of_month_valid(year1, month1, day1) or \
        not day_of_month_valid(year2, month2, day2):
            return None

    # start must be before or same as end date:
    if not date_is_before(year1, month1, day1, year2, month2, day2):
        if not (year1 == year2 and month1 == month2 and day1 == day2):
            print("Start date must be less than or equal to end date")
            return None
    
    # count up the # of days
    num_days = 0
    while date_is_before(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = get_next_day(year1, month1, day1)
        num_days += 1
    return num_days

def day_of_month_valid(year, month, day):
    if day > last_day_in_month(month, year):
        print("Day value from input is invalid for {} - {} - {}"
                                        .format(month, day, year))
        return False
    return True


def get_next_day(year, month, day):
    if day == last_day_in_month(month, year):
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
    else:
        return year, month, day + 1

def last_day_in_month(month, year):
    # 30 days
    if month in (4, 6, 9, 11):
        return 30
    # 31 days
    elif month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    # Feb
    elif is_leap(year):
        return 29
    else:
        return 28

def is_leap(year):
    if ((year % 4 == 0) and (year % 100 != 0)) \
        or (year % 400 == 0):
        return True
    else:
        return False

def date_is_before(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    # check months if years the same
    elif year1 == year2:
        if month1 < month2:
            return True
        # check days if year and month the same
        else:
            if day1 < day2:
                return True
    return False


def testDaysBetweenDates():
    
    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30, 
                              2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30, 
                              2018, 1,  1)  == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                              2013, 6, 29)  == 365)

    # test 2020 leap year
    assert(daysBetweenDates(2020, 2, 1,
                              2020, 3, 1) == 29)

    # test invalid day for a given month - 2019 not leap year
    assert(daysBetweenDates(2019, 2, 29,
                              2020, 3, 1) == None)

    # test start date later than end date
    assert(daysBetweenDates(2021, 2, 1,
                              2020, 3, 1) == None)

testDaysBetweenDates()

'''
pseudo-code
daysBetweenDates(year1, month1, day1, year2, month2, day2):
    num_days = 0
    while current_date < end_date:
        current_date = get_next_day(current_date)
        num_days += 1

Step 1:
- Assume all inputs valid for now
- Will initially assume all months are 30 days
- Define a helper function to see if date1 < date2
- Return a count that increments for # days in between 

Step 2:
- Add in some complexity now
- Add the actual number of days for each month
- Return count

Step 3:
- Check if leap year, and account for that

Step 4:
- Check for valid dates - make sure date2 >= date1, no Feb 29th for non leap years
'''