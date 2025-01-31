# This is assignment1_part1 for I.S.211

# assignment1_part1.py

# Function to count elements divisible by 'divide'
def listDivide(numbers, divide=2):
    return len([num for num in numbers if num % divide == 0])

# Custom exception class
class ListDivideException(Exception):
    pass

# Function to test listDivide
def testListDivide():
    try:
        assert listDivide([1, 2, 3, 4, 5]) == 2
        assert listDivide([2, 4, 6, 8, 10]) == 5
        assert listDivide([30, 54, 63, 98, 100], divide=10) == 2
        assert listDivide([]) == 0
        assert listDivide([1, 2, 3, 4, 5], 1) == 5
    except AssertionError:
        raise ListDivideException("Test failed")

# Run the tests
testListDivide()
