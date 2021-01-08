#include <iostream>
#include <vector>
// ok. i will reactor this later. im new to cpp

using namespace std;

int main(){
	int n;
	cin>>n;
	if (n==1) {
        cout<<1<<endl;
        return 0;
	}
	else if (n==4) {
        cout <<"2 4 1 3"<<endl;
        return 0;
	}
	if (n<5) {
        cout<<"NO SOLUTION";
        return 0;
	}
	vector<int> v1(n);
	vector<int> v2(n);
    for(int i=1;i<=n;++i){
        if(i%2!=0)
            v1.push_back(i);
        else
            v2.push_back(i);
    }
    for(int i=0;i<v1.size();++i) {
        if (v1[i] != 0)
                cout<<v1[i]<<" ";
    }
    for(int i=0;i<v2.size();++i) {
        if (v2[i] != 0)
                cout<<v2[i]<<" ";    }
	return 0;
}



