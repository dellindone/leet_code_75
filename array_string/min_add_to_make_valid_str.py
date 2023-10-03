# https://leetcode.com/problems/minimum-additions-to-make-valid-string/description/

def addMinimum(word: str) -> int:
    insertion = 0
    count_a = count_b = count_c = 0

    for i in word:
        if i == 'a':
            if count_b == 0 and count_c == 0:
                insertion += 2
            elif count_b == 1:
                insertion += 2
            count_a = 1
            count_b = count_c = 0

        elif i == 'b':
            if count_a == 0 and count_c == 0:
                insertion += 2
            elif count_c == 0 and count_a == 1:
                insertion -= 1
                count_a = count_c = 0
            elif count_a == 1:
                insertion -= 1
            count_b = 1
            
        elif i == 'c':
            if count_a == 0 and count_b == 0:
                insertion += 2
            elif count_a == 1 and count_b == 1:
                insertion -= 1
            elif count_a == 1:
                insertion -= 1
            elif count_b == 1:
                insertion -= 1
            count_a = count_b = count_c = 0
    return insertion
    
word = 'abc'
# word = 'aaaaba'
result = addMinimum(word)
print(result)