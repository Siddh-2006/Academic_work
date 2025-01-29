n = int(input ("How many product want to insert:"))
product_name = [input(f"Enter {i+1}th product name: ") for i in range(n)]
price = [(input(f"Enter price of {product_name[i]} : ")) for i in range(n)]
products = dict(zip(product_name,price))
print("For STOP shutdown the terminal")
while(1):
    value = products.get(input("enter the product name: "),'None')
    if value == 'None':
        print("There is no such product stored")
    else:
        print("price:", value)