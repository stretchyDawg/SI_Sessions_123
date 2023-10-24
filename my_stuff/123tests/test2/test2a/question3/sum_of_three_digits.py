"""
Part A: Create a sum_of_digits function below that returns the sum of the digits
in any three digit number.

Part B: Create a main function that prompts the user to enter a three digit
number.  Call your sum_of_digits function from Part A and then output the sum
of the digits.

Examples - your output should match exactly
  Enter a three digit number: 123
  The sum of the digits are:  6

  Enter a three digit number: 999
  The sum of the digits are:  27

  Enter a three digit number: 642
  The sum of the digits are:  12
"""

""" Part A Code Here """
def sum_of_digits(three_digit_number):
    digit_one = three_digit_number // 100
    digit_two = (three_digit_number-(digit_one*100)) // 10
    digit_three = ((three_digit_number-(digit_one*100))-(digit_two*10)) // 1
    
    return (digit_one + digit_two + digit_three)

""" Part B Code Here """
def main():
    three_digit_number = int(input("Please enter a three digit number: "))
    print("The sum of the digits are: ", sum_of_digits(three_digit_number), sep = "")

main()
