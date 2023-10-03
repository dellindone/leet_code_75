# https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75
from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    n_list = len(flowerbed)
    count = 0
    for i in range(n_list):
        if(flowerbed[i] == 0):
            if(i == 0 or flowerbed[i-1] == 0):
                if(i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    count += 1
    return count >= n
             
flowerbed = [1,0,0,0,1]
n = 2
result = canPlaceFlowers(flowerbed, n)
print(result)