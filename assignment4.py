# research on python function , both with parameters and without

def is_leap(year):
    """
    Determines if a given year is a leap year.

    Args:
        year: The year to check (integer).

    Returns:
        True if the year is a leap year, False otherwise.
    """
    # The order of these checks is important for correctly
    # handling years divisible by 100 and 400.
    if (year % 400) == 0:
        return True
    elif (year % 100) == 0:
        return False
    elif (year % 4) == 0:
        return True
    else:
        return False

# --- Example Usage ---
# Test cases
year1 = 2000 # Should be True (divisible by 400)
year2 = 1900 # Should be False (divisible by 100 but not 400)
year3 = 2024 # Should be True (divisible by 4)
year4 = 2023 # Should be False (not divisible by 4)

print(f"{year1} is a leap year: {is_leap(year1)}")
print(f"{year2} is a leap year: {is_leap(year2)}")
print(f"{year3} is a leap year: {is_leap(year3)}")
print(f"{year4} is a leap year: {is_leap(year4)}")

# You can also get user input
# try:
#     user_year = int(input("Enter a year to check: "))
#     if is_leap(user_year):
#         print(f"{user_year} is a leap year.")
#     else:
#         print(f"{user_year} is not a leap year.")
# except ValueError:
#     print("Invalid input. Please enter a numerical year.")
print("================")

# python functions
# calling a function
def my_function():
  print("Hello from a function")

my_function()
my_function()
my_function()

# passing information to python functions.

def greet(name):
    print("Hi",name)
greet("john")