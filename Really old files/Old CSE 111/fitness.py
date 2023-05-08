from datetime import datetime,date
def main():
#ask user to enter four values
    gender=input("Please enter your gender (m or f):")
    
    dob=input("Please enter your birthdate (YYYY-MM-DD):")
    
    user_date = datetime.strptime(dob, "%Y-%m-%d")
    
    weight=float(input("Please enter your weight in pounds:"))
   
    height=float(input("Please enter your height in inches:"))

    BMI=bmi(weight_to_pounds(weight), inches_to_centimeters(height))

    AGE=age(user_date)

    BMR=bmr(gender,weight_to_pounds(weight), inches_to_centimeters(height),AGE)

    print(f"Age (years) : {AGE}")
    print (f"Weight (Kg) : {weight_to_pounds(weight):.2f}")
    print(f"Height (cm) : {inches_to_centimeters(height):.1f}")
    #print(f"{inches_to_centimeters(height)}")
    print(f"Body mass index: {BMI:.1f}")
    print(f"Basal metabolic rate (kcal/day) : {BMR:.0f}")

def weight_to_pounds(weight_in_pounds):
    conversion=weight_in_pounds*0.45359237
    return conversion


def inches_to_centimeters(height_in_inches):
    centimeters=height_in_inches*2.54
    return centimeters

def bmi( weight, height):
    calculation=(10000*weight)/height**2
    return calculation


def bmr(gender,weight,height,AGE):
     if gender=="m":
        mass_ratio=88.362 +(13.397*weight) +(4.799*height)-(5.677*AGE)
     else:
        mass_ratio=447.593 + (9.247*weight) + (3.098 *height) -(4.330*AGE)
   
     return mass_ratio

def age(birthdate):
    today = date.today()
    age=today.year-birthdate.year-((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

main()