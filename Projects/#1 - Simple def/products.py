#First simple program
# List products
products = []

# Function to add products
def add_products(name, price, quantity, description):
    product = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "description": description,
    }
    products.append(product)
    print(f"product {name} sucessfully added!")

# Function to remove products 
def remover_product(name):
    global products
    products = [product for product in products if product["name"] != name]
    print(f"product {name} sucessfully removed!")

# Function to list products
def listar_products():
    if not products:
        print("No product in stock.")
    else:
        print("Product stock:")
        for product in products:
            print(f"- {product['name']} (Price: {product['price']}, quantity: {product['quantity']}), description: {product['description']}")

# Main function
def main():
    while True:
        print("\n1. Add product")
        print("2. Remove product")
        print("3. List products")
        print("4. Exit")
        
        opcao = input("Choose an option: ")

        if opcao == "1":
            name = input("Product name: ")
            price = float(input("Product price: "))
            quantity = int(input("Stock: "))
            description = input('Description: ')
            add_products(name, price, quantity, description)

        elif opcao == "2":
            name = input("Product name to remove: ")
            remover_product(name)

        elif opcao == "3":
            listar_products()

        elif opcao == "4":
            print("Leaving...")
            break

        else:
            print("Invalid option! Try again.")

# Exec
if __name__ == "__main__":
    main()
