# 백준_1874

### 스택 수열

문제링크

[https://www.acmicpc.net/problem/1874](https://www.acmicpc.net/problem/1874)

```kotlin
import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.StringBuilder
import java.util.*

fun main() = with(BufferedReader(InputStreamReader((System.`in`)))){
    val index = readLine().toInt()
    val list : Queue<Int> = LinkedList()
    for(i in 0 until index){
        list.offer(readLine().toInt())
    }
    println(list.stackSequence())
}

fun Queue<Int>.stackSequence() : StringBuilder{
    val result = StringBuilder()
    var index = 1
    val list = Stack<Int>().apply {
        add(1)
        result.addPlus()
    }
    while(peek()!=null){
        when {
            list.isEmpty() || peek() > list.peek() -> {
                index += 1
                list.push(index)
                result.addPlus()
            }
            peek() == list.peek() -> {
                list.pop()
                poll()
                result.addMinus()
            }
            peek() < list.peek() -> {
                return result.resultNO()
            }
        }
    }
    return result
}

fun StringBuilder.addPlus() = append("+\n")
fun StringBuilder.addMinus() = append("-\n")
fun StringBuilder.resultNO() = apply {
    clear()
    append("NO")
}
```

### 코드리뷰

코드리뷰입니다.
