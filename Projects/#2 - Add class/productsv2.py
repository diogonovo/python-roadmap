#Second version, added classes
# Class Product 
class Product:
    def __init__(self, name, price, quantity, description):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    def __str__(self):
        return f"{self.name} (Price: {self.price}, Quantity: {self.quantity}, Description: {self.description})"

# Class Marketplace 
class Marketplace:
    def __init__(self):
        self.products = [] 

    def add_product(self, product):
        self.products.append(product)
        print(f"Product {product.name} added successfully!")

    def remove_product(self, name):
        self.products = [product for product in self.products if product.name != name]
        print(f"Product {name} removed successfully!")

    def list_products(self):
        if not self.products:
            print("No products in stock.")
        else:
            print("Product stock:")
            for product in self.products:
                print(product)


def main():
    marketplace = Marketplace()

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
            product = Product(name, price, quantity, description)
            marketplace.add_product(product) 

        elif opcao == "2":
            name = input("Product name to remove: ")
            marketplace.remove_product(name)

        elif opcao == "3":
            marketplace.list_products()

        elif opcao == "4":
            print("Exiting...")
            break

        else:
            print("Invalid option! Try again.")

# Exec
if __name__ == "__main__":
    main()
