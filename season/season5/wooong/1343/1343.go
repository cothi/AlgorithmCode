package main

import (
  "fmt"
)

func errorCheck(inputString string) bool {

  var cnt int = 0
  
  for i := 0; i < len(inputString); i++ {
    if inputString[i] == 88 {
      cnt += 1
    }
  }
  if cnt % 2 == 0 {
    return true
  } else {
    return false 
  }
}

func main() {
  
  var inputString, ans string
  var errorBool bool
  var check int = 0

  fmt.Scanf("%s", &inputString)

  errorBool = errorCheck(inputString)
  check = 0
  if errorBool {

    for i := 0; i < len(inputString); i++ {
      if inputString[i] == 88 {
        check += 1

        if check >= 4 {
          check = 0
          ans += "AAAA"
        }
      } else{

        if check == 2 {
          ans += "BB"
          ans += "."
          check = 0
        } else if check == 4 {
          ans += "AAAA"
          ans += "."
          check = 0
        } else if check == 0 {
          ans += "."
        } else 
        {
          fmt.Println("-1")
          return 
        }
      }
    }
     if check == 2 {
        ans += "BB"
      }
      fmt.Printf("%s\n", ans)
  } else {
    fmt.Println("-1")
  }
}
