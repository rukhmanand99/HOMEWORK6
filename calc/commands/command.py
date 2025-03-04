"""
Base class for all calculator commands.
"""

class Command:
    """Abstract base class for commands."""
    def execute(self, *args):
        raise NotImplementedError("Execute method must be implemented.")
