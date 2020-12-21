# getting input from the user and assigning it to user
def main():
    
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kg: "))

    # the formula for calculating bmi

    bmi = weight/(height**2) 
    # ** is the power of operator i.e height*height in this case

    print("Your BMI is: {0} and you are: ".format(bmi), end='')

    #conditions
    if ( bmi < 16):
        print("severely underweight")
        main()

    elif ( bmi >= 16 and bmi < 18.5):
        print("underweight")
        main()

    elif ( bmi >= 18.5 and bmi < 25):
        print("Healthy")
        main()
        
    elif ( bmi >= 25 and bmi < 30):
        print("overweight")
        main()

    elif ( bmi >=30):
        print("severely overweight")
        main()
main()