class Solution {
public:
    vector<int>::iterator getMin(vector<int>& nums, int indent)
    {
        if(indent > nums.size() / 2)
            return nums.begin();
        
        if(*(nums.begin()+indent) < *(nums.end()-1-indent))
        {
            return nums.begin();
        }
        else if(*(nums.begin()+indent) > *(nums.end()-1-indent))
        {
            return nums.end()-1;
        }
        else
        {
            return getMin(nums, indent+1);
        }
    }

    int maximumScore(vector<int>& nums, vector<int>& multipliers) {
        int score = 0;
        int m = multipliers.size();

        for(int i = 0; i < m; i++)
        {
            cout << "I: " << i << endl;
            cout << "Mult: " << *(multipliers.begin()+i) << endl;
            vector<int>::iterator min;
            vector<int>::iterator max;
            vector<int>::iterator num;
            
            min = getMin(nums, 0);
            max = (min == nums.begin()) ? nums.end()-1 : nums.begin();
            num = *(multipliers.begin()+i) > 0 ? max : min;
            cout << "Num: " << *num << endl;

            score += *(multipliers.begin()+i) * *num;
            if(num == nums.begin())
            {
                nums.erase(nums.begin());
            }
            else
            {
                nums.pop_back();
            }
        }

        return score;
    }
};

