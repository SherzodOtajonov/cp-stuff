#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solve(vector<int> nums) {
    sort(nums.begin(), nums.end());
    vector<int> v;
    for (int i=0; i<nums.size(); i++){
        if (i<2 || (i>=2 && v[v.size()-2] != nums[i]))
            v.push_back(nums[i]);
    }
    return v;
}

int main() {
	vector<int> nums, r;
	int l, cur;
	cout<<"Enter vector length: ";
	cin>>l;
	cout<<"Enter vector elements: ";
	for (int i=0; i<l; i++){
		cin>>cur;
		nums.push_back(cur);
	}
	r = solve(nums);
	for (int i=0; i<r.size(); i++){
		cout<<r[i];
	}
	return 0;

}
