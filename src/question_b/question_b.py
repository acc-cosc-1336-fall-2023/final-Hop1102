#write functions here, don't add input('') statements here!
def create_multiplication_table(rows, cols):
    table = []
    for i in range (1, rows + 1):
        row = []
        for j in range(1, cols + 1):
            row.append(i + j)
        table.append(row)
    return table

def display_multiplication_table(table):
    for row in table:
        for value in row:
            print(f"{value:4}", end=" ")
        print()


        