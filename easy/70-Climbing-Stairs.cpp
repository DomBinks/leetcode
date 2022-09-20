class Solution {
public:
    int climbStairs(int n) {
        int steps[46]; // Used to the number of ways to climb n steps
        steps[1] = 1; // Manually set value for 1
        steps[2] = 2; // Manually set value for 2
        
        for(int i = 3; i <= n; i++) // For 3 to n
        {
            // To climb i steps you either climb i-1 steps and add 1 step, or
            // climb i-2 steps and add 2
            steps[i] = steps[i-1] + steps[i-2];
        }
        
        return steps[n];
    }
};
