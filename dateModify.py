def dateMode():
    currentDate = str(input("Enter Current Date: "))
    date = currentDate [3:5]
    intDate = int(date)
    newDate = intDate + 1
    strDate = str(newDate)
    listCurrentDate = list(currentDate)
    listCurrentDate[3:5] = strDate
    currentDate = "".join(listCurrentDate)
    return currentDate


print(dateMode())