# https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75

word1 = "abc"
word2 = "pq"

def merge_string_alternatively(word1, word2):
    n1 = len(word1)
    n2 = len(word2)
    n = min(n1,n2)
    result = ''
    for i in range(0,n):
        result+= word1[i]+word2[i]
    
    if(n1 == n2):
        return result
    elif(n1 > n2):
        return result+word1[n:]
    else:
        return result+word2[n:]

result = merge_string_alternatively(word1, word2)
print(result)