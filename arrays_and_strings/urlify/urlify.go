package main

import (
  "fmt"
  "strings"
)

func main() {
  var (
    test   = "Mr John Smith    "
    result = Urlify(test)
  )
  fmt.Println(result)
}

func Urlify(s string) string {
  var (
    code  = "%20"
    space = rune(' ')
    runes = []rune(strings.TrimSpace(s))
    b     strings.Builder
  )

  for _, r := range runes {
    if r == space {
      b.WriteString(code)
    } else {
      b.WriteRune(r)
    }
  }

  return b.String()
}
