str = list(input("enter any string : "))
for i in range(1,len(str),2):
    str[i] = str[i].upper()
new_str = ''.join(str)
print(new_str)