#include <iostream>
#include <vector>

using namespace std;

int solve(vector<int>& nums) {
    for (int i=0; i<nums.size(); i++){
        if (i == nums[i])
            return i;
    }
    return -1;
}

int main() {
	int l, n;
	cout<<"Enter the length of the vector: ";
	cin>>l;
	cout<<"Enter vector elements: \n";
	vector<int> v;
	for (int i=0; i<l; i++){
		cin>>n;
		v.push_back(n);
	}
	cout<<solve(v)<<endl;
	return 0;
}
