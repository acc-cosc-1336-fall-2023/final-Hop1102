#write functions here, don't add input('') statements here!

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

            