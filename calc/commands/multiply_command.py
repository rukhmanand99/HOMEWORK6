from calc.commands.command import Command
from logging_config import logger

class MultiplyCommand(Command):
    def execute(self, a, b):
        result = a * b
        logger.info(f"Multiplying {a} * {b} = {result}")
        return result
