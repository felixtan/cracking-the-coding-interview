package permutation

import (
  "testing"
)

func TestCopyRuneFreqMap(t *testing.T) {
  t.Log("Copy of a string...")
  var (
    str     = "qwerty"
    copy    = "qwerty"
  )

  if !IsPermutationRuneFreqMap(str, copy) {
    t.Error("Expected true, but got false")
  }
}

func TestReverseRuneFreqMap(t *testing.T) {
  t.Log("Reverse of a string...")

  var (
    str     = "qwerty"
    reverse = "ytrewq"
  )

  if !IsPermutationRuneFreqMap(str, reverse) {
    t.Error("Expected true, but got false")
  }
}

func TestRepeatingCharsRuneFreqMap(t *testing.T) {
  t.Log("String with repeating chars...")

  var (
    str   = "abbcccdddd"
    test  = Shuffle(str)
  )

  if !IsPermutationRuneFreqMap(str, test) {
    t.Error("Expected true, but got false")
  }
}

func TestWhitespaceRuneFreqMap(t *testing.T) {
  t.Log("String with whitespace chars...")

  var (
    str   = "  \ba\tb\nc\vd\fe\r"
    test  = Shuffle(str)
  )

  if !IsPermutationRuneFreqMap(str, test) {
    t.Error("Expected true, but got false")
  }
}

func TestNonAsciiRuneFreqMap(t *testing.T) {
  t.Log("String with non-ascii chars...")

  var (
    str  = "零一二三四五六七八九"
    test = Shuffle(str)
  )

  if !IsPermutationRuneFreqMap(str, test) {
    t.Error("Expected true, but got false")
  }
}

func TestNotPermutationRuneFreqMap(t *testing.T) {
  t.Log("String that's not a permutation...")

  var (
    str  = "qwerty"
    test = "qwerti"
  )

  if IsPermutationRuneFreqMap(str, test) {
    t.Error("Expected false, but got true")
  }
}
