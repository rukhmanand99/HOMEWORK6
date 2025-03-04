"""
Unit tests for the calculator commands.
"""
import pytest
from calc.commands.command import Command
from calc.commands.add_command import AddCommand
from calc.commands.subtract_command import SubtractCommand
from calc.commands.multiply_command import MultiplyCommand
from calc.commands.divide_command import DivideCommand

def test_add():
    """Test addition operation"""
    assert AddCommand().execute(2, 3) == 5

def test_subtract():
    """Test subtraction operation"""
    assert SubtractCommand().execute(10, 5) == 5

def test_multiply():
    """Test multiplication operation"""
    assert MultiplyCommand().execute(4, 3) == 12

def test_divide():
    """Test division operation"""
    assert DivideCommand().execute(10, 2) == 5

def test_divide_by_zero():
    """Test division by zero handling"""
    assert DivideCommand().execute(10, 0) == "Error: Division by zero"
def test_command_abstract():
    """Ensure Command's execute method raises NotImplementedError"""
    cmd = Command()
    with pytest.raises(NotImplementedError):
        cmd.execute()
