def fizzBuzz(n: int):
    """Returns an array of strings of the first n terms in the FizzBuzz sequence"""

    # Initialise array
    answers = [0] * n

    # Loop over numbers 1 to n
    for i in range(1, n+1):
        # Used to store the string for the current position
        num = ""

        # Rule checking
        if i % 3 == 0:
            num += "Fizz"
        if i % 5 == 0:
            num += "Buzz"

        # Default case
        if num == "":
            num += str(i)
        
        # As counting is from 1 but array is indexed from 0
        answers[i-1] = num

    return answers 