# https://leetcode.com/contest/weekly-contest-291/problems/remove-digit-from-number-to-maximize-result/

def remove_ith_occurrence(input_str: str, char_to_remove: int, i: int) -> int:
    count = 0
    result = ""
    for char in input_str:
        count += 1
        if char == char_to_remove:
            if count == i:
                continue  # Skip this occurrence
        result += char
    return result

def removeDigit(number: str, digit: str) -> str:
    result = []
    number_list = list(number)
    
    for i in range(0, len(number_list)):
        dup = number
        if(number_list[i] == digit):
            res = remove_ith_occurrence(dup, digit,i+1)
            result.append(res)
    return max(result)

number = "1231"
digit = "1"

result = removeDigit(number, digit)
print(result)