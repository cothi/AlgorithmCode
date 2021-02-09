# 백준_1929

### 2021-02-09

### 소수 구하기

문제링크

[https://www.acmicpc.net/problem/1929](https://www.acmicpc.net/problem/1929)

```kotlin
import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.math.sqrt

fun main() = with(BufferedReader(InputStreamReader((System.`in`)))) {
    val data = StringTokenizer(readLine())
    with(data){
        val min = nextToken().toInt()
        val max = nextToken().toInt()
        getList(max).printDecimal(min, max)
    }
}

fun getList(max: Int): MutableList<Boolean> =
        mutableListOf<Boolean>().apply {
            for (i in 0..max) {
                if (i < 2) add(false)
                else add(true)
            }
        }

/**
 * 에라토스테네스의 체 알고리즘
 */
fun MutableList<Boolean>.printDecimal(min: Int, max: Int) {
    for (i in 0..sqrt(max.toDouble()).toInt()) {
        if (!get(i))
            continue
        for (j in i + i..max step i) {
            set(j, false)
        }
    }
    forEachIndexed { index, b ->
        if (b && index >= min)
            println(index)
    }
}
```

### 코드리뷰

코드리뷰입니다.