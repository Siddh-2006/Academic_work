def digital_root(n):
    while len(str(n)) > 1:
        n = int(sum(int(digit) for digit in str(n)))
        return digital_root(n)
    return n

def main():
    n = input("Enter any number for getting digital root: ")
    print(f"Digital root of {n} is: {digital_root(n)}")

if __name__ == '__main__':
    main()
