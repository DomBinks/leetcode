// Returns x^n
double myPow(double x, int n){
    // Special cases 
    if(n == 0)
    {
        return 1.0;
    }
    if(x == 1.0 || n == 1)
    {
        return x;
    }
    
    double out; // Stores the output value
    unsigned int ln; // Used to store the power as an unsigned int

    // Used to indicate whether the reciprocal needs to be returned
    int reciprocal = 0;
    // Store the power in ln
    if(n < 0)
    {
        ln = - (unsigned) n;
        reciprocal = 1;
    }
    else
    {
        ln = n;
    }

    // Split the calculation into 2 equal halves
    double half = myPow(x, ln / 2);
    if(ln % 2 == 0)
    {
        out = half * half; // Combine the 2 halves
    }
    else
    {
        // Need an extra * x if the power is odd
        out = half * half * x;
    }

    // Return the reciprocal of out if the power is negative
    return reciprocal == 1 ? 1.0/out : out;
}