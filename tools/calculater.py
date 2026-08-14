import math
from langchain.tools import tool


@tool
def calculate(expression: str) -> str:
    """
    Calculate mathematical expressions.

    Use this tool when the user asks for calculations,
    arithmetic, mathematical functions, square roots,
    logarithms, or trigonometric calculations.

    Input should be a valid mathematical expression,
    such as '25 * 4', 'sqrt(16)', or 'sin(pi / 2)'.
    """

    try:
        # Convert ln() to Python's log() function
        expression = expression.replace("ln(", "log(")

        # Allow only numbers, operators, letters, spaces, and brackets
        allowed_chars = set(
            "0123456789+-*/(). abcdefghijklmnopqrstuvwxyz"
        )

        # Check for unwanted characters
        if not set(expression.lower()).issubset(allowed_chars):
            return "Error: Unauthorized characters detected."

        # Define the math functions and constants allowed by the calculator
        safe_math_env = {
            "__builtins__": {},
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log,
            "log10": math.log10,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e,
        }

        # Evaluate the expression using only the allowed math functions
        result = eval(
            expression.lower(),
            safe_math_env,
            {}
        )

        return str(result)

    except Exception as e:
        # Return an error if the expression is invalid
        return f"Error: Invalid mathematical expression. {str(e)}"