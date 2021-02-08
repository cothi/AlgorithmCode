# 백준_1920

### 수 찾기

문제링크

[https://www.acmicpc.net/problem/1920](https://www.acmicpc.net/problem/1920)

```kotlin
import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.StringBuilder
import java.util.*

fun main() = with(BufferedReader(InputStreamReader((System.`in`)))){
    val index = readLine().toInt()
    val token = StringTokenizer(readLine())
    val index2 = readLine().toInt()
    val token2 = StringTokenizer(readLine())
    val listA = token.getList(index).sorted()
    val data = token2.getList(index2)
    val result = StringBuilder()
    data.forEach{
        result.append("${listA.find(it)}\n")
    }
    print(result)
}

fun StringTokenizer.getList(index : Int) : MutableList<Int>{
    val list = mutableListOf<Int>()
    for(i in 0 until index){
        list.add(nextToken().toInt())
    }
    return list
}

/**
 * HashMap
 * key : 값
 * value : 순서
 */
fun MutableList<Int>.toMap() : HashMap<Int,Int>{
    return hashMapOf<Int,Int>().apply {
        forEachIndexed { index, value ->
            put(value,index)
        }
    }
}

// Binary Search
fun List<Int>.find(value : Int) : Int{
    var high = size-1
    var low = 0
    while(low <= high){
        val mid = (high+low)/2
        when {
            get(mid) == value -> return 1
            get(mid) > value -> high = mid - 1
            else -> low = mid+1
        }
    }
    return 0
}
```

### 코드리뷰

코드리뷰입니다.