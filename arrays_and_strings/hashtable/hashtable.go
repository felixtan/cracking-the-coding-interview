package hashtable

import (
  "fmt"
  "errors"
  "hash/adler32"
  "container/list"
)

func main() {
  var (
    i int
    v interface{}
    myTable = *NewHashTable()
  )

  i = myTable.Insert("foo", "one")
  fmt.Printf("foo inserted at %d\n", i)
  v, _ = myTable.Get("foo")
  fmt.Println(v)
  fmt.Println(myTable.Len())

  myTable.Insert("bar", "two")
  fmt.Printf("bar inserted at %d\n", i)
  v, _ = myTable.Get("bar")
  fmt.Println(v)
  fmt.Println(myTable.Len())

  myTable.Delete("bar")
  fmt.Println(myTable.Len())
}

type HashTable struct {
  slice []*list.List
}

func NewHashTable() *HashTable {
  ht := &HashTable{}
  ht.slice = make([]*list.List, 0, 1)
  return ht
}

func (ht *HashTable) Insert(key string, value interface{}) int {
  var (
    hash  = getHash(key)
    index = mapHashToIndex(hash, ht.slice)
    ll    *list.List
    node  = make(map[string]interface{})
  )

  node["key"] = key
  node["value"] = value

  if len(ht.slice) == index {
    // there is no ll at index, create a new one
    ll = list.New()
    ht.slice = append(ht.slice, ll)
  } else {
    ll = ht.slice[index]
  }

  fmt.Printf("hash of key %s is %d\n", key, hash)
  fmt.Printf("inserting %s into ll and index %d\n", key, index)
  ll.PushBack(node)

  return index
}

func (ht *HashTable) Get(key string) (interface{}, error) {
  var (
    hash  = getHash(key)
    index = mapHashToIndex(hash, ht.slice)
    ll    = ht.slice[index]   // todo: check if this index is nil?
  )

  for n := ll.Front(); n != nil; n = n.Next() {
    // have to assert the type of list.Element.Value which has interface{} type
    node := n.Value.(map[string]interface{})

    if node["key"] == key {
      return node["value"], nil
    }
  }

  return nil, errors.New("KeyError")
}

func (ht* HashTable) Delete(key string) (interface{}, error) {
  var (
    hash  = getHash(key)
    index = mapHashToIndex(hash, ht.slice)
    ll    = ht.slice[index]
  )

  for n := ll.Front(); n != nil; n = n.Next() {
    // have to assert the type of list.Element.Value which has interface{} type
    node := n.Value.(map[string]interface{})

    if node["key"] == key {
      return ll.Remove(n), nil
    }
  }

  return nil, errors.New("KeyError")
}

func (ht *HashTable) Len() (uint) {
  len := 0
  // fmt.Println(len(ht.slice))
  for i, ll := range ht.slice {
    fmt.Printf("i: %d, val: %v\n", i, ll)
    if ll != nil {
      len += 1
    }
  }
  return uint(len)
}

// map hash code to slice index
func mapHashToIndex(hash uint32, arr []*list.List) int {
  return int(hash) % cap(arr)
}

// return int hash given string
// uses adler32 which returns uint32
func getHash(key string) uint32 {
  return adler32.Checksum([]byte(key))
}
