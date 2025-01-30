def main():
    n = int(input("How many test cases you want :"))
    Utree_data = []
    for _ in range(n):
        Utree_input = int(input("Enter the test case value: "))
        Utree_output = Utree(Utree_input)
        Utree_data.append(Utree_output)
    for output in Utree_data:
        print(output)

def Utree(n):
    i = 1
    for j in range(n):
        if j % 2 == 0:
            i *= 2
        else:
            i += 1
    return i

if __name__ == "__main__":
    main()

