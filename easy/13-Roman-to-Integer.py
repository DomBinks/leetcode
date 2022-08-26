def romanToInt(s: str) -> int:
    """Calculates the numerical value of a string s of roman numerals"""

    # Store numerical values of the numerals 
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    length = len(s) # Cache length of the input string

    total = 0
    for i in range(length):
        current = values[s[i]] # Value of current numeral

        # Check to see if the next numeral is a greater value
        if i < length - 1 and current < values[s[i+1]]:
            total -= current 
        
        else:
            total += current 

    return total