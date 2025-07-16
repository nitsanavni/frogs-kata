from frogs import solve_frog_problem, can_frogs_meet


def test_frogs_start_at_same_position() -> None:
    """Test when frogs start at the same position."""
    result = solve_frog_problem(
        apollo_start=0, apollo_velocity=3, 
        bubbles_start=0, bubbles_velocity=2, 
        equator_length=5
    )
    assert result == "0"


def test_frogs_same_velocity_different_positions() -> None:
    """Test when frogs have same velocity but different positions - should be impossible."""
    result = solve_frog_problem(
        apollo_start=0, apollo_velocity=3, 
        bubbles_start=1, bubbles_velocity=3, 
        equator_length=5
    )
    assert result == "Impossible"


def test_frogs_can_meet_simple_case() -> None:
    """Test a simple case where frogs can meet."""
    result = solve_frog_problem(
        apollo_start=0, apollo_velocity=3, 
        bubbles_start=1, bubbles_velocity=2, 
        equator_length=5
    )
    assert result == "1"
    
    # Verify they actually meet
    jumps = 1
    apollo_pos = (0 + jumps * 3) % 5
    bubbles_pos = (1 + jumps * 2) % 5
    assert apollo_pos == bubbles_pos == 3


def test_frogs_can_meet_after_multiple_jumps() -> None:
    """Test case where frogs meet after multiple jumps."""
    result = solve_frog_problem(
        apollo_start=0, apollo_velocity=2, 
        bubbles_start=1, bubbles_velocity=3, 
        equator_length=5
    )
    assert result == "4"
    
    # Verify they actually meet
    jumps = 4
    apollo_pos = (0 + jumps * 2) % 5
    bubbles_pos = (1 + jumps * 3) % 5
    assert apollo_pos == bubbles_pos == 3


def test_frogs_cannot_meet_large_circle() -> None:
    """Test case where frogs cannot meet on a larger circle."""
    result = solve_frog_problem(
        apollo_start=0, apollo_velocity=3, 
        bubbles_start=5, bubbles_velocity=1, 
        equator_length=10
    )
    assert result == "Impossible"


def test_frogs_meet_with_wraparound() -> None:
    """Test case where meeting involves wraparound."""
    result = solve_frog_problem(
        apollo_start=8, apollo_velocity=3, 
        bubbles_start=2, bubbles_velocity=1, 
        equator_length=10
    )
    assert result == "2"
    
    # Verify they meet
    jumps = 2
    apollo_pos = (8 + jumps * 3) % 10
    bubbles_pos = (2 + jumps * 1) % 10
    assert apollo_pos == bubbles_pos == 4


def test_frogs_equivalent_starting_positions() -> None:
    """Test when frogs start at equivalent positions (mod circle length)."""
    result = solve_frog_problem(
        apollo_start=0, apollo_velocity=2, 
        bubbles_start=10, bubbles_velocity=3, 
        equator_length=10
    )
    assert result == "0"


def test_frogs_backwards_relative_motion() -> None:
    """Test when one frog is effectively moving backwards relative to the other."""
    result = solve_frog_problem(
        apollo_start=0, apollo_velocity=1, 
        bubbles_start=0, bubbles_velocity=4, 
        equator_length=6
    )
    # They start at same position so should meet immediately
    assert result == "0"
    
    # Verify they meet at start
    jumps = 0
    apollo_pos = (0 + jumps * 1) % 6
    bubbles_pos = (0 + jumps * 4) % 6
    assert apollo_pos == bubbles_pos == 0


def test_extended_gcd_basic() -> None:
    """Test the extended GCD function with basic cases."""
    from frogs import extended_gcd
    
    # Test basic cases
    gcd, x, y = extended_gcd(10, 6)
    assert gcd == 2
    assert 10 * x + 6 * y == gcd
    
    gcd, x, y = extended_gcd(15, 25)
    assert gcd == 5
    assert 15 * x + 25 * y == gcd


def test_can_frogs_meet_returns_int() -> None:
    """Test that can_frogs_meet returns proper integer values."""
    result = can_frogs_meet(
        apollo_start=0, apollo_velocity=3, 
        bubbles_start=1, bubbles_velocity=2, 
        equator_length=5
    )
    assert isinstance(result, int)
    assert result == 1
    
    result = can_frogs_meet(
        apollo_start=0, apollo_velocity=3, 
        bubbles_start=1, bubbles_velocity=3, 
        equator_length=5
    )
    assert result == -1


def test_edge_case_zero_velocity() -> None:
    """Test edge case where one frog has zero velocity."""
    result = solve_frog_problem(
        apollo_start=0, apollo_velocity=0, 
        bubbles_start=1, bubbles_velocity=1, 
        equator_length=5
    )
    assert result == "4"
    
    # Verify: Apollo stays at 0, Bubbles starts at 1 and moves 1 per jump
    # After 4 jumps, Bubbles is at (1 + 4*1) % 5 = 0
    jumps = 4
    apollo_pos = (0 + jumps * 0) % 5
    bubbles_pos = (1 + jumps * 1) % 5
    assert apollo_pos == bubbles_pos == 0


def test_large_numbers() -> None:
    """Test with larger numbers to ensure algorithm scales."""
    result = solve_frog_problem(
        apollo_start=0, apollo_velocity=7, 
        bubbles_start=13, bubbles_velocity=3, 
        equator_length=100
    )
    
    if result != "Impossible":
        jumps = int(result)
        # Verify they meet
        apollo_pos = (0 + jumps * 7) % 100
        bubbles_pos = (13 + jumps * 3) % 100
        assert apollo_pos == bubbles_pos
    else:
        # If impossible, verify they can't meet by checking a few jumps
        for t in range(25):  # Check first 25 jumps
            apollo_pos = (0 + t * 7) % 100
            bubbles_pos = (13 + t * 3) % 100
            if apollo_pos == bubbles_pos:
                raise AssertionError(f"Frogs actually meet at jump {t}, but algorithm said Impossible")