from flask import Flask, render_template_string

app = Flask(__name__)

# Factorial Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Prime Number Check Function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Fibonacci Series Function
def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

# Static input number
static_number = 10  # You can change this number

# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Logic Demo</title>
</head>
<body>
    <h2>Results for Number: {{ number }}</h2>
    <p>Factorial: {{ factorial }}</p>
    <p>Prime Check: {{ prime }}</p>
    <p>Fibonacci Series: {{ fibonacci }}</p>
</body>
</html>
"""

@app.route("/")
def home():
    # Use the static number
    number = static_number
    factorial_result = factorial(number)
    prime_result = "Yes" if is_prime(number) else "No"
    fibonacci_result = fibonacci(number)

    return render_template_string(HTML_TEMPLATE, number=number, factorial=factorial_result, prime=prime_result, fibonacci=fibonacci_result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

