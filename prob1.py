try:
    age = int(input("Enter your age: "))

    if age >= 12 and age <= 18:
        print("Valid age.")
    else:
        print("Invalid age. Age must be from 12 to 18.")

except ValueError:
    print("Invalid input. Please enter a whole number.")