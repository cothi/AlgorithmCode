
## 백준 10250번 문제 - ACM 호텔

[link](https://www.acmicpc.net/problem/10250)

### 알고리즘 문제  

```cpp
#include <bits/stdc++.h>

int main(){
    using namespace std;
    
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int caseCount, height, width, order;
    cin >> caseCount;

    for (int i = 0; i < caseCount; ++i) {
        cin >> height >> width >> order;
        int floor = order % height == 0 ? height : order % height;
        int room = ceil((double)order / height);

        if(room < 10) cout << floor << '0' << room << "\n";
        else cout << floor << room << "\n";
    }
  
    return 0;
}
```
