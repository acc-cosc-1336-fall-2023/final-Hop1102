#add import
from question_c import validate_dna_string, validate_dna_substring, get_most_likely_ancestor_consensus

def main():
    while True:
        dna_string = input("Enter a DNA string(between 8 and 16 characters): ")
        if not validate_dna_string(dna_string):
            print("Invalid DNA string length. Please try again.")
            continue

        dna_substring = input("Enter a DNA substring(exactly 4 characters): ")

        if not validate_dna_substring(dna_substring):
            print("Invalid DNA substring length. Please try again.") 
            continue

        result_positions = get_most_likely_ancestor_consensus(dna_string, dna_substring)
        print(f"Result: {result_positions}")

        user_input = input("Do you want to continue? (yes/no): ").lower()
        if user_input != 'yes':
            print("Exiting program. Goodbye.")
            break 

if __name__ == "__main__":
    main()
