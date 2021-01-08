// this is how i checked locally
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool solve(vector<int>& nums) {
	sort(nums.begin(), nums.end(), greater<>());
	return nums[0] > nums[1]*2;
}


int main() {
    int n;
    int c;
	vector<int> v;
	cin>>n;
	for (int i=0;i<n;++i){
        cin>>c;
        v.push_back(c);
	}
	cout<<solve(v)<<endl;
	return 0;
}

// this is what i submited on bsio
/*

bool solve(vector<int>& nums) {
	sort(nums.begin(), nums.end(), greater<>());
	return nums[0] > nums[1]*2;    
}
 
 */


