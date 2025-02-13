def main():
    str = list(input(""))
    hash_list = {i:0 for i in range(97,124)}
    for i in str:
        hash_list[ord(i)] = 1

    for i in range(97,123):
        if hash_list[i] == 0:
            print("not pangram")
            return 0
    
    print("Pangram")

if __name__ == "__main__":
    main()