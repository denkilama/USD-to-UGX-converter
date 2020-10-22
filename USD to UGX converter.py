country_currency = int(input("Currency amount: "))
currency = input('USD or UGX: ')
if currency.upper() == "USD":
    converted = country_currency * 3600
    print(f"you have {converted}UGX")
else:
    converted = country_currency / 3600
    print(f"you have {converted}USD")
