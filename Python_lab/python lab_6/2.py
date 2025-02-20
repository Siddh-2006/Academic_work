T  = int (input("Enter a number of test cases"));
max_cuts = [];
for i in range(T):
    cuts = int(input(""))
    if(cuts%2 == 0):
        max_cuts.append((cuts//2)**2)
    else:
        max_cuts.append((cuts//2)*((cuts//2)+1))
print(max_cuts)