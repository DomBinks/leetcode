class Solution {
public:
    vector<int> findOriginalArray(vector<int>& changed) {
        if(changed.size() % 2 != 0)
            return vector<int>();

        sort(changed.begin(), changed.end());
        vector<int> output;

        int loops = changed.size() / 2;
        for(int i = 0; i < loops; i ++)
        {
            int current = changed[0];
            changed.erase(changed.begin());

            if(binary_search(changed.begin(), changed.end(), current*2)) 
            {
                int index;
                // Speed this up
                for(int j = 0; j < changed.size(); j++)
                {
                    if(changed[j] == current*2)
                    {
                        index = j;
                        break;
                    }
                }

                changed.erase(changed.begin()+index);
                output.push_back(current);
            }
            else
                return vector<int>();
        }

        return output;
    }
};
