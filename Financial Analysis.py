class Evaluation:
    def __init__(self):
        self.series_of_questions = {
            "Housing": "How much do you spend on housing each month? (rent/mortgage)",
            "Utilities": "How much do you spend on utilities each month? (electricity, water, gas)",
            "Groceries": "How much do you spend on groceries each month?",
            "Transportation": "How much do you spend on transportation each month? (car payments, public transit)",
            "Insurance": "How much do you spend on insurance each month? (health, car, home)",
            "Healthcare": "How much do you spend on healthcare each month? (medications, doctor visits)",
            "Entertainment": "How much do you spend on entertainment each month? (movies, dining out, hobbies)",
            "Savings": "How much do you save each month?",
            "Debts": "How much do you spend on paying off debts each month? (credit card, student loan)",
            "Miscellaneous": "How much do you spend on miscellaneous items each month?"
        }
        self.start()

    def start(self):
        user_input = input("Hello, welcome to The Finance Evaluation program. Type 'Begin' to start: ")
        if user_input.lower() == 'begin':
            self.evaluate_finances()
        else:
            print("Exiting program. Please type 'Begin' to start the evaluation.")

    def evaluate_finances(self):
        for key in self.series_of_questions.keys():
            while True:
                response = input(f"{self.series_of_questions[key]} ")
                confirm = input(f"You entered '{response}' for {key}. Is this correct? (yes/edit) ").lower()
                if confirm == 'yes':
                    try:
                        self.series_of_questions[key] = float(response)
                        break
                    except ValueError:
                        print("Invalid entry. Please enter a numeric value.")
                elif confirm == 'edit':
                    continue
                else:
                    print("Please enter 'yes' or 'edit'.")

        while True:
            print(f"Your answer choices are as follows: {self.series_of_questions}. Are these correct? (yes/no)")
            final_answer = input().lower()

            if final_answer == "no":
                print("Let's revise your answers.")
                return self.evaluate_finances()  # Start the process over again
            elif final_answer == "yes":
                print("Let's Proceed")
                self.visionary()
                self.percent()
                break
            else:
                print("Please enter 'yes' or 'no'.")

    def visionary(self):
        total_spending_this_month = sum(self.series_of_questions.values())
        print(f"You have spent a total amount of ${total_spending_this_month:.2f} this month.")

        predicted_three_months = total_spending_this_month * 3
        print(f"Predicted total for the next three months: ${predicted_three_months:.2f}")

    def percent(self):
        total_spending_this_month = sum(self.series_of_questions.values())
        print(f"Since you have spent a total amount of ${total_spending_this_month:.2f}, here are your expense categories in percentages:\n")
        for key, value in self.series_of_questions.items():
            percentage = (value / total_spending_this_month) * 100
            print(f"{key}: {percentage:.2f}%")
Evaluation()