from mcp.server.fastmcp import FastMCP, Context
import math

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

# MATH MODULE ITSELF
# Constants (No Parameters)
constants = ["e", "inf", "nan", "pi", "tau"]
    
# Single-Parameter Functions (f(x))
single_param = [
    "acos", "acosh", "asin", "asinh", "atan", "atanh", "cbrt", "ceil", "cos",
    "cosh", "degrees", "erf", "erfc", "exp", "exp2", "expm1", "fabs", "factorial",
    "floor", "frexp", "gamma", "isfinite", "isinf", "isnan", "isqrt", "lgamma",
    "log", "log10", "log1p", "log2", "modf", "radians", "sin", "sinh", "sqrt",
    "tan", "tanh", "trunc", "ulp"
]

# Two-Parameter Functions (f(x, y))
two_param = [
    "atan2", "copysign", "fmod", "gcd", "hypot", "isclose", "lcm",
    "ldexp", "nextafter", "pow", "remainder"
]

# Multiple-Parameter Functions (f(*args))
multi_param = [
    "comb", "dist", "fsum", "prod", "perm", "sumprod"
]

# Constants (No Parameters)
@mcp.tool()
def e() -> float:
    """Return Euler's number."""
    return math.e

@mcp.tool()
def inf() -> float:
    """Return positive infinity."""
    return math.inf

@mcp.tool()
def nan() -> float:
    """Return NaN (Not a Number)."""
    return math.nan

@mcp.tool()
def pi() -> float:
    """Return the mathematical constant π."""
    return math.pi

@mcp.tool()
def tau() -> float:
    """Return the mathematical constant τ."""
    return math.tau


# Single-Parameter Functions (f(x))
@mcp.tool()
def acos(x: float) -> float:
    """Compute the arc cosine of x."""
    return math.acos(x)

@mcp.tool()
def acosh(x: float) -> float:
    """Compute the inverse hyperbolic cosine of x."""
    return math.acosh(x)

@mcp.tool()
def asin(x: float) -> float:
    """Compute the arc sine of x."""
    return math.asin(x)

@mcp.tool()
def asinh(x: float) -> float:
    """Compute the inverse hyperbolic sine of x."""
    return math.asinh(x)

@mcp.tool()
def atan(x: float) -> float:
    """Compute the arc tangent of x."""
    return math.atan(x)

@mcp.tool()
def atanh(x: float) -> float:
    """Compute the inverse hyperbolic tangent of x."""
    return math.atanh(x)

@mcp.tool()
def cbrt(x: float) -> float:
    """Compute the cube root of x."""
    return math.cbrt(x)

@mcp.tool()
def ceil(x: float) -> int:
    """Return the ceiling of x."""
    return math.ceil(x)

@mcp.tool()
def cos(x: float) -> float:
    """Compute the cosine of x."""
    return math.cos(x)

@mcp.tool()
def cosh(x: float) -> float:
    """Compute the hyperbolic cosine of x."""
    return math.cosh(x)

@mcp.tool()
def degrees(x: float) -> float:
    """Convert x from radians to degrees."""
    return math.degrees(x)

@mcp.tool()
def erf(x: float) -> float:
    """Compute the error function of x."""
    return math.erf(x)

@mcp.tool()
def erfc(x: float) -> float:
    """Compute the complementary error function of x."""
    return math.erfc(x)

@mcp.tool()
def exp(x: float) -> float:
    """Compute e raised to the power of x."""
    return math.exp(x)

@mcp.tool()
def exp2(x: float) -> float:
    """Compute 2 raised to the power of x."""
    return math.exp2(x)

@mcp.tool()
def expm1(x: float) -> float:
    """Compute exp(x) - 1."""
    return math.expm1(x)

@mcp.tool()
def fabs(x: float) -> float:
    """Compute the absolute value of x."""
    return math.fabs(x)

@mcp.tool()
def factorial(x: int) -> int:
    """Compute the factorial of x."""
    return math.factorial(x)

@mcp.tool()
def floor(x: float) -> int:
    """Return the floor of x."""
    return math.floor(x)

@mcp.tool()
def frexp(x: float):
    """Return the mantissa and exponent of x."""
    return math.frexp(x)

@mcp.tool()
def gamma(x: float) -> float:
    """Compute the gamma function of x."""
    return math.gamma(x)

@mcp.tool()
def isfinite(x: float) -> bool:
    """Check if x is finite."""
    return math.isfinite(x)

@mcp.tool()
def isinf(x: float) -> bool:
    """Check if x is infinite."""
    return math.isinf(x)

@mcp.tool()
def isnan(x: float) -> bool:
    """Check if x is NaN."""
    return math.isnan(x)

@mcp.tool()
def isqrt(x: int) -> int:
    """Compute the integer square root of x."""
    return math.isqrt(x)

@mcp.tool()
def lgamma(x: float) -> float:
    """Compute the natural logarithm of the absolute value of the gamma function."""
    return math.lgamma(x)

@mcp.tool()
def log(x: float) -> float:
    """Compute the natural logarithm of x."""
    return math.log(x)

@mcp.tool()
def log10(x: float) -> float:
    """Compute the base-10 logarithm of x."""
    return math.log10(x)

@mcp.tool()
def log1p(x: float) -> float:
    """Compute log(1 + x)."""
    return math.log1p(x)

@mcp.tool()
def log2(x: float) -> float:
    """Compute the base-2 logarithm of x."""
    return math.log2(x)

@mcp.tool()
def modf(x: float):
    """Return the fractional and integer parts of x."""
    return math.modf(x)

@mcp.tool()
def radians(x: float) -> float:
    """Convert x from degrees to radians."""
    return math.radians(x)

@mcp.tool()
def sin(x: float) -> float:
    """Compute the sine of x."""
    return math.sin(x)

@mcp.tool()
def sinh(x: float) -> float:
    """Compute the hyperbolic sine of x."""
    return math.sinh(x)

@mcp.tool()
def sqrt(x: float) -> float:
    """Compute the square root of x."""
    return math.sqrt(x)

@mcp.tool()
def tan(x: float) -> float:
    """Compute the tangent of x."""
    return math.tan(x)

@mcp.tool()
def tanh(x: float) -> float:
    """Compute the hyperbolic tangent of x."""
    return math.tanh(x)

@mcp.tool()
def trunc(x: float) -> int:
    """Truncate x to an integer."""
    return math.trunc(x)


# Two-Parameter Functions (f(x, y))
@mcp.tool()
def atan2(x: float, y: float) -> float:
    """Compute atan2(x, y)."""
    return math.atan2(x, y)

@mcp.tool()
def copysign(x: float, y: float) -> float:
    """Return x with the sign of y."""
    return math.copysign(x, y)

@mcp.tool()
def fmod(x: float, y: float) -> float:
    """Compute x modulo y."""
    return math.fmod(x, y)

@mcp.tool()
def gcd(x: int, y: int) -> int:
    """Compute the greatest common divisor of x and y."""
    return math.gcd(x, y)

@mcp.tool()
def hypot(x: float, y: float) -> float:
    """Compute the Euclidean norm sqrt(x² + y²)."""
    return math.hypot(x, y)

@mcp.tool()
def isclose(x: float, y: float) -> bool:
    """Check if x and y are close."""
    return math.isclose(x, y)

@mcp.tool()
def lcm(x: int, y: int) -> int:
    """Compute the least common multiple of x and y."""
    return math.lcm(x, y)

@mcp.tool()
def ldexp(x: float, y: int) -> float:
    """Compute x * (2**y)."""
    return math.ldexp(x, y)

@mcp.tool()
def nextafter(x: float, y: float) -> float:
    """Return the next floating-point value after x toward y."""
    return math.nextafter(x, y)

@mcp.tool()
def pow(x: float, y: float) -> float:
    """Compute x raised to the power of y."""
    return math.pow(x, y)

@mcp.tool()
def remainder(x: float, y: float) -> float:
    """Compute the IEEE remainder of x divided by y."""
    return math.remainder(x, y)


if __name__ == "__main__":
    mcp.run()
