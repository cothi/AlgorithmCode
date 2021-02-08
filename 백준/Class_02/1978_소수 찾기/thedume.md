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

코드리뷰입니다.
