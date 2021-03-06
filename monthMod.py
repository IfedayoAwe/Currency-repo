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

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    def __len__(self):
        return len(self.cards)
    def __getitem__(self, position):
        return self.cards[position]
        

class Employee:

    def __init__(self, first, last, age, email, rank):
        self.first = first
        self.last = last
        self.age = age
        self.email = email
        self.rank = rank

    def salary(self):
        return self.rank * 1000

def foo(num1, num2):
    foo = num1 * num2
    return foo
