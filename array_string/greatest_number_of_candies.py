# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

def kidsWithCandies( candies: List[int], extraCandies: int) -> List[bool]:
    max_number = max(candies)
    print(max_number)
    bool_list = []
    for i in candies:
        number = extraCandies + i
        if(number >= max_number):
            bool_list.append(True)
            continue
        bool_list.append(False)
        number = 0
    return bool_list

candies = [2,3,5,1,3]
extraCandies = 3
result = kidsWithCandies(candies, extraCandies)
print(result)
