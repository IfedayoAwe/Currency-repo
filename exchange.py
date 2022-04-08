def exchange():
    currency = (input("Enter Currency: "))
    Amount = float(input("Enter Amount: "))
    exchangeRate = float(input("Enter Excchange Rate of currency to 1 Naira: "))
    newCurrency = Amount / exchangeRate
    return newCurrency
    

naira = exchange()
print(naira)