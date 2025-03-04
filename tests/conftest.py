"""
Pytest fixture configuration for calculator commands.
"""

import pytest
from calc.commands.add_command import AddCommand
from calc.commands.subtract_command import SubtractCommand
from calc.commands.multiply_command import MultiplyCommand
from calc.commands.divide_command import DivideCommand

@pytest.fixture
def add_command():
    """Fixture for AddCommand instance"""
    return AddCommand()

@pytest.fixture
def subtract_command():
    """Fixture for SubtractCommand instance"""
    return SubtractCommand()

@pytest.fixture
def multiply_command():
    """Fixture for MultiplyCommand instance"""
    return MultiplyCommand()

@pytest.fixture
def divide_command():
    """Fixture for DivideCommand instance"""
    return DivideCommand()
