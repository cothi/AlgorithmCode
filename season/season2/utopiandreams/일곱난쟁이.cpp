#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  int sum=0;
  int x,y;
  vector<int> dwarfs(9,0);
  for(int i=0;i<9;i++){
    std::cin>>dwarfs[i];
    sum+=dwarfs[i];
  }
  sum-=100;
  for(int i=0;i<8;i++){
    for(int j=i+1;j<9;j++){
      if(dwarfs[i]+dwarfs[j]==sum){
      x = dwarfs[i];
      y = dwarfs[j];
      goto end;
     }
    }
  }
  end:
  sort(dwarfs.begin(),dwarfs.end());
  for(int i=0;i<9;i++){
    if(dwarfs[i]!=x&&dwarfs[i]!=y){
      std::cout<<dwarfs[i]<<"\n";
    }
  }
}