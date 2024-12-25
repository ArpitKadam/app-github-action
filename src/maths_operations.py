import math

def add(a,b):
    return print(f"The sum of a and b is: {a+b}")

def sub(a,b):
    return print(f"The difference of a and b is: {a-b}")

def mul(a,b):
    return print(f"The product of a and b is: {a*b}")

def div(a,b):
    return print(f"The division of a and b is: {a/b}")

def mod(a,b):
    return print(f"The modulus of a and b is: {a%b}")

def exp(a,b):
    return print(f"The exponent of a and b is: {a**b}")

def floor_div(a,b):
    return print(f"The floor division of a and b is: {a//b}")

def sqrt(a):
    return print(f"The square root of a is: {a**0.5}")

def cube(a):
    return print(f"The cube of a is: {a**3}")

def square(a):
    return print(f"The square of a is: {a**2}")

def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a-1)
    
def lcm(a,b):
    if a > b:
        greater = a
    else:
        greater = b
    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1
    return print(f"The LCM of a and b is: {lcm}")

def hcf(a,b):
    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller+1):
        if a % i == 0 and b % i == 0:
            hcf = i
    return print(f"The HCF of a and b is: {hcf}")

def is_prime(a):
    if a > 1:
        for i in range(2, a):
            if a % i == 0:
                return print(f"{a} is not a prime number")
                break
        else:
            return print(f"{a} is a prime number")
    else:
        return print(f"{a} is not a prime number")
    
def is_even(a):
    if a % 2 == 0:
        return print(f"{a} is an even number")
    else:
        return print(f"{a} is an odd number")
    
def is_odd(a):
    if a % 2 != 0:
        return print(f"{a} is an odd number")
    else:
        return print(f"{a} is an even number")
    
def is_armstrong(a):
    sum = 0
    temp = a
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if a == sum:
        return print(f"{a} is an Armstrong number")
    else:
        return print(f"{a} is not an Armstrong number")

def is_perfect(a):
    sum = 0
    for i in range(1, a):
        if a % i == 0:
            sum += i
    if a == sum:
        return print(f"{a} is a perfect number")
    else:
        return print(f"{a} is not a perfect number")
    
def is_palindrome(a):
    temp = a
    rev = 0
    while a > 0:
        dig = a % 10
        rev = rev * 10 + dig
        a = a // 10
    if temp == rev:
        return print(f"{temp} is a palindrome number")
    else:
        return print(f"{temp} is not a palindrome number")
    
def is_positive(a):
    if a > 0:
        return print(f"{a} is a positive number")
    else:
        return print(f"{a} is not a positive number")
    
def is_negative(a):
    if a < 0:
        return print(f"{a} is a negative number")
    else:
        return print(f"{a} is not a negative number")
    
def is_zero(a):
    if a == 0:
        return print(f"{a} is a zero number")
    else:
        return print(f"{a} is not a zero number")
    
def is_perfect_square(a):
    if a ** 0.5 == int(a ** 0.5):
        return print(f"{a} is a perfect square")
    else:
        return print(f"{a} is not a perfect square")
    
def is_perfect_cube(a):
    if a ** (1/3) == int(a ** (1/3)):
        return print(f"{a} is a perfect cube")
    else:
        return print(f"{a} is not a perfect cube")
    
def is_fibonacci(a):
    if (5 * a * a + 4) == int((5 * a * a + 4) ** 0.5) ** 2 or (5 * a * a - 4) == int((5 * a * a - 4) ** 0.5) ** 2:
        return print(f"{a} is a Fibonacci number")
    else:
        return print(f"{a} is not a Fibonacci number")

def is_factorial(a):
    i = 1
    while i < a:
        if factorial(i) == a:
            return print(f"{a} is a factorial number")
        i += 1
    return print(f"{a} is not a factorial number")

def is_harshad(a):
    sum = 0
    temp = a
    while temp > 0:
        digit = temp % 10
        sum += digit
        temp //= 10
    if a % sum == 0:
        return print(f"{a} is a Harshad number")
    else:
        return print(f"{a} is not a Harshad number")
    
def is_abundant(a):
    sum = 0
    for i in range(1, a):
        if a % i == 0:
            sum += i
    if sum > a:
        return print(f"{a} is an Abundant number")
    else:
        return print(f"{a} is not an Abundant number")
    
def is_deficient(a):
    sum = 0
    for i in range(1, a):
        if a % i == 0:
            sum += i
    if sum < a:
        return print(f"{a} is a Deficient number")
    else:
        return print(f"{a} is not a Deficient number")
    
def is_pronic(a):
    for i in range(1, a):
        if i * (i + 1) == a:
            return print(f"{a} is a Pronic number")
    return print(f"{a} is not a Pronic number")

def is_triangular(a):
    sum = 0
    i = 1
    while sum < a:
        sum += i
        i += 1
    if sum == a:
        return print(f"{a} is a Triangular number")
    else:
        return print(f"{a} is not a Triangular number")
    
def is_pentagonal(a):
    n = (1 + (1 + 24 * a) ** 0.5) / 6
    if n == int(n):
        return print(f"{a} is a Pentagonal number")
    else:
        return print(f"{a} is not a Pentagonal number")
    
def is_hexagonal(a):
    n = (1 + (1 + 8 * a) ** 0.5) / 4
    if n == int(n):
        return print(f"{a} is a Hexagonal number")
    else:
        return print(f"{a} is not a Hexagonal number")
    
def is_heptagonal(a):
    n = (3 + (9 + 40 * a) ** 0.5) / 10
    if n == int(n):
        return print(f"{a} is a Heptagonal number")
    else:
        return print(f"{a} is not a Heptagonal number")
    
def is_octagonal(a):
    n = (2 + (4 + 12 * a) ** 0.5) / 6
    if n == int(n):
        return print(f"{a} is a Octagonal number")
    else:
        return print(f"{a} is not a Octagonal number")

def is_prime_factors(a):
    for i in range(2, a):
        if a % i == 0:
            return print(f"{a} is not a prime number")
            break
    else:
        return print(f"{a} is a prime number")
    
def is_composite_factors(a):
    for i in range(2, a):
        if a % i == 0:
            return print(f"{a} is a composite number")
            break
    else:
        return print(f"{a} is not a composite number")
    
def is_composite(a):
    for i in range(2, a):
        if a % i == 0:
            return print(f"{a} is a composite number")
            break
    else:
        return print(f"{a} is not a composite number")
    
def is_deficient_prime(a):
    sum = 0
    for i in range(1, a):
        if a % i == 0:
            sum += i
    if sum < a:
        for i in range(2, a):
            if a % i == 0:
                return print(f"{a} is a deficient prime number")
                break
        else:
            return print(f"{a} is not a deficient prime number")
    else:
        return print(f"{a} is not a deficient prime number")

def is_abundant_prime(a):
    sum = 0
    for i in range(1, a):
        if a % i == 0:
            sum += i
    if sum > a:
        for i in range(2, a):
            if a % i == 0:
                return print(f"{a} is an abundant prime number")
                break
        else:
            return print(f"{a} is not an abundant prime number")
    else:
        return print(f"{a} is not an abundant prime number")
    
def is_perfect_square_prime(a):
    if a ** 0.5 == int(a ** 0.5):
        for i in range(2, a):
            if a % i == 0:
                return print(f"{a} is a perfect square prime number")
                break
        else:
            return print(f"{a} is not a perfect square prime number")
    else:
        return print(f"{a} is not a perfect square prime number")
    
def is_perfect_cube_prime(a):
    if a ** (1/3) == int(a ** (1/3)):
        for i in range(2, a):
            if a % i == 0:
                return print(f"{a} is a perfect cube prime number")
                break
        else:
            return print(f"{a} is not a perfect cube prime number")
    else:
        return print(f"{a} is not a perfect cube prime number")

def is_fibonacci_prime(a):
    if (5 * a * a + 4) == int((5 * a * a + 4) ** 0.5) ** 2 or (5 * a * a - 4) == int((5 * a * a - 4) ** 0.5) ** 2:
        for i in range(2, a):
            if a % i == 0:
                return print(f"{a} is a Fibonacci prime number")
                break
        else:
            return print(f"{a} is not a Fibonacci prime number")
    else:
        return print(f"{a} is not a Fibonacci prime number")
    
def is_factorial_prime(a):
    i = 1
    while i < a:
        if factorial(i) == a:
            for i in range(2, a):
                if a % i == 0:
                    return print(f"{a} is a factorial prime number")
                    break
            else:
                return print(f"{a} is not a factorial prime number")
        i += 1
    return print(f"{a} is not a factorial prime number")

def is_harshad_prime(a):
    sum = 0
    for i in str(a):
        sum += int(i)
    if a % sum == 0:
        for i in range(2, a):
            if a % i == 0:
                return print(f"{a} is a harshad prime number")
                break
        else:
            return print(f"{a} is not a harshad prime number")
    else:
        return print(f"{a} is not a harshad prime number")

def is_pronic_prime(a):
    for i in range(1, a):
        if i * (i + 1) == a:
            for i in range(2, a):
                if a % i == 0:
                    return print(f"{a} is a pronic prime number")
                    break
            else:
                return print(f"{a} is not a pronic prime number")
    return print(f"{a} is not a pronic prime number")
    
def is_triangular_prime(a):
    sum = 0
    i = 1
    while sum < a:
        sum += i
        i += 1
    if sum == a:
        for i in range(2, a):
            if a % i == 0:
                return print(f"{a} is a triangular prime number")
                break
        else:
            return print(f"{a} is not a triangular prime number")
    else:
        return print(f"{a} is not a triangular prime number")
    
def is_pentagonal_prime(a):
    n = (1 + (1 + 24 * a) ** 0.5) / 6
    if n == int(n):
        for i in range(2, a):
            if a % i == 0:
                return print(f"{a} is a pentagonal prime number")
                break
        else:
            return print(f"{a} is not a pentagonal prime number")
    else:
        return print(f"{a} is not a pentagonal prime number")
    
def is_hexagonal_prime(a):
    n = (1 + (1 + 8 * a) ** 0.5) / 4
    if n == int(n):
        for i in range(2, a):
            if a % i == 0:
                return print(f"{a} is a hexagonal prime number")
                break
        else:
            return print(f"{a} is not a hexagonal prime number")
    else:
        return print(f"{a} is not a hexagonal prime number")
    
def is_heptagonal_prime(a):
    n = (3 + (9 + 40 * a) ** 0.5) / 10
    if n == int(n):
        for i in range(2, a):
            if a % i == 0:
                return print(f"{a} is a heptagonal prime number")
                break
        else:
            return print(f"{a} is not a heptagonal prime number")
    else:
        return print(f"{a} is not a heptagonal prime number")
    
def is_octagonal_prime(a):
    n = (2 + (4 + 12 * a) ** 0.5) / 6
    if n == int(n):
        for i in range(2, a):
            if a % i == 0:
                return print(f"{a} is a octagonal prime number")
                break
        else:
            return print(f"{a} is not a octagonal prime number")
    else:
        return print(f"{a} is not a octagonal prime number")
    
def is_greater(a,b):
    if a > b:
        return print(f"{a} is greater than {b}")
    else:
        return print(f"{a} is not greater than {b}")
    
def is_smaller(a,b):
    if a < b:
        return print(f"{a} is smaller than {b}")
    else:
        return print(f"{a} is not smaller than {b}")

def is_equal(a,b):
    if a == b:
        return print(f"{a} is equal to {b}")
    else:
        return print(f"{a} is not equal to {b}")

def is_judgement(a,b,c):
    if a > b and a > c:
        return print(f"{a} is the greatest number")
    elif b > a and b > c:
        return print(f"{b} is the greatest number")
    elif c > a and c > b:
        return print(f"{c} is the greatest number")
    else:
        return print("The numbers are equal")

def is_positive_negative(a):
    if a > 0:
        return print(f"{a} is a positive number")
    elif a < 0:
        return print(f"{a} is a negative number")
    else:
        return print(f"{a} is zero")
    
def is_quadratic(a,b,c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return print(f"The roots are real and distinct")
    elif d == 0:
        return print(f"The roots are real and equal")
    else:
        return print(f"The roots are imaginary")

def is_cubic(a,b,c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return print(f"The roots are real and distinct")
    elif d == 0:
        return print(f"The roots are real and equal")
    else:
        return print(f"The roots are imaginary")
    
def is_quintic(a,b,c,d,e):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return print(f"The roots are real and distinct")
    elif d == 0:
        return print(f"The roots are real and equal")
    else:
        return print(f"The roots are imaginary")
    
def is_sextic(a,b,c,d,e,f):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return print(f"The roots are real and distinct")
    elif d == 0:
        return print(f"The roots are real and equal")
    else:
        return print(f"The roots are imaginary")

def is_septic(a,b,c,d,e,f,g):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return print(f"The roots are real and distinct")
    elif d == 0:
        return print(f"The roots are real and equal")
    else:
        return print(f"The roots are imaginary")
    
def is_octic(a,b,c,d,e,f,g,h):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return print(f"The roots are real and distinct")
    elif d == 0:
        return print(f"The roots are real and equal")
    else:
        return print(f"The roots are imaginary")
    
def is_nonic(a,b,c,d,e,f,g,h,i):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return print(f"The roots are real and distinct")
    elif d == 0:
        return print(f"The roots are real and equal")
    else:
        return print(f"The roots are imaginary")
    
def is_decic(a,b,c,d,e,f,g,h,i,j):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return print(f"The roots are real and distinct")
    elif d == 0:
        return print(f"The roots are real and equal")
    else:
        return print(f"The roots are imaginary")

def roots(a,b):
    r = -b / a
    return print(f"The root is {r}")
  
def roots(a,b,c):
    d = b ** 2 - 4 * a * c
    r = (-b + d ** 0.5) / 2 * a
    s = (-b - d ** 0.5) / 2 * a
    return print(f"The roots are {r} and {s}")

def discriminant(a,b,c):
    d = b ** 2 - 4 * a * c
    return print(f"The discriminant is {d}")

def roots(a,b,c,d):
    d = b ** 2 - 4 * a * c
    r = (-b + d ** 0.5) / 2 * a
    s = (-b - d ** 0.5) / 2 * a
    t = (-b + d ** 0.5) / 2 * a
    u = (-b - d ** 0.5) / 2 * a
    return print(f"The roots are {r}, {s}, {t} and {u}")
    
def roots(a,b,c,d,e):
    d = b ** 2 - 4 * a * c
    r = (-b + d ** 0.5) / 2 * a
    s = (-b - d ** 0.5) / 2 * a
    t = (-b + d ** 0.5) / 2 * a
    u = (-b - d ** 0.5) / 2 * a
    v = (-b + d ** 0.5) / 2 * a
    w = (-b - d ** 0.5) / 2 * a
    return print(f"The roots are {r}, {s}, {t}, {u}, {v} and {w}")

def roots(a,b,c,d,e,f):
    d = b ** 2 - 4 * a * c
    r = (-b + d ** 0.5) / 2 * a
    s = (-b - d ** 0.5) / 2 * a
    t = (-b + d ** 0.5) / 2 * a
    u = (-b - d ** 0.5) / 2 * a
    v = (-b + d ** 0.5) / 2 * a
    w = (-b - d ** 0.5) / 2 * a
    x = (-b + d ** 0.5) / 2 * a
    y = (-b - d ** 0.5) / 2 * a
    z = (-b + d ** 0.5) / 2 * a
    a = (-b - d ** 0.5) / 2 * a
    b = (-b + d ** 0.5) / 2 * a
    c = (-b - d ** 0.5) / 2 * a
    d = (-b + d ** 0.5) / 2 * a
    e = (-b - d ** 0.5) / 2 * a
    return  print(f"The roots are {r}, {s}, {t}, {u}, {v}, {w}, {x}, {y}, {z}, {a}, {b}, {c} and {d}")

def power(a,b):
    return print(f"{a} raised to the power of {b} is: {a**b}")
    return print(f"{b} raised to the power of {a} is: {b**a}") 
    return print(f"{a} raised to the power of {a} is: {a**a}")
    return print(f"{b} raised to the power of {b} is: {b**b}")

def power(a,b,c):
    return print(f"{a} raised to the power of {b} is: {a**b}")
    return print(f"{b} raised to the power of {a} is: {b**a}")
    return print(f"{a} raised to the power of {c} is: {a**c}")
    return print(f"{c} raised to the power of {a} is: {c**a}")
    return print(f"{b} raised to the power of {c} is: {b**c}")
    return print(f"{c} raised to the power of {b} is: {c**b}")
    return print(f"{a} raised to the power of {a} is: {a**a}")
    return print(f"{b} raised to the power of {b} is: {b**b}")
    return print(f"{c} raised to the power of {c} is: {c**c}")

def power(a,b,c,d):
    return print(f"{a} raised to the power of {b} is: {a**b}")
    return print(f"{b} raised to the power of {a} is: {b**a}")
    return print(f"{a} raised to the power of {c} is: {a**c}")
    return print(f"{c} raised to the power of {a} is: {c**a}")
    return print(f"{b} raised to the power of {c} is: {b**c}")
    return print(f"{c} raised to the power of {b} is: {c**b}")
    return print(f"{a} raised to the power of {d} is: {a**d}")
    return print(f"{d} raised to the power of {a} is: {d**a}")
    return print(f"{b} raised to the power of {d} is: {b**d}")
    return print(f"{d} raised to the power of {b} is: {d**b}")
    return print(f"{c} raised to the power of {d} is: {c**d}")
    return print(f"{d} raised to the power of {c} is: {d**c}")
    return print(f"{a} raised to the power of {a} is: {a**a}")
    return print(f"{b} raised to the power of {b} is: {b**b}")
    return print(f"{c} raised to the power of {c} is: {c**c}")
    return print(f"{d} raised to the power of {d} is: {d**d}")

def kth_root(a,b):
    return print(f"The {b}th root of {a} is: {a ** (1/b)}")
    return print(f"The {b}th root of {a} is: {a ** (1/b)}")

def kth_root(a,b,c):
    return print(f"The {b}th root of {a} is: {a ** (1/b)}")
    return print(f"The {b}th root of {b} is: {b ** (1/b)}")
    return print(f"The {b}th root of {c} is: {c ** (1/b)}") 
    return print(f"The {c}th root of {a} is: {a ** (1/c)}")
    return print(f"The {c}th root of {b} is: {b ** (1/c)}")
    return print(f"The {c}th root of {c} is: {c ** (1/c)}")
    return print(f"The {a}th root of {b} is: {b ** (1/a)}")
    return print(f"The {a}th root of {c} is: {c ** (1/a)}")
    return print(f"The {a}th root of {a} is: {a ** (1/a)}")

def absolute(a):
    return print(f"The absolute value of {a} is: {abs(a)}")

def absolute(a,b):
    return print(f"The absolute value of {a} is: {abs(a)}")
    return print(f"The absolute value of {b} is: {abs(b)}")

def absolute(a,b,c):
    return print(f"The absolute value of {a} is: {abs(a)}")
    return print(f"The absolute value of {b} is: {abs(b)}")
    return print(f"The absolute value of {c} is: {abs(c)}")

def absolute(a,b,c,d):
    return print(f"The absolute value of {a} is: {abs(a)}")
    return print(f"The absolute value of {b} is: {abs(b)}")
    return print(f"The absolute value of {c} is: {abs(c)}")
    return print(f"The absolute value of {d} is: {abs(d)}")

def intercept(a,b):
    return print(f"The x-intercept of the line is: {a}")
    return print(f"The y-intercept of the line is: {b}")

def intercept(a,b,c):
    return print(f"The x-intercept of the line is: {a}")
    return print(f"The y-intercept of the line is: {b}")
    return print(f"The z-intercept of the line is: {c}")

def slope(a,b):
    return print(f"The slope of the line is: {a/b}")

def sine(a):
    return print(f"The sine of {a} is: {math.sin(a)}")

def cosine(a):
    return print(f"The cosine of {a} is: {math.cos(a)}")

def tangent(a):
    return print(f"The tangent of {a} is: {math.tan(a)}")

def secant(a):
    return print(f"The secant of {a} is: {1/math.cos(a)}")

def cosecant(a):
    return print(f"The cosecant of {a} is: {1/math.sin(a)}")

def cotangent(a):
    return print(f"The cotangent of {a} is: {1/math.tan(a)}")

def arcsine(a):
    return print(f"The arcsine of {a} is: {math.asin(a)}")

def arccosine(a):
    return print(f"The arccosine of {a} is: {math.acos(a)}")

def arctangent(a):
    return print(f"The arctangent of {a} is: {math.atan(a)}")

def arcsecant(a):
    return print(f"The arcsecant of {a} is: {math.acos(1/a)}")

def arccosecant(a):
    return print(f"The arccosecant of {a} is: {math.asin(1/a)}")

def arccotangent(a):
    return print(f"The arccotangent of {a} is: {math.atan(1/a)}")

def hyperbolic_sine(a):
    return print(f"The hyperbolic sine of {a} is: {math.sinh(a)}")

def hyperbolic_cosine(a):
    return print(f"The hyperbolic cosine of {a} is: {math.cosh(a)}")

def hyperbolic_tangent(a):
    return print(f"The hyperbolic tangent of {a} is: {math.tanh(a)}")

def hyperbolic_secant(a):
    return print(f"The hyperbolic secant of {a} is: {1/math.cosh(a)}")

def hyperbolic_cosecant(a):
    return print(f"The hyperbolic cosecant of {a} is: {1/math.sinh(a)}")

def hyperbolic_cotangent(a):
    return print(f"The hyperbolic cotangent of {a} is: {1/math.tanh(a)}")

def hyperbolic_arcsine(a):
    return print(f"The hyperbolic arcsine of {a} is: {math.asinh(a)}")

def hyperbolic_arccosine(a):
    return print(f"The hyperbolic arccosine of {a} is: {math.acosh(a)}")

def hyperbolic_arctangent(a):
    return print(f"The hyperbolic arctangent of {a} is: {math.atanh(a)}")

def hyperbolic_arcsecant(a):
    return print(f"The hyperbolic arcsecant of {a} is: {math.acosh(1/a)}")

def hyperbolic_arccosecant(a):
    return print(f"The hyperbolic arccosecant of {a} is: {math.asinh(1/a)}")

def hyperbolic_arccotangent(a):
    return print(f"The hyperbolic arccotangent of {a} is: {math.atanh(1/a)}")

def logarithm(a):
    return print(f"The logarithm of {a} is: {math.log(a)}")

def logarithm(a,b):
    return print(f"The logarithm of {a} to the base {b} is: {math.log(a,b)}")


