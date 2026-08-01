from fractions import Fraction
from src.claim1_quadratic_slp_toy import bit_lsb, quadratic_multiply, eval_slp, INSTANCES

def test_quadratic_gadget_exact_on_rationals():
    for x in [Fraction(-3,2), Fraction(0), Fraction(7,3)]:
        for y in [Fraction(-5,4), Fraction(2), Fraction(9,7)]:
            assert quadratic_multiply(x,y) == x*y

def test_fixture_matches_independent_expected_values():
    for _, program, expected in INSTANCES:
        got, _ = eval_slp(program)
        assert got == expected

def test_destructive_control_is_detected():
    assert any(eval_slp(p, corrupt=True)[0] != expected for _,p,expected in INSTANCES)

def test_bits_follow_pinned_absolute_numerator_convention():
    assert [bit_lsb(Fraction(-7),j) for j in range(4)] == [1,1,1,0]
