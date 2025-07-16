from typing import Tuple


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Extended Euclidean Algorithm
    Returns (gcd, x, y) such that a*x + b*y = gcd(a, b)
    """
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd, x, y


def can_frogs_meet(x1: int, v1: int, x2: int, v2: int, total_length: int) -> int:
    """
    Determine if two frogs can meet and find minimum jumps.
    
    Args:
        x1: Apollo's starting position
        v1: Apollo's jump distance
        x2: Bubbles' starting position  
        v2: Bubbles' jump distance
        total_length: Length of the equator
    
    Returns:
        int: Minimum number of jumps if they can meet, -1 if impossible
    """
    # Calculate relative velocity and initial distance
    rel_velocity = v2 - v1
    initial_distance = (x1 - x2) % total_length
    
    # Handle case where frogs have same velocity
    if rel_velocity == 0:
        if initial_distance == 0:
            return 0  # They start at same position or equivalent positions
        else:
            return -1  # They'll never meet
    
    # We need to solve: t * rel_velocity ≡ -initial_distance (mod total_length)
    # Because we want: (x1 + t*v1) ≡ (x2 + t*v2) (mod total_length)
    # Which gives us: t*(v1-v2) ≡ (x2-x1) (mod total_length)
    # So: t*(-rel_velocity) ≡ (-initial_distance) (mod total_length)
    
    target = (-initial_distance) % total_length
    coeff = (-rel_velocity) % total_length
    
    gcd, x, y = extended_gcd(coeff, total_length)
    
    # Check if solution exists
    if target % gcd != 0:
        return -1
    
    # Scale the solution
    scale = target // gcd
    t = x * scale
    
    # Get the smallest positive solution
    step = total_length // gcd
    t = t % step
    if t < 0:
        t += step
    
    return t


def solve_frog_problem(x1: int, v1: int, x2: int, v2: int, total_length: int) -> str:
    """
    Main function to solve the frog meeting problem.
    
    Returns:
        str: Either the minimum number of jumps or "Impossible"
    """
    result = can_frogs_meet(x1, v1, x2, v2, total_length)
    
    if result == -1:
        return "Impossible"
    else:
        return str(result)


