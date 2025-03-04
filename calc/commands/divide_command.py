from calc.commands.command import Command
from logging_config import logger

class DivideCommand(Command):
    def execute(self, a, b):
        if b == 0:
            logger.error("Division by zero attempted.")
            return "Error: Division by zero"
        result = a / b
        logger.info(f"Dividing {a} / {b} = {result}")
        return result
