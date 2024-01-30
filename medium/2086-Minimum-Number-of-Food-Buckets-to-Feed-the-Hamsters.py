class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        count = 0 # Buckets placed
        arr = list(hamsters) # convert string to array

        # For each cell
        for i in range(0,len(arr)):
            # If it's an unfed hamster
            if arr[i] == 'H':
                # If a bucket can be placed to the right
                if i+1 < len(arr) and arr[i+1] == '.':
                    # If there is a hamster the other side that can be fed
                    if i+2 < len(arr) and arr[i+2] == 'H':
                        # Set that hamster as fed
                        arr[i+2] = 'F'
                    count += 1
                # If a bucket can be placed behind
                elif i-1 >= 0 and arr[i-1] == '.':
                    # Increment the buckets placed
                    count += 1
                # If a bucket can't be placed to feed this hamster
                else:
                    return -1

        return count
