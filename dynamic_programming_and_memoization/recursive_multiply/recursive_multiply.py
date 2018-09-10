# O(min(a, b))
def multiply(a, b):
    negative = (a < 0) ^ (b < 0)
    
    a, b = abs(a), abs(b)

    def _multiply(a, b):
        if a < b:
            a, b = b, a

        if b == 0:
            return 0
        
        if b == 1:
            return a

        if b > 1:
            return a + _multiply(a, b - 1)
    
    abs_val = _multiply(a, b)
    
    return 0 - abs_val if negative else abs_val