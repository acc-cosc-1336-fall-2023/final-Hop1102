#add import
#from question_d import stock_purchase_history
#for some reason its not letting me import so I will put the class and def's in main. 

class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name
    
def stock_purchase_history():
        stock_dict = {
            'AAPL' : Stock('AAPL', 'Apple Inc.'),
            'CAT' : Stock('CAT', 'Caterpillar'),
            'EK' : Stock('EK', 'Eastman Kodak'), 
            'GOOG' : Stock('GOOG', 'Google'),
            'MSFT': Stock('MSFT', 'Microsoft')
        }

        print("Stock Purchase History:")
        print("symbol Company Name")
        for symbol, stock in stock_dict.items():
            print(f"{symbol}    {stock.get_company_name()}")

def main():
    while True:
        print("Main Menu:")
        print("1) Display stock purchase history")
        print("2) Exit")

        choice = input("Enter your choice(1/2): ")

        if choice == '1':
            stock_purchase_history()
        elif choice == '2':
            print("exiting program. Bye.")
            break 
        else:
            print("Invalid entry. Please put 1 or 2.")

if __name__ == "__main__":
    main()          
        