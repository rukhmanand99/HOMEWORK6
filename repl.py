import os
from dotenv import load_dotenv
from calc.commands.add_command import AddCommand
from calc.commands.subtract_command import SubtractCommand
from calc.commands.multiply_command import MultiplyCommand
from calc.commands.divide_command import DivideCommand
from logging_config import logger

# Load environment variables
load_dotenv()
ENVIRONMENT = os.getenv("ENVIRONMENT", "production")

commands = {
    "add": AddCommand(),
    "subtract": SubtractCommand(),
    "multiply": MultiplyCommand(),
    "divide": DivideCommand()
}

def repl():
    print(f"Calculator running in {ENVIRONMENT} mode.")
    while True:
        user_input = input(f"Enter command ({', '.join(commands.keys())}, quit): ").strip().lower()
        if user_input == "quit":
            print("Exiting...")
            break

        if user_input in commands:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = commands[user_input].execute(a, b)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter numbers.")
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    repl()
