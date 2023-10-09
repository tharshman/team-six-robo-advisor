from models import UserInfo


class LifeExpectancyCalculator:
    def __init__(self, user_info: UserInfo):
        self._expectancy = int()
        self._user_info = user_info

    def add_expectancies(self, age, sex, age_of_retirement):
        expectancies = UserInfo(age, sex, age_of_retirement)
        self._expectancy.append(expectancies)

    def calculate_for_user(self) -> UserInfo:
            for row in table:
                if int(row['Age']) == age:
                    if gender == 'Male':
                        return float(row['Male'])
                    else:
                        return float(row['Female'])
            return self._user_info

    def load_actuary_data(self):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            table = list(reader)
        return table
        
    def main():
        filename = "Life Expectancy Male and Female 30 - 100.csv"
        table = load_actuary_data(filename)

        age = int(input("Enter age: "))
        gender = input("Enter sex at birth (Male/Female): ").capitalize()

        life_expectancy = calculate_for_user(age, gender, table)

        if life_expectancy is not None:
            print(f"Estimated life expectancy for a {gender} of age {age} is {life_expectancy} years.")
        else:
            print("Data not available for the given input.")

    if __name__ == "__main__":
        main()
