// https://leetcode.com/problems/find-original-array-from-doubled-array/discuss/2581075/Easy-C%2B%2Boror-using-queue-oror-94-less-memory-oror-Explained-oror-Beginner-Friendly
class Solution {
public:
    vector<int> findOriginalArray(vector<int>& changed) {
        sort(changed.rbegin(), changed.rend());
        queue<int> biggest;
        int length = changed.size();
        vector<int> out;

        for(int i = 0; i < length; i++)
        {
            if(biggest.empty())
                biggest.push(changed[i]);
            else if(biggest.front() == changed[i] * 2)
            {
                biggest.pop();
                out.push_back(changed[i]);
            }
            else
                biggest.push(changed[i]);
        }

        if(biggest.empty())
            return out;
        else
            return vector<int>();
    }        
};

