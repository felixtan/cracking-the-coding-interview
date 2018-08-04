package permutation

import (
  "testing"
)

func TestEmptyString(t *testing.T) {
  t.Log("Empty string...")

  var (
    str     = ""
    perms   = GeneratePermutations(str)
    prs     = perms[str]
    length  = len(perms)
  )

  if length != 1 {
    t.Errorf("Expected length 1, but got %d\n", length)
  }

  if !prs {
    t.Error("Expected true, but false")
  }
}

func TestAsciiString(t *testing.T) {
  t.Log("Ascii string...")

  var (
    str      = "abcd"
    perms    = GeneratePermutations(str)
  )

  // expected := map[string]bool{
  //   "abcd": true, "bacd": true, "cabd": true, "dabc": true,
  //   "abdc": true, "badc": true, "cadb": true, "dacb": true,
  //   "acbd": true, "bcad": true, "cbad": true, "dbac": true,
  //   "acdb": true, "bcda": true, "cbda": true, "dbca": true,
  //   "adbc": true, "bdac": true, "cdab": true, "dcab": true,
  //   "adcb": true, "bdca": true, "cdba": true, "dcba": true,
  // }
  expected := make(map[string]bool)

  expected["abcd"] = true
  expected["bacd"] = true
  expected["cabd"] = true
  expected["dabc"] = true
  expected["abdc"] = true
  expected["badc"] = true
  expected["cadb"] = true
  expected["dacb"] = true
  expected["acbd"] = true
  expected["bcad"] = true
  expected["cbad"] = true
  expected["dbac"] = true
  expected["acdb"] = true
  expected["bcda"] = true
  expected["cbda"] = true
  expected["dbca"] = true
  expected["adbc"] = true
  expected["bdac"] = true
  expected["cdab"] = true
  expected["dcab"] = true
  expected["adcb"] = true
  expected["bdca"] = true
  expected["cdba"] = true
  expected["dcba"] = true

  for p, _ := range expected {
    _, prs := perms[p]
    if !prs {
      t.Errorf("Expected permutation %s\n", p)
    }
  }
}
