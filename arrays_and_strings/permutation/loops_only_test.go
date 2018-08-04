package permutation

import (
  "testing"
)

func TestCopyLoopsOnly(t *testing.T) {
  t.Log("Copy of a string...")
  var (
    str     = "qwerty"
    copy    = "qwerty"
  )

  if !IsPermutationLoopsOnly(str, copy) {
    t.Error("Expected true, but got false")
  }
}

func TestReverseLoopsOnly(t *testing.T) {
  t.Log("Reverse of a string...")

  var (
    str     = "qwerty"
    reverse = "ytrewq"
  )

  if !IsPermutationLoopsOnly(str, reverse) {
    t.Error("Expected true, but got false")
  }
}

func TestRepeatingCharsLoopsOnly(t *testing.T) {
  t.Log("String with repeating chars...")

  var (
    str   = "abbcccdddd"
    test  = Shuffle(str)
  )

  if !IsPermutationLoopsOnly(str, test) {
    t.Error("Expected true, but got false")
  }
}

func TestWhitespaceLoopsOnly(t *testing.T) {
  t.Log("String with whitespace chars...")

  var (
    str   = "  \ba\tb\nc\vd\fe\r"
    test  = Shuffle(str)
  )

  if !IsPermutationLoopsOnly(str, test) {
    t.Error("Expected true, but got false")
  }
}

func TestNonAsciiLoopsOnly(t *testing.T) {
  t.Log("String with non-ascii chars...")

  var (
    str  = "零一二三四五六七八九"
    test = Shuffle(str)
  )

  if !IsPermutationLoopsOnly(str, test) {
    t.Error("Expected true, but got false")
  }
}

func TestNotPermutationLoopsOnly(t *testing.T) {
  t.Log("String that's not a permutation...")

  var (
    str  = "qwerty"
    test = "qwerti"
  )

  if IsPermutationLoopsOnly(str, test) {
    t.Error("Expected false, but got true")
  }
}
