recur :: String -> Int -> Int -> Int -> Int
-- Base case -> return number of balanced strings (o)
recur "" l r o = if (l == 0 && r == 0) || l /= r then o
                 else o+1
-- Recursive case -> increment correct counter
recur s l r o = if (l == 0 && r == 0) || l /= r then
                   if (s !! 0) == 'L' then recur (tail s) (l+1) r o
                   else recur (tail s) l (r+1) o
                else
                   recur s 0 0 o+1

-- Returns the maximum number of balanced strings that can be obatined
balancedStringSplit :: String -> Int
balancedStringSplit s = recur s 0 0 0