def operation(str):
    num = 0
    n = len(str)
    for i in range(n // 2):
        if i == n-i-1:
            return num
        num += abs(ord(str[i]) - ord(str[n - i - 1]))
    return num


def main():
    NumWords = int(input("Enter the number of string ,you will enter: "))
    TotalOperation = []
    Words = []
    for i in range(NumWords):
        Words.append(input(""))
        TotalOperation.append(operation(list(Words[i])))
    print("Required Operation is ",TotalOperation)

if __name__ == "__main__":
    main()

