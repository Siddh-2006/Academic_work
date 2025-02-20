def next_lexicographic_permutation(w):
    chars = list(w)
    i = len(chars) - 2
    while i >= 0 and chars[i] >= chars[i + 1]:
        i -= 1

    if i == -1:
        return "No greater word possible"
    
    j = len(chars) - 1
    while chars[j] <= chars[i]:
        j -= 1
    chars[i], chars[j] = chars[j], chars[i]
    chars = chars[:i + 1] + chars[i + 1:][::-1]
    return ''.join(chars)

T = int(input("Enter number of test cases: "))
str_list = []
for _ in range(T):
    w = input("Enter a word: ")
    s = next_lexicographic_permutation(w)
    str_list.append(s)

print("The next lexicographically greater words are:")
for s in str_list:
    print(s)
