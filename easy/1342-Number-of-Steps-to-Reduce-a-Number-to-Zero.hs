reduce :: Int -> Int -> Int
reduce 0 y = y
reduce x y = if even x then reduce (x`div`2) (y+1) else reduce (x-1) (y+1)

stepsToReduce :: Int -> Int
stepsToReduce x = reduce x 0