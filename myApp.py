bank = 400
covidMoney = 200

totalBank = covidMoney*12 + 400

currency = "${:,.2f}".format(totalBank)


print(currency)




