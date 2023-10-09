import csv
def load_actuarial_table(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        table = list(reader)
    return table

def calculate_life_expectancy(age, gender, table):
    for row in table:
        if int(row['Age']) == age:
            if gender == 'Male':
                return float(row['Male'])
            else:
                return float(row['Female'])
            return None
def main():
    filename = "Life Expectancy Male and Female 30 - 100.csv"  # Replace with your CSV filename
    table = load_actuarial_table(filename)

    age = int(input("Enter age: "))
    gender = input("Enter sex at birth (Male/Female): ").capitalize()

    life_expectancy = calculate_life_expectancy(age, gender, table)

    if life_expectancy is not None:
        print(f"Estimated life expectancy for a {gender} of age {age} is {life_expectancy} years.")
    else:
        print("Data not available for the given input.")


if __name__ == "__main__":
    main()