A = int(input("Enter the number A :"))
B = int(input("Enter the number B :"))
max_XOR = 0;
for i in range(A,B+1):
    for j in range(A,B+1):
        if(max_XOR < (i^j)):
              max_XOR = i^j
print(max_XOR)