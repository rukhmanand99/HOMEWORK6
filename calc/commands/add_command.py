from calc.commands.command import Command
from logging_config import logger

class AddCommand(Command):
    def execute(self, a, b):
        result = a + b
        logger.info(f"Adding {a} + {b} = {result}")
        return result
