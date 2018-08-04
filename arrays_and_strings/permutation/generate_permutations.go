package permutation

import (
  "strings"
)

func GeneratePermutations(s string) map[string]bool {
  if s == "" {
    return map[string]bool{s: true}
  }
  return generatePermutations([]rune(s))
}

func generatePermutations(runes []rune) map[string]bool {
  var (
    b               strings.Builder
    r               = runes[0]
    newPermutations map[string]bool
  )

  b.WriteRune(r)

  if len(runes) == 1 {
    newPermutations[b.String()] = true
    return newPermutations
  }

  for p, _ := range generatePermutations(runes[1:len(runes)]) {
    b.WriteString(p)
    newPermutations[b.String()] = true
  }

  return newPermutations
}
