package permutation

import (
  "fmt"
  "bufio"
  "os"
  "strings"
  "math/rand"
  "time"
)

func main() {
  reader := bufio.NewReader(os.Stdin)
  fmt.Print("Enter a string: ")
  a, _ := reader.ReadString('\n')
  a = strings.TrimSpace(a)

  fmt.Print("Enter another string: ")
  b, _ := reader.ReadString('\n')
  b = strings.TrimSpace(b)

  if IsPermutationLoopsOnly(a, b) {
    fmt.Println("permutations")
  } else {
    fmt.Println("not permutations")
  }
}

func IsPermutationLoopsOnly(a, b string) bool {
  if len(a) != len(b) {
    return false
  }

  var (
    matchIndex = -1
    aRunes     = []rune(a)
    t          = []rune(b)
  )

  Outer:
  for aPos, aRune := range aRunes {
    if matchIndex > -1 {
      t = append([]rune(t[:matchIndex]), []rune(t[matchIndex+1:len(t)])...)
    }

    for tPos, tRune := range t {
      //fmt.Printf("%c = %c?\n", tRune, aRune)
      if tRune == aRune {
        if aPos == len(aRunes) - 1 {
          return true
        } else {
          matchIndex = tPos
          //fmt.Printf("match at %d\n", matchIndex)
          continue Outer
        }
      } else {
        continue
      }
    }
    return false
  }
  return false
}

func IsPermutationRuneFreqMap(a, b string) bool {
  var (
    aRunes = []rune(a)
    bRunes = []rune(b)
  )

  aRuneFreq := make(map[rune]uint)
  bRuneFreq := make(map[rune]uint)

  if len(aRunes) != len(bRunes) {
    return false
  }

  for _, aRune := range aRunes {
    _, prs := aRuneFreq[aRune]

    if prs {
      aRuneFreq[aRune] += 1
    } else {
      aRuneFreq[aRune] = 1
    }
  }

  for _, bRune := range bRunes {
    _, prs := bRuneFreq[bRune]

    if prs {
      bRuneFreq[bRune] += 1
    } else {
      bRuneFreq[bRune] = 1
    }
  }

  if len(aRuneFreq) != len(bRuneFreq) {
    return false
  }

  for aRune, aFreq := range aRuneFreq {
    bFreq, prs := bRuneFreq[aRune]

    if !prs || aFreq != bFreq {
      return false
    }
  }

  return true
}

// shuffle a string
func Shuffle(s string) string {
  runes := []rune(s)

  // seed the pseudo-random generator
  rand.Seed(time.Now().UTC().UnixNano())

  rand.Shuffle(len(runes), func(i, j int) {
    runes[i], runes[j] = runes[j], runes[i]
  })

  return string(runes)
}
