class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int n = arr.size();
        int temp,mx=-1;
        for(int i = n-1 ;i>=0;i--)
           {
             temp = arr[i];
             arr[i]=mx;
             mx = max(temp,mx);
           }
        return arr;
    }
};