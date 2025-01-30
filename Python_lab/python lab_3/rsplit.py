def R_split(string, delimiter=" ", maxsplit=-1):    
    result = []
    current = []
    count = 0
    
    for char in reversed(string):
        if char == delimiter and (maxsplit == -1 or count < maxsplit):
            result.append("".join(reversed(current)))
            current = []
            count += 1
        else:
            current.append(char)
    
    result.append("".join(reversed(current)))
    
    return list(reversed(result))

text = "This is an example string for rsplit"
parts = R_split(text, " ", 2)
print(parts)
