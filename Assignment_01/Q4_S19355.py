
import math

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check if the discriminant is positive, negative, or zero to determine the number of solutions
    if discriminant > 0:
        # Two real and distinct solutions
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f'x = {x1} or x = {x2}')
    
    elif discriminant == 0:
        # One real solution
        x = -b / (2*a)
        print(f'x = {x}')

    else:
        print('No real solutions (complex roots)')

# Examples

solve_quadratic(5, 17, -10)
solve_quadratic(12, 10, 20)
solve_quadratic(1, 5, 6)