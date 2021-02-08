# 문제 링크

[https://www.acmicpc.net/problem/1874](https://www.acmicpc.net/problem/1874)


# 소스코드 및 주석

```c++
/******
 * Author      :    Jiung
 * Filename    :    1874.cpp
 * Version     :    Apple clang version 12.0.0 (clang-1200.0.32.27)
 * Date        :    2021-02-08
 * Copyright   :    Free
 */
  
#include <iostream>
#include <deque>
using namespace std;

/*
 * 앞에 부분을 POP을 하기 위해서, deque 라이브러리를 사용했습니다.
 */

/*
 * 1 ~ N 까지 담을 stack
 * 예제 입력을 담을 command
 * 정답을 담을 ans
 */

deque<int> stack;
deque<int> command;
deque<char> ans;

int main()
{
    // 1부터 N까지 변수와 입력 부분 while 문에 조건을 담을 i
    int N, command1;
    cin >> N;

    int i=1;
    /*
     * 예제입력 부분
     */

    while(i <= N)
    {
        cin >> command1;
        command.push_back(command1);
        i += 1;
    }

    /*
     * 과정 부분
     * stack이 1 ~ N으로 순차적으로 증가하기 위한, 변수를 i로 설정합니다.
     * 그리고, dequedls push, pop을 활용해서 진행합니다.
     */
    i=0; 
    while(command.size()) {

        /*
         * 만약 stack deque가 비어있다면, if이 비교가 힘들어지므로 if statement
         * 를 걸어두어서, 문제의 조건인 오름차순을 변수 i를 활용해서 추가를 진행합니다.
         */
        if (stack.empty()) {
            ans.push_back('+');
            i += 1;
            stack.push_back(i);
        }
        /*
         * stack의 뒷부분과 command의 앞부분이 같다면, command 앞부분을 pop
         * 그리고 stack 부분도 pop을 해줍니다. 이유는 문제의 조건인 똑같은 수
         * 가 없다는 점을 이용했습니다.
         */
        if (stack.back() == command.front()) {
            ans.push_back('-');
            stack.pop_back();
            command.pop_front();

        /*
         * 만약 stack의 마지막 부분이 command 앞부분보다 커지면, i가 다음 단계에서
         * 계속 증가합니다. 그러면 비교할 필요가 없으므로 제거하지 못합니다.
         * 따라서, 반복문을 종료하고 NO를 출력하고 main을 끝냅니다.
         */
        } else if (stack.back() > command.front()) {
            cout << "NO";
            return 0;
        /*
         * 같지도 않고, 크지도 않으므로 증가를 진행합니다.
         * 그리고 증가했다는 표시인 +를 ans에 push합니다.
         */
        } else { 
            ans.push_back('+');
            i += 1;
            stack.push_back(i);
        }

    }
    
    /*
     * 정상적으로 command가 끝나서 종료되었을 경우, 해당 반복문을 진행하여 
     * 정답을 출력합니다.
     */
    i=0;
    int size = ans.size();
    while (i < size) {
        cout << ans[i] << "\n";
        i += 1;
    }
}
```



# 코드리뷰
