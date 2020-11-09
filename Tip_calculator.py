print ("Tips calculator")

value1 = input ("Total number of shifts = ")
value1_int = int(value1)

value2 = input ("Tips per shift =")
value2_flt = float(value2)

tips_owed = (value1_int * value2_flt)
currency = "€{:,.2f}".format(tips_owed)
print (currency)