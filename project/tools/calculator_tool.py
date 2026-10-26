class CalculatorTool:
    """A simple calculator tool with explicit schema."""

    schema = {
        "name": "calculator",
        "description": "Perform basic arithmetic operations for study metrics",
        "parameters": {
            "operation": {"type": "string", "enum": ["add", "subtract", "multiply", "divide"]},
            "a": {"type": "number"},
            "b": {"type": "number"}
        },
        "returns": {"type": "number"}
    }

    def calculate(self, operation, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("a and b must be numbers")
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return a / b
        else:
            raise ValueError("Unknown operation: " + str(operation))