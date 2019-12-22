def last_day_of_month(month, year):
    month_30day = [4,6,9,11]
    if month == 2:
        last_day = 29 if is_leap_year(year) else 28
    elif month in month_30day:
        last_day=30
    else:
        last_day=31
    return last_day

def next_day(year, month, date):
    if isValidDate(year, month, date):
        next_date = date
        next_month = month
        next_year = year

        if(date == last_day_of_month(month,year) and month == 12):
            next_month = 1
            next_date = 1
            next_year += 1
        elif(date == last_day_of_month(month,year)):
            next_month += 1
            next_date = 1
        else:
            next_date += 1
        return next_year, next_month, next_date
    else:
        print("Please pass valid date")

def is_leap_year(year):
    if year%4==0:
		if year%100==0:
			if year%400==0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False

def isValidDate(year, month,date):
    if(month<=12):
        if date <= last_day_of_month(month, year):
            return True
    return False

def date1BeforeDate2(year1, month1, date1, year2, month2, date2):
    if(year1>year2) or (year1==year2 and month1>month2) or (year1==year2 and month1==month2 and date1>=date2):
        return False
    else:
        return True


def daysBetweenDates(year1, month1, date1, year2, month2, date2):
    if isValidDate(year1, month1, date1) and isValidDate(year2, month2, date2) and date1BeforeDate2(year1, month1, date1, year2, month2, date2):
        count = 0
        while date1BeforeDate2(year1, month1, date1, year2, month2, date2):
            count += 1
            year1,month1,date1 = next_day(year1, month1, date1)

        return count
    else:
        print("Please enter valid dates")


def test():
    test_cases = [((2012,9,30,2012,10,30),30),
                ((2012,1,1,2013,1,1),366),
                  ((2012,9,1,2012,9,4),3)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "failed")
        else:
            print ("Test case passed!")

test()



