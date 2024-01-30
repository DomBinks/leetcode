class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen = {} # Store cards that have been seen
        s = 9999999 # Stores minimum consecutive cards

        count = 0 # Current card

        # For each card
        for card in cards:
            # If the card has been seen
            if card in seen:
                # Update the minimum if this interval is smaller
                s = min(count - seen[card] + 1, s)
                # Update when this card was last seen
                seen[card] = count
            else:
                # Update when this card was last seen
                seen[card] = count
                
            # Increment the current card
            count += 1

        if s == 9999999:
            return -1
        else:
            return s
