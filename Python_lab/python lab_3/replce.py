def replace(s, old, new):
    result = ''
    i = 0
    while i < len(s):
        if s[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += s[i]
            i += 1
    return result

s = "hello world, welcome to the world"
old = "world"
new = "universe"
result = replace(s, old, new)
print(result)
