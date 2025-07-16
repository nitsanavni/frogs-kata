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


def can_frogs_meet(
    apollo_start: int, apollo_velocity: int, 
    bubbles_start: int, bubbles_velocity: int, 
    equator_length: int
) -> int:
    """
    Determine if two frogs can meet and find minimum jumps.
    
    Args:
        apollo_start: Apollo's starting position
        apollo_velocity: Apollo's jump distance
        bubbles_start: Bubbles' starting position  
        bubbles_velocity: Bubbles' jump distance
        equator_length: Length of the equator
    
    Returns:
        int: Minimum number of jumps if they can meet, -1 if impossible
    """
    # Calculate relative velocity and initial distance
    rel_velocity = bubbles_velocity - apollo_velocity
    initial_distance = (apollo_start - bubbles_start) % equator_length
    
    # Handle case where frogs have same velocity
    if rel_velocity == 0:
        if initial_distance == 0:
            return 0  # They start at same position or equivalent positions
        else:
            return -1  # They'll never meet
    
    # We need to solve: t * rel_velocity ≡ -initial_distance (mod equator_length)
    # Because we want: (apollo_start + t*apollo_velocity) ≡ (bubbles_start + t*bubbles_velocity) (mod equator_length)
    # Which gives us: t*(apollo_velocity-bubbles_velocity) ≡ (bubbles_start-apollo_start) (mod equator_length)
    # So: t*(-rel_velocity) ≡ (-initial_distance) (mod equator_length)
    
    target = (-initial_distance) % equator_length
    coeff = (-rel_velocity) % equator_length
    
    gcd, x, y = extended_gcd(coeff, equator_length)
    
    # Check if solution exists
    if target % gcd != 0:
        return -1
    
    # Scale the solution
    scale = target // gcd
    t = x * scale
    
    # Get the smallest positive solution
    step = equator_length // gcd
    t = t % step
    if t < 0:
        t += step
    
    return t


def solve_frog_problem(
    apollo_start: int, apollo_velocity: int,
    bubbles_start: int, bubbles_velocity: int, 
    equator_length: int
) -> str:
    """
    Main function to solve the frog meeting problem.
    
    Args:
        apollo_start: Apollo's starting position
        apollo_velocity: Apollo's jump distance
        bubbles_start: Bubbles' starting position  
        bubbles_velocity: Bubbles' jump distance
        equator_length: Length of the equator
    
    Returns:
        str: Either the minimum number of jumps or "Impossible"
    """
    result = can_frogs_meet(apollo_start, apollo_velocity, bubbles_start, bubbles_velocity, equator_length)
    
    if result == -1:
        return "Impossible"
    else:
        return str(result)


