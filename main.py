inventory=[]
def insert_product():
    sku = input("Enter SKU: ")
    for item in inventory:
        if item['SKU'] == sku:
            print("Product with this SKU is already listed.")
            return
    name = input("Enter the name: ")
    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        return
    product = {'SKU': sku, 'Name': name, 'Quantity': quantity}
    inventory.append(product)
    print("Product added successfully.")
def search_product():
    query = input("Enter SKU or Name to search: ").strip().lower()
    found = False
    for item in inventory:
        if item['SKU'].lower() == query or item['Name'].lower() == query:
            print(f"Found: SKU: {item['SKU']}, Name: {item['Name']}, Quantity: {item['Quantity']}")
            found = True
    if not found:
        print("No product found with that SKU or Name.")
def insert_product_with_validation():
    sku = input("Enter SKU: ")
    for item in inventory:
        if item['SKU'] == sku:
            print("Product with this SKU is already listed.")
            return
    name = input("Enter the name: ").strip()
    if not name:
        print("Product name cannot be empty.")
        return
    try:
        quantity = int(input("Enter quantity: "))
        if quantity < 0:
            print("Quantity cannot be negative.")
            return
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        return
    product = {'SKU': sku, 'Name': name, 'Quantity': quantity}
    inventory.append(product)
    print("Product added successfully.")

def delete_product():
    sku = input("Enter SKU of the product to delete: ").strip()
    for i, item in enumerate(inventory):
        if item['SKU'] == sku:
            del inventory[i]
            print(f"Product with SKU {sku} deleted successfully.")
            return
    print(f"Product with SKU {sku} not found.")

def update_product():
    skus = input("Enter SKU(s) of the product(s) to update (separate multiple SKUs with commas): ")
    sku_list = [sku.strip() for sku in skus.split(',')]
    for sku in sku_list:
        found = False
        for item in inventory:
            if item['SKU'] == sku:
                found = True
                print(f"Current details for SKU {sku}: Name: {item['Name']}, Quantity: {item['Quantity']}")
                new_name = input(f"Enter new name for SKU {sku} (leave blank to keep current): ")
                if new_name:
                    item['Name'] = new_name
                try:
                    new_quantity = input(f"Enter new quantity for SKU {sku} (leave blank to keep current): ")
                    if new_quantity:
                        new_quantity_int = int(new_quantity)
                        if new_quantity_int < 0:
                            print("Quantity cannot be negative. Keeping current value.")
                        else:
                            item['Quantity'] = new_quantity_int
                except ValueError:
                    print("Invalid quantity. Keeping current value.")
                print(f"Product with SKU {sku} updated successfully.")
                break
        if not found:
            print(f"Product with SKU {sku} not found.")
def display_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("Current Inventory:")
    for item in inventory:
        print(f"SKU: {item['SKU']}, Name: {item['Name']}, Quantity: {item['Quantity']}")
    print()
def main():
    while True:
        print("\nInventory Stock Manager")
        print("1. Insert New Product")
        print("2. Display Inventory")
        print("3. Update Product Details")
        print("4. Search Product")
        print("5. Delete Product")
        print("6. Exit")
        choice = input("Enter your Choice: ")
        if choice == '1':
            insert_product()
        elif choice == '2':
            display_inventory()
        elif choice == '3':
            update_product()
        elif choice == '4':
            search_product()
        elif choice == '5':
            delete_product()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()