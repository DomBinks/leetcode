// Returns the number of steps needed to reduce the provided number
// to 0
int numberOfSteps(int num)
{
    int steps = 0; // Counts the number of steps

    // Loops while the number hasn't been reduced to 0
    while(num > 0)
    {
        // If the number is even
        if(num % 2 == 0)
        {
            num /= 2;
        }
        // If the number is odd
        else
        {
            num--;
        }

        steps++; // Increments the step counter
    }

    return steps;
}