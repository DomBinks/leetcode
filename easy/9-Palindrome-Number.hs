-- Converts an integer to a list of digits
intToList :: Int -> [Int]
intToList 0 = []
intToList x = intToList (x `div` 10) ++ [x `mod` 10]

-- Compares the first element of the first array and the last element of the second array
compareFirstAndLast :: [Int] -> [Int] -> Bool
compareFirstAndLast [] [] = True
compareFirstAndLast xs ys = if head (reverse xs) == head ys then compareFirstAndLast (init xs) (tail ys)
              else False

-- Returns whether the input number is a palindrome 
-- (Works as long as the number doesn't start with a 0 because of the way intToList works - removes the leading 0)
palindromeNumber :: Int -> Bool
palindromeNumber x = if length (intToList x) == 1 then True 
                     else if (length (intToList x)) `mod` 2 == 0
                     then compareFirstAndLast (take ((length (intToList x)) `div` 2) (intToList x)) (drop ((length (intToList x)) `div` 2) (intToList x))
                     else compareFirstAndLast (take ((length (intToList x)) `div` 2) (intToList x)) (drop (((length (intToList x)) `div` 2) + 1) (intToList x))