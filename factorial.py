from pathlib import Path
import math 

l = 4 
def factorial(
    n: int) -> int        :
    if n <          2:
        return 1
    return           n * factorial(n - 1)

print(f"value is: {factorial(l)}")