from pr_tutorial.simple_functions import factorial


def test_factorial_3():
    """Simplest test for one crete case"""

    # Fail and throw error if not !3==6
    assert factorial(3) == 6
