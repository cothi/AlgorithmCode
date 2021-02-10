## 10845 큐 

### 문제링크
https://www.acmicpc.net/problem/1978


### 문제풀이 및 주석

```c++
/******
 * Author      :    Jiung
 * Filename    :    test.cpp
 * Version     :    Apple clang version 12.0.0 (clang-1200.0.32.27)
 * Date        :    2021-02-10
 * Copyright   :    Free
 */
  
#include <iostream> // 입출력 사용
#include <string>  // 문자열 사용 
#include <deque> // deque 구현 사용
using namespace std; // 표준 문자 사용

#define endl "\n"; // endl을 "\n"으로 정의

/* global variable
 * 명령어 갯수 N
 * push에 쓰일 변수 PushNum
 * deque 정의 Deque
 * 명령어로 쓰일 command
 */
int N, PushNum;
deque<int> Deque;
string command;


/*
 * push function 구현
 * num 매겨변수를 입력받아서
 * Deque에 push_back을 진행합니다.
 */
void push(int num) {
    Deque.push_back(num);
}

/* 
 * front function 구현
 * Deque의 맨 앞의 숫자를 
 * 출력하는 함수
 */
void front() {
    if (Deque.size() == 0) {
        cout << -1 << endl;
    } else {
        cout << Deque.front() << endl;
    }
}

/*
 * back function 구현
 * Deque의 맨 뒤의 숫자를
 * 출력하는 함수
 */
void back() {
    if (Deque.size() == 0) {
        cout << -1 << endl;
    } else {
        cout << Deque.back() << endl;
    }
}

/* 
 * pop function 구현
 * pop의 경우 맨 앞의 숫자를
 * 빼는 함수
 */
void pop() {
    int tmp;
    if (Deque.size() == 0) {
        cout << -1 << endl;
    } else {
        int tmp = Deque.front();
        cout << tmp << endl;
        Deque.pop_front();
    }
}

/* 
 * size function 구현
 * Deque의 크기를 출력하는
 * 함수
 */
void size() {
    
    cout << Deque.size() << endl;
}

/*
 * empty function 구현
 * Deque가 비어있는지 확인하는
 * 함수
 */
void empty() {
    if (Deque.size() == 0) {
        cout << 1 << endl;
    } else {
        cout << 0 << endl;
    }
}

/* 
 * main
 */
int main()
{
    /* Input
     * 명령어 갯수 입력
     */
    cin >> N;

    /* process
     * 해당 커멘드를 입력받아서
     * if statement를 이용해서 해당 함수를 실행
     * 다만, push의 경우 숫자를 따로 입력 받아서 매개변수로
     * 넘기는 방향으로 구현
     */
    while (N) {
        cin >> command;
        
        if(command == "push") {
            cin >> PushNum;
            push(PushNum);
        } else if (command == "pop") {
            pop();
        } else if (command == "size") {
            size();
        } else if (command == "empty") {
            empty();
        } else if (command == "front") {
            front();
        } else if (command == "back") {
            back();
        }
        N -= 1;
    }
}

```

<br><br>

## 코드 리뷰

