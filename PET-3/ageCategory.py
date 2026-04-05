# Write a Python program to calculate the final train ticket price based on:

# gender (male/female)
# age
# original fare

# Check only the age to decide whether the person is a senior citizen (age ≥ 60) or normal citizen, then apply:
# Senior Citizen (age ≥ 60):
# Male → 70% of fare
# Female → 50% of fare

# Normal Citizen (age < 60):
# Female → 70% of fare
# Male → 100% of fare

# Print the final ticket price.


def calculate_fare(gender, age, original_fare):
    ## write your code here
    fare = 0
    if gender == "Male" and age >= 60:
        fare = (original_fare * 70) / 100
    elif gender == "Female" and age >= 60:
        fare = (original_fare * 50) / 100
    elif gender == "Female" and age < 60:
        fare = (original_fare * 70) / 100
    elif gender == "Male" and age < 60:
        fare = original_fare
    print(fare)


calculate_fare("Female", 60, 1000)  # Case 1
calculate_fare("Male", 60, 1000)  # Case 2
calculate_fare("Female", 25, 200)  # Case 3
calculate_fare("Male", 18, 500)  # Case 4
calculate_fare("Female", 85, 120)  # Case 5
