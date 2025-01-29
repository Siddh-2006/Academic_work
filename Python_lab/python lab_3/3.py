T = int(input("Enter how many numbers you want to enter: "))
count = []

for _ in range(T):
    N = list(input("Enter any number: "))
    N_number = int(''.join(map(str, N)))
    count.append(0)
    for digit in N:
        if int(digit) != 0 and N_number % int(digit) == 0:
            count[-1] += 1

for c in count:
    print(c)
