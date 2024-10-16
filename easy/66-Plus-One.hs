-- Recursive function
recur :: [Int] -> [Int] -> [Int]
-- Singleton list case
recur (x:[]) [] = if x > 9 then [1,x-10] -- If digit is above 9
                  else [x] -- If digit is below 10
-- Base case for non-singleton lists
recur (x:[]) ys = if x > 9 then [1,x-10] ++ ys -- If digit is above 9
                  else x:ys -- If digit is below 10
-- Recursive case for non-singleton lists
recur xs ys = if (head (reverse xs)) > 9 then recur ((init (init xs)) ++ [((reverse xs) !! 1) + 1]) ([0] ++ ys) -- If digit is above 9
              else recur (init xs) ([(head (reverse xs))] ++ ys) -- If digit is below 10

-- Add 1 to the input number provided as a list
plusOne :: [Int] -> [Int]
plusOne xs = recur ((init xs) ++ [(head (reverse xs)) + 1]) [] -- Adding 1 to the last element in the list