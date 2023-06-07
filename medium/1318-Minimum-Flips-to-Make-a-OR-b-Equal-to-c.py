class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # Convert inputs to strings of bits
        binA = bin(a)[2:]
        binB = bin(b)[2:]
        binC = bin(c)[2:]

        # Get the max length of one of these strings
        maxLen = max(len(binA), max(len(binB), len(binC)))

        # Ensure all strings are the same length so their characters
        # can easily be compared
        while len(binA) < maxLen:
            binA = '0' + binA
            
        while len(binB) < maxLen:
            binB = '0' + binB

        while len(binC) < maxLen:
            binC = '0' + binC
        
        # Track the number of flips needed
        numFlips = 0

        # For each bit in the strings
        for i in range(0, maxLen):
            # If the target is a 1
            if binC[i] == '1':
                # If neither of the input bits is 1
                if binA[i] == '0' and binB[i] == '0':
                    # Have to flip one of the bits to or to give 1
                    numFlips += 1

            # If the target is a 0
            if binC[i] == '0':
                # If either of the input bits is a 1 it must be
                # flipped so that the or gives 0
                if binA[i] == '1':
                    numFlips += 1

                if binB[i] == '1':
                    numFlips += 1

        return numFlips
