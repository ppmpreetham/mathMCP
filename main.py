from mcp.server.fastmcp import FastMCP, Context, Image

mcp = FastMCP()

# BASIC MATH OPERATIONS
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@mcp.tool()
def power(base: int, exponent: int) -> int:
    """Raise a number to a power."""
    return base ** exponent

@mcp.tool()
def factorial(n: int) -> int:
    """Calculate the factorial of a number."""
    if n < 0:
        raise ValueError("Cannot calculate factorial of a negative number.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

@mcp.tool()
def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number."""
    if n < 0:
        raise ValueError("Cannot calculate Fibonacci of a negative number.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

@mcp.tool()
def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor of two numbers."""
    while b:
        a, b = b, a % b
    return abs(a)

@mcp.tool()
def lcm(a: int, b: int) -> int:
    """Calculate the least common multiple of two numbers."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

@mcp.tool()
def prime(n: int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    mcp.run()
