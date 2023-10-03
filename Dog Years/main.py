# Calculate how old a dog is in dog years
import math

def main():
    print("This will calculate roughly the age of your dog. For fun.")
    age = input("Please insert your dogs age: ").strip()

    calculate_age(float(age))
    
def calculate_age(age):
    # Formula for calculating dogs age is 16ln(dog age) + 31
    human_years = int(16 * math.log(age) + 31)
    print(f"\nYour dogs age is roughly {human_years} in human years\n")
    print("This is based on research done by by a team lead by Tina Wang\nOf the University of California, San Diego")


if __name__ == '__main__':
    main()