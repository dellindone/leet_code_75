# https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75



def reverseVowels(s: str) -> str:
    reverse = []
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in s:
        if i in vowels:
            reverse.append(i)
    reverse = reverse[::-1]

    count = 0
    s = list(s)
    for j in s:
        if j in vowels:
            s[count] = reverse[0]
            reverse = reverse[1:]
        count += 1
    return "".join(s)

s = "aA"
result = reverseVowels(s)
print(result)
