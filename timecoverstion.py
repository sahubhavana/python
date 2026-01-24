def dayOfProgrammer(year):
     # Special case: year 1918
    if year == 1918:
        return "26.09.1918"

    # Julian calendar
    if year < 1918:
        leap = (year % 4 == 0)

    # Gregorian calendar
    else:
        leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

    # Feb days
    feb_days = 29 if leap else 28

    # Jan to Aug total days
    days_till_aug = 31 + feb_days + 31 + 30 + 31 + 30 + 31 + 31

    # Day of September
    day = 256 - days_till_aug

    return  "{:02d}.09.{}".format(day, year)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
