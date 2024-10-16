maximumWealth :: [[Int]] -> Int
maximumWealth (x:[]) = sum x
maximumWealth (x:xs) = max (sum x) (maximumWealth xs)