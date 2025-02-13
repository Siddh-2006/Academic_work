import math
def main():
    T =  int(input("Enter the number of test cases: "))
    sqr = [];
    for i in range(T):
        A = int(input("Enter the lower bound: "))
        B = int(input("Enter the Upper bound: "))
        sqr.append(abs(int(math.sqrt(A)) - int(math.sqrt(B))))
    print(sqr)

if __name__ == "__main__":
    main()