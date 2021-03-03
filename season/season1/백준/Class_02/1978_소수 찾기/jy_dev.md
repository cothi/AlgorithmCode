# 백준_1978

### 2021-02-09

### 소수 찾기

문제링크

[https://www.acmicpc.net/problem/1978](https://www.acmicpc.net/problem/1978)

```kotlin
import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.math.sqrt

fun main() = with(BufferedReader(InputStreamReader((System.`in`)))) {
    val index = readLine().toInt()
    val st = StringTokenizer(readLine())
    var count = 0
    for(i in 0 until index){
        if(st.nextToken().toInt().isDecimal())
            count++
    }
    print(count)
}

fun Int.isDecimal() : Boolean{
    if(this < 2)
        return false
    for(i in 2..sqrt(this.toDouble()).toInt()){
        if(this%i == 0)
            return false
    }
    return true
}
```

### 코드리뷰

코드리뷰입니다.