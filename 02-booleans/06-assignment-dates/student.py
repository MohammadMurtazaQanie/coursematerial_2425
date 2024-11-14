# write your code here
def is_valid_month(month):
    if 1 <= month <= 12:
        return True
    else:
        return False
def is_leap_year(year):
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False

def has_30_days(month):
    if month in [4, 6, 9, 11]:
        return True
    else:
        return False

def has_31_days(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return True
    else:
        return False

def has_28_days(month, year):
    if month == 2 and not is_leap_year(year):
        return True
    else:
        return False

def has_29_days(month, year):
    if month == 2 and is_leap_year(year):
        return True
    else:
        return False

def is_valid_date(day, month, year):
    if not is_valid_month(month):
        return False

    if has_31_days(month):
        return 1 <= day <= 31
    elif has_30_days(month):
        return 1 <= day <= 30
    elif has_28_days(month, year):
        return 1 <= day <= 28
    elif has_29_days(month, year):
        return 1 <= day <= 29
    else:
        return False