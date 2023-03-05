"""
This is the first part of qustion 1

Complete the function below to compute a dogs age in human years according
to the following formula (according to the American Kennel Club):

- The first year of a dog's life equals 15 human years
- The second year of a dog's life equals 9 human years
- Each year after that equals 5 human years

You may assume that the dog_years parameter is always an integer

If the dog_years parameter is less than or equal to 0, the function should
return None

In dogs_age_test.py, write as many unit tests needed for complete code coverage
of your function.

Example: A dog whose age is 7 would be be 49 (15 + 9 + 5 + 5 + 5 + 5 + 5) in
         human years

Be careful of Magic Numbers in your solution
"""


def human_years(dog_years):
    """
    Computes a dogs age in human years according to the AKC formula
    Parameters:
        dog_years - a dogs age in years (any positive integer)
    Returns: the dogs age in human years if dog_years greater than 0
             None if dog_years is less than or equal to 0
    """
    if dog_years <= 0:
        return None
    
    if dog_years == 1:
        return 15
    
    if dog_years == 2:
        return 15 + 9
    
    if dog_years > 2:
        dog_years -= 2
        return 15 + 9 + (5*dog_years) 

""" 
You do not have to write a main but you can if you would like to.
The tests in part 2 will be used to run your function.             
"""
def main():
    print(human_years(3)) # manual testing :p

main()