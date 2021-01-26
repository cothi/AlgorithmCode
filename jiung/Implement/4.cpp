/******
 * Author      :    Jiung
 * Filename    :    4-1.cpp
 * Version     :    Apple clang version 12.0.0 (clang-1200.0.32.27)
 * Date        :    2021-01-27
 * Copyright   :    Free
 */
  
#include <iostream>
#include <string>
using namespace std;


// 나이트가 상, 하, 좌, 우, 대각선으로 이동할 수 있도록 8가지 정의.
int dx[8] = {-2, -2, -1, 1, 2, 2, 1, 1};
int dy[8] = {-1, 1, 2, 2, -1, 1, -2, -2};
int ans = 0;

int main()
{
    string InputData;
    cin >> InputData;
    // 숫자형으로 변환을 진행합니다.
    int x = (InputData[1] - '0') -1;
    // 아스키 코드의 정수로 변환합니다.
    int y =  InputData[0] - 'a';

    for(int i = 0; i < 8; i++){

        // nx, ny 8가지를 다 계산합니다.
        int nx = x + dx[i];
        int ny = y + dy[i];

        // 범위가 벗어난 경우 
        if (nx < 0 || nx > 7 || ny < 0 || ny > 7)
            continue;
        else 
            ans++;
    }
    // 정답 출력
    printf("%d", ans);
}
