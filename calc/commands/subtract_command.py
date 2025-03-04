from calc.commands.command import Command
from logging_config import logger

class SubtractCommand(Command):
    def execute(self, a, b):
        result = a - b
        logger.info(f"Subtracting {a} - {b} = {result}")
        return result
