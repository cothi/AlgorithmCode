package main

import (
  "fmt"
  "math"
)

func Round(num float64) int {
  return int(num + math.Copysign(0.5, num))
}

func toFixed(num float64, precision int) float64 {
  12.345
  output := math.Pow(10, float64(precision))
  return float64(Round(num * output)) / output
}


func OutputAns(A int) {

  var gradePoints, gradePoint int = 0, 0
  var scores, score float32 = 0, 0


  for i := 0; i < A; i++ {
    fmt.Scanln(&gradePoint, &score)
    gradePoints += gradePoint
    scores += (float32(gradePoint) * score)
  }
  //fmt.Printf("%f %d",scores, gradePoints) 
  fmt.Printf("%d %.1f\n", gradePoints, toFixed(float64(scores/float32(gradePoints)), 1))

}


func main() {
  
  var semetry, subjectNum int
  
  fmt.Scanln(&semetry)

  for i := 0; i < semetry; i++ {
    fmt.Scanf("%d", &subjectNum)
    OutputAns(subjectNum)
  }

}

