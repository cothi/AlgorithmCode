package main

import "fmt"

func HowDays(A int64, B int64, V int64) int64 {

  if (V - B) % (A - B) != 0 {
    return (((V - A) / (A - B)) + 2)
  } else {
    return ((V - A) / (A - B)) + 1
  }
}

func main() {
  var V, A, B int64
  fmt.Scan(&A, &B, &V)
  ans := HowDays(A, B, V)
  print(ans)

}
