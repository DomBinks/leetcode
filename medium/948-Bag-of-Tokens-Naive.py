class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort() # Sort the tokens
        total = sum(tokens) # Find the total potential power that can be gained 

        if tokens != [] and tokens[0] > power: # If you can't play any face up
            return 0

        toScore = 0 # Amount used to score points
        score = 0 # Current score

        # While there are still token(s) that can be played face up
        # (Have enough power to do so)
        while tokens != [] and total + power - tokens[0] >= toScore + tokens[0]:
            toScore += tokens[0] # Play the token with the lowest value
            total -= tokens.pop(0) # Lose potential power equal to the token being played
            score += 1 # Increment the score
        
        toPower = power # Amount used to gain power
        while toPower < toScore: # While more power is needed
            toPower += tokens.pop() # Play the token with the highest value
            score -= 1 # Decrement the score

        return score 
