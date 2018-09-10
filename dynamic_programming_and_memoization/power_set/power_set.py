import sys

# O(2^n)
# The power set P(S) of a set S contains the 2^n subsets of S
def generate_subsets(S):
    # Maintain cache to prevent repeated calls
    # The null set is a subset of any set
    # and any set is subset of itself, so init the cache
    # with these
    cache = {
        frozenset(): True, 
        frozenset(S): True
    }

    def generate(A, B):
        for v in A:
            if len(A) >= 1:
                _A, _B = A.copy(), B.copy()
                _A.remove(v)
                _B.append(v)
            
            if len(_B) >= 1:
                subset = frozenset(_B)

                if subset not in cache:
                    cache[subset] = True

                    # avoid last level of calls in the tree
                    if len(_A) > 1:
                        generate(_A, _B)
            
    generate(S, [])

    return set(cache.keys())

if __name__ == '__main__':
    P = generate_subsets(sys.argv[1:])
    for s in P:
        print(s)
