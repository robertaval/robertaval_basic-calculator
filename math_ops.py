def add(a, b):
    return f"{a} + {b} = {a + b}"

def sub(a, b):
    return f"{a} - {b} = {a - b}"

def mul(a, b):
    return f"{a} * {b} = {a * b}"

def div(a, b):
    if b != 0:
        return f"{a} / {b} = {a / b}"
    return "Cannot divide by zero."

operations = {
    "add": {"label": "Addition", "func": add},
    "sub": {"label": "Subtraction", "func": sub},
    "mul": {"label": "Multiplication", "func": mul},
    "div": {"label": "Division", "func": div},
}
