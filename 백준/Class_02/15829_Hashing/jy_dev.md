# 백준_15829

### Hashing

문제링크

[https://www.acmicpc.net/problem/15829](https://www.acmicpc.net/problem/15829)

```kotlin
import java.io.BufferedReader
import java.io.InputStreamReader
val MULTIPLY = 31
val m = 1234567891L
fun main() = with(BufferedReader(InputStreamReader((System.`in`)))){
    val index = readLine().toInt()
    val data = readLine()
    print(data.getHash().getMod(m))
}

fun Char.getUniqueNumber() : Int =
        toInt() - 96

fun Char.getHashAtoZ(index : Int, r : Long) : Long{
    return getUniqueNumber() * r
}

fun String.getHash() : Long {
    var result = 0L
    var r = 1L
    forEachIndexed { index, data ->
        result += data.getHashAtoZ(index,r).getMod(m)
        r = (r*MULTIPLY).getMod(m)
    }
    return result
}

fun Long.getMod(m : Long) : Long =
        this%m
```

### 코드리뷰

코드리뷰입니다.

```
작성자: 한지웅
작성일: 2020-02-12

좋았던 점
함수 단위로 나눠서 보기 좋았습니다.

아쉬운 점
전에도 말했던 코드리뷰이지만, 여전히 코드리뷰가 적어보입니다.

```

