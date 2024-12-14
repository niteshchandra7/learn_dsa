from typing import List, Dict
import time
# sumArr - Camel Casing
# sum_arr - snake casing, python way of doing things
# SumArr - pascal casing
def sum_arr(arr:List[int]):
    sum:int = 0
    # size of arr  = N
    for elem in arr: # N
        sum += elem # O(1)
    return sum

# TC: N * O(1) = O(N)

# 1 second - 10^9 operation
# 10^9 operations - 1 second
# 1 operation - 10 ^(-9)
# Can I have size of arr as 10^(6)?
# 10^6 * 10^(-9)  - 1ms
# Can I have size of arr as 10^(15)?
# 10^15 * 10^(-9) = 10^(6) seconds = 11.5 days
# O(1) - 1ns
# binary operation ,arithmetic operation is fastest - O(1) 
# 1 +1 , 1000000000 + 1999999999
# 000000000..........1 + 0000000000000........1
# 00001000000001000..0 + 1000100000000........1
# CPU has ALU (Arithmetic and logic unit)
# arithmetic and logic operation will take constant time and it doesn't depend on how big the input is given

if __name__ == "__main__":
    start_time = time.time()
    arr:List[int] = list(range(0,100000000,1))
    print(sum_arr(arr))
    end_time = time.time()
    print(f"time taken: {end_time-start_time}")
    