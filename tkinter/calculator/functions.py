import tkinter as tk
import math

# This module stores the current expression and offers helpers
_expression = ""


def _update_display(display: tk.Entry, text: str) -> None:
    """Replace everything now showing in the entry widget."""
    display.delete(0, tk.END)
    display.insert(tk.END, text)


def press(value: str, display: tk.Entry) -> None:
    """Append a digit or operator to the running expression."""
    global _expression
    _expression += str(value)
    _update_display(display, _expression)


def clear(display: tk.Entry) -> None:
    """Clear everything."""
    global _expression
    _expression = ""
    _update_display(display, "")


def equal(display: tk.Entry) -> None:
    """Evaluate the current expression."""
    global _expression
    try:
        result = str(eval(_expression))
        _expression = result            # let users continue calculating
        _update_display(display, result)
    except Exception:
        _update_display(display, "Error")
        _expression = ""


def sqrt(display: tk.Entry) -> None:
    """Square-root of the current value/expression."""
    global _expression
    try:
        result = math.sqrt(float(eval(_expression)))
        _expression = str(result)
        _update_display(display, _expression)
    except Exception:
        _update_display(display, "Error")
        _expression = ""

        
def backspace(display: tk.Entry) -> None:
    """Remove the last character from the expression."""
    global _expression
    _expression = _expression[:-1]  # remove last character
    _update_display(display, _expression)

