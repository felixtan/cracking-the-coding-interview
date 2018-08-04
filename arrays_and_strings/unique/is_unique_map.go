package unique

import (
  "fmt"
  "bufio"
  "os"
  "strings"
)

func unique(s string) bool {
  charMap := make(map[rune]uint)
  for _, char := range s {
    if _, present := charMap[char]; !present {
      charMap[char] = 1
    } else {
      return false
    }
  }
  return true
}

func main() {
  reader := bufio.NewReader(os.Stdin)
  fmt.Print("Enter a string: ")
  s, _ := reader.ReadString('\n')
  s = strings.TrimSpace(s)
  if unique(s) {
    fmt.Printf("%s has all unique chars\n", s)
  } else {
    fmt.Printf("%s has repeating chars\n", s)
  }
}
