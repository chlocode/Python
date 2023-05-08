from datetime import date, datetime
"""
my_string = str(input('Enter date(yyyy-mm-dd): '))
my_date = datetime.strptime(my_string, "%Y-%m-%d")
 
age=datetime.now()-my_date
#print(my_date)
print({age})
"""
def main():
    dob=input("date of birth in YYYY-MM-DD:")
    my_date = datetime.strptime(dob, "%Y-%m-%d")
    AGE=age(my_date)
    print({AGE})

def age(birthdate):
    today = date.today()
    age=today.year-birthdate.year-((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

main()

#print(age(date(my_date)))