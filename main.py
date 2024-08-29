from datetime import date , time  , datetime

today = date.today()
ct = datetime.now()
print("Todays date is: ", today)
print("The current time is: ", ct)
print("The current year is: ", date.today().year)
print("The current month is: ", date.today().month)
print("Todays Date is: ", date.today().day)