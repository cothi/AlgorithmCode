//package test
package main

import (
  "fmt"
  "strings"
  "strconv"
)

func ReturnInt(A []string, B []string) int {
  var AArray [3]int
  var BArray [3]int

  for i := 0; i < len(A); i++ {

    AArray[i], _ = strconv.Atoi(A[i])
    BArray[i], _ = strconv.Atoi(B[i])
  }

  
  //fmt.Println(AArray[1:3])

  var ans int = 0

  AAInt := A[0] + A[1] + A[2] 
  BBInt := B[0] + B[1] + B[2]

  AAA, _ := strconv.Atoi(AAInt)
  AAB, _ := strconv.Atoi(BBInt)

  fmt.Println(AArray, AAB, AAA, A) 
  if AAA % 3 == 0 { ans += 1 }
 
  for int(AAA) != int(AAB) {

    if (AArray[0] == 1) {
      println(AAA)
    }
    AArray[2] += 1
    if AArray[2] >= 60 {
      AArray[2] = 0
      AArray[1] += 1
    }

    if AArray[1] >= 60 {
      AArray[1] = 0
      AArray[0] += 1
    }

    if AArray[0] >= 24 {
      AArray[0] = 0
    }

    AAInt = strconv.Itoa(AArray[0]) + strconv.Itoa(AArray[1]) + strconv.Itoa(AArray[2])      
    AAA, _ = strconv.Atoi(AAInt)
    if AAA % 3 == 0 { ans += 1 }
  }

  return ans
}


func main() {
  
  for i := 0; i < 3; i++ {
    var startTime, endTime string
    fmt.Scanln(&startTime, &endTime)
    startTimeArray := strings.Split(startTime, ":")
    endTimeArray := strings.Split(endTime, ":")
    ans := ReturnInt(startTimeArray, endTimeArray)
    fmt.Println(ans)
  } 

  }
