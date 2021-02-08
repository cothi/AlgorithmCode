# 백준_25901719

### 체스판 다시 칠하기

문제링크

[https://www.acmicpc.net/problem/1018](https://www.acmicpc.net/problem/1018)

```kotlin
import java.util.*

fun main(args: Array<String>) =with(Scanner(System.`in`)){
    val height = nextInt()
    val width = nextInt()
    nextLine()
    val data = Array(height){nextLine()}
    val result = findMinChess(width,height,data)
    println(result)
}

fun findMinChess(maxX : Int, maxY : Int , data : Array<String>) : Int{
    val MAX_X = maxX - 8
    val MAX_Y = maxY - 8
    var resultMin = 64
    for(y in 0..MAX_Y){
        for(x in 0..MAX_X) {
            val max = y+8
            resultMin = Integer.min(resultMin,find(x, data.getSliceData(y,max)))
        }
    }
    return resultMin
}

fun Array<String>.getSliceData(min : Int, max : Int) : List<String> =
        slice(min until max)

fun find(x : Int,data : List<String>) : Int{
    var result = 0
    var count = 0
    val MAX_VALUE = 64
    var change = false
    data.forEach {
        val max = x+8
        val line = it.substring(x,max)
        val first = getWhiteBlack(change)
        val second = getWhiteBlack(!change)
        line.forEachIndexed { index, c ->
            if(index%2!=0 && c != first)
                count++
            else if(index%2==0 && c != second)
                count++
        }
        change = !change
    }
    result = Integer.min(count,MAX_VALUE-count)
    return result
}

fun getWhiteBlack(boolean: Boolean) : Char =
        if(boolean) 'W' else 'B'
```

### 코드리뷰

코드리뷰입니다.