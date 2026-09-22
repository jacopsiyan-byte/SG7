try:
    grade = int(input("Enter your grade level: "))

    if grade == 7 or grade == 8 or grade == 9 or grade == 10 or grade == 11 or grade == 12:
        print("Valid grade level.")
    else:
        print("Invalid grade level.")

except ValueError:
    print("Invalid input. Please enter a whole number.")



