backwardsSum :: [Int] -> [Int] -> [Int]
backwardsSum xs [] = xs
backwardsSum [] (y:ys) = backwardsSum [y] ys
backwardsSum xs (y:ys) = backwardsSum (((head xs) + y):xs) ys

runningSum :: [Int] -> [Int]
runningSum xs = reverse (backwardsSum [] xs)
