## 시사점

> 문제에서 1번, 2번, 3번의 세 장의 색종이가 순서대로 놓인다고 합니다. 따라서 해당 다음 색종이가 전의 해당 색종이 위에 덮여졌을 때를 고려하고 문제를 푸는 것이 포인트입니다.

## 함수 리스트

-- process
> 문제를 푸는 과정인 함수

-- output
> 결과 값을 출력하는 함수

-- main
> 함수를 불러오는 main

## 소스코드 


```c++
/******
 * Author      :    Jiung
 * Filename    :    10163.cpp
 * Version     :    Apple clang version 12.0.0 (clang-1200.0.32.27)
 * Date        :    2021-02-16
 * Copyright   :    Free
 */
  
#include <iostream>
#include <cstring> 
using namespace std;

struct paper {
    int N, x, y, w, h;
};


int arr[101][101] = {0, };
int ans[101];
paper one;


/**
 * x, y, w, h 값을 받은 뒤, 해당 색종이의 면적을 구하는 함수
 *
 * @  리턴값: 전역변수를 이용했기 때문에 리턴값은 따로 없습니다.
 */
void process() {
    
    /**
     * 변수 k를 이용하여, 색종이가 몇번째인지를 확인합니다.
     */
    int k=1;
    while(k <= one.N) {     
        cin >> one.x >> one.y >> one.w >> one.h;

        for(int i=one.y; i < one.y + one.h; i++) {
            for(int j=one.x; j < one.x + one.w; j++) {
                if (arr[i][j] == 0) {
                    ans[k] += 1;
                    arr[i][j] = k;
                } else {
                    ans[arr[i][j]] -= 1;
                    ans[k] += 1;
                    arr[i][j] = k;
                }
            }
        }
        k += 1;
    }
}

/**
 * 전역변수인 ans값을 출력하는 함수
 */
void OuputAns() {
    // ans output
    for(int i=1; i <= one.N; i++) {
        cout << ans[i] << endl;
    }
}

int main() {

    // input
    memset(ans, 0, sizeof(ans));
    cin >> one.N;
    
    // process
    process();

    // result output
    OuputAns();
}
```

## 코드리뷰 

