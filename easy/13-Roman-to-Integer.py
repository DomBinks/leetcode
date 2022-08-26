def romanToInt(s: str) -> int:
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    length = len(s)

    total = 0
    for i in range(length):
        current = values[s[i]]

        if i < length - 1 and current < values[s[i+1]]:
            total -= current 
        
        else:
            total += current 

    return total