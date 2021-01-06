# age_converter.py

first_name = "Gerardo"

age_years = 26

age_secs = age_years * 60 * 60 * 24 *365

print(f"Hello, my name is {first_name}.")

print(f"I am {age_years} years old", end=", ")

print(f"which is {age_secs:,} seconds.")