import product
def main():
    
    def make_list():
        product_list = []
        print("Enter data for 3 products:")
        for count in range(1,4):
            name = input("Enter the name of product " + str(count) + ": ")
            price = float(input("Enter the price of product " + str(count) + ": "))

            cProduct = product.Product(name, price)

            product_list.append(cProduct)

        return product_list

    def display_list(product_list):
        for item in product_list:
            print("{} price = {} total price with tax for {} is {}".format(item.getProductName(), item.getProductPrice(), item.getProductName(), format(item.getTotalPrice(),'.2f')))

    
    def grandTotal(product_list):
        total = 0
        for item in product_list:
            total += item.getTotalPrice()
        print("Total: ", format(total, '.2f'))
    
    
    pro_list = make_list()
    print(pro_list)
    #display_list(pro_list)
    display_list(pro_list)
    grandTotal(pro_list)
main()