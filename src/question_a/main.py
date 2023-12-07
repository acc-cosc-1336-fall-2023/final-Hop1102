#add import

#from question_a import get_stock_list
#from question_a import display_stock_list
#keep getting an import error even though its all spelled right and defined so i put it all in main to work. 
class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol 
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self): 
        return self.__company_name 
    
stock_data = [
    ('AAPL', 'Apple Inc'),
    ('CAT', 'Caterpillar'),
    ('EK', 'Eastman Kodak'),
    ('GOOG', 'Google'),
    ('MSFT', 'Microsoft')
]

def get_stock_list():
        stock_list = {}
        for symbol, company_name in stock_data:
             stock_list[symbol] = Stock(symbol, company_name)
        return stock_list 

def display_stock_list(stock_list):
        for symbol, stock in stock_list.items():
            print(f"Company: {stock.get_company_name()}, Symbol: {stock.get_symbol()}")

def main():
    while True:
        print("Main Menu:")
        print("1- Display stock purchase history")
        print("2- Exit")

        choice = input("Enter your choice(1/2):")

        if choice == "1":
            display_stock_list(get_stock_list())
        elif choice == "2":
            print("Exiting program. Bye")
            break
        else:
            print("Invalid entry. Please put 1 or 2.") 

if __name__ == "__main__":
    main() 