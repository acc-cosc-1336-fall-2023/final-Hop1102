#add import

from question_b import display_multiplication_table, create_multiplication_table

def main():
    while True:
        print("Main menu:")
        print("1) Generate/display multiplication table")
        print("2) Quit")

        choice = input("Enter your choice(1/2): ")

        if choice == "1":
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: ")) 

            multiplication_table = create_multiplication_table(rows, cols)
            display_multiplication_table(multiplication_table)

        elif choice == "2":
            print("Exiting program. Goodbye.") 
            break 
        else:
            print("Invalid response. please put 1 or 2.") 

if __name__ == "__main__":
    main() 
            


        
    