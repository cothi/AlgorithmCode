# 백준_1978

### 소수 찾기

문제링크

https://www.acmicpc.net/problem/1978

```C#
using System;

namespace Beakjoon
{
    class Program
    {
        static void Main(string[] args)
        {
            int cnt = 0;

            string line = Console.ReadLine();
            int linenumber = int.Parse(line);

            string primeline = Console.ReadLine();
            string[] primelinearray = primeline.Split(" ");
            int[] primenumber = new int[linenumber];

            for (int n = 0; n < linenumber; n++)
            {
                primenumber[n] = int.Parse(primelinearray[n]);
            }

            int target = 1000;

            bool[] arr = new bool[target + 1];
            arr[0] = true;
            arr[1] = true;
            for (int i = 2; i <= target; i++)
            {
                if (arr[i])
                    continue;


                for (int j = 2 * i; j <= target; j += i)
                {
                    arr[j] = true;
                }
            }

            for (int j = 0; j < linenumber; j++)
            {
                for (int i = 2; i <= target; i++)
                {
                    if ((arr[i] == false) && (i == primenumber[j]))
                        cnt++;
                }
            }
            Console.WriteLine(cnt);
        }
    }
}
```

### 코드리뷰
```
작성자 : jy_dev
작성일 : 2021-02-10
코드는 깔끔하게 잘작성하셔서 코드를 읽는데 부담은 없었습니다.
구현하실때 최소한의 함수단위로 나누어서 작성하시고 주석만 달아주시면 코드가 더 깔끔해 질 것 같습니다.
```
