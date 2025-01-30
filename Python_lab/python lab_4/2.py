def isfibo(n, b, c):
    if c == n:
        return True
    elif c > n:
        return False
    else:
        d = b + c
        return isfibo(n, c, d)

def main():
    fibo = []
    n = int(input("How many numbers do you want to enter: "))
    for i in range(n):
        num = int(input(""))
        if isfibo(num, 0, 1):
            fibo.append(1)
        else:
            fibo.append(0)
    print(fibo)
    for i in range(n):
        if fibo[i]:
            print("isfibo")
        else:
            print("isnotfibo")

if __name__ == "__main__":
    main()
