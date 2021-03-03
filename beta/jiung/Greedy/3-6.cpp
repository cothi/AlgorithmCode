/******
 * Author      :    Jiung
 * Filename    :    3-6.cpp
 * Version     :    Apple clang version 12.0.0 (clang-1200.0.32.27)
 * Date        :    2021-01-26
 * Copyright   :    Free
 */
  
#include <iostream>
  
using namespace std;

/*
 * 1이 될 때까지, 최소 횟수 구하기.
 * 
 * 1. N을 K로 나누거나
 * 2. N에서 -1을 빼거나를 반복한다.
 */

int main(){
   int n, k, result = 0;

   scanf("%d %d", &n, &k);

   while(true) {

       
       result = (n/k) * k;
       n -= result;


       // n이 k보다 나눌 수 없을 때 반복문을 탈출합니다.
       if (n < k) {
           break;
       }

       // k로 나누기를 반복한다. k보다 크기 때문이다.
       result += 1;
       n /= k;
   }   
   // 마지막으로 남은 수에 대하여 1을 빼는 것으로 마무리 합니다.
   result += (n - 1);
   printf("%d", result);
}
