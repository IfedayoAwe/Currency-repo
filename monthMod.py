def dateFunction():
    print("1.dd-mm-yyyy \n2.yyyy-mm-dd \n3.mm-dd-yyyy" )
    dateFormat = int(input("Enter Date Format: "))
    if (dateFormat == 1):
        print(dayMonthYear())
    elif (dateFormat == 2):
        print(yearMonthDay())
    else:
        print(monthDayYear()) 

def dayMonthYear():
    currentDate = str(input("Enter Current Date: "))
    intMonth = int(currentDate [3:5])
    intYear = int(currentDate [6:10])
    listCurrentDate = list(currentDate)
    newMonth = intMonth + 1
    if (newMonth == 13):
        newMonth = 1
        strYear = str(intYear + 1)
        listCurrentDate[6:10] = strYear
        currentDate = "".join(listCurrentDate)
    doubleDigitMonth = '%02d' % newMonth
    strMonth = str(doubleDigitMonth)
    listCurrentDate[3:5] = strMonth
    currentDate = "".join(listCurrentDate)
    return currentDate


def yearMonthDay():
    currentDate = str(input("Enter Current Date: "))
    intMonth = int(currentDate [5:7])
    intYear = int(currentDate [0:4])
    listCurrentDate = list(currentDate)
    newMonth = intMonth + 1
    if (newMonth == 13):
        newMonth = 1
        strYear = str(intYear + 1)
        listCurrentDate[0:4] = strYear
        currentDate = "".join(listCurrentDate)
    doubleDigitMonth = '%02d' % newMonth
    strMonth = str(doubleDigitMonth)
    listCurrentDate[5:7] = strMonth
    currentDate = "".join(listCurrentDate)
    return currentDate


def monthDayYear():
    currentDate = str(input("Enter Current Date: "))
    intMonth = int(currentDate [0:2])
    intYear = int(currentDate [6:10])
    listCurrentDate = list(currentDate)
    newMonth = intMonth + 1
    if (newMonth == 13):
        newMonth = 1
        strYear = str(intYear + 1)
        listCurrentDate[6:10] = strYear
        currentDate = "".join(listCurrentDate)
    doubleDigitMonth = '%02d' % newMonth
    strMonth = str(doubleDigitMonth)
    listCurrentDate[0:2] = strMonth
    currentDate = "".join(listCurrentDate)
    return currentDate

dateFunction()