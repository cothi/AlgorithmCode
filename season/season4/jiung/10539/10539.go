//package main

import (
  "fmt"
)

var numArray, ansArray := make([]int, 100)
var num int

func Sequence() {

  ansArray[0] = numArray[0]

  for j := 1; j < num; j++ {
    ansArray[j] = numArray[j] * (j+1)
  }

  for k := num-1; k > 0; k-- {
    ansArray[k] = ansArray[k] - ansArray[k-1]
  }

}


func main() {
  fmt.Scanf("%d", &num)
  
  A := make([]int, num)
  
  for i := 0; i < num; i++ {
    fmt.Scanf("%d", &numArray[i])
  }

  Sequence()

  for j := 0; j < num; j++ {
    fmt.Printf("%d ", ansArray[j])
  }


}
