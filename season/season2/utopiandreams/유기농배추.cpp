#include <iostream>
#include <vector>
using namespace std;

int map[50][50];
int moveX[4]={0,1,0,-1};
int moveY[4]={1,0,-1,0};

void init(){
  for(int i=0;i<50;i++){
    for(int j=0;j<50;j++){
      map[i][j]=0;
    }
  }
}

void BFS(int &x,int &y,int &w,int &l){
  int moveX[4]={0,1,0,-1};
  int moveY[4]={1,0,-1,0};
  if(map[x][y]==1){
    map[x][y]=0;
    for(int i=0;i<4;i++){
    int a = x + moveX[i];
    int b = y + moveY[i];
    if(a>=0&&b>=0&&a<w&&b<l)
    BFS(a,b,w,l);
    }
  }
}

int main() {
  int testcase;
  cin>>testcase;
  vector<int> result(testcase,0);

  for(int k=0;k<testcase;k++){
    int count=0;
    int Cabbage,Width,Length;
    cin>>Width>>Length>>Cabbage;

    init();

    for(int i=0;i<Cabbage;i++){
      int a,b;
      cin>>a>>b;
      map[a][b]=1;
    }

    for(int i=0;i<Width;i++){
      for(int j=0;j<Length;j++){
        if(map[i][j]==1){
          BFS(i,j,Width,Length);
          count++;
        }
      }
    }
    result[k]=count;
  }
  for(int i=0;i<testcase;i++){
    cout<<result[i]<<"\n";
  }
}